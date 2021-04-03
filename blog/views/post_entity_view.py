from typing import Dict, Any

from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from blog.models import PostEntity, CommentEntity
from blog.serializers.post_serializer import PostSerializer, ReadPostSerializer
from commons.base_view import BaseView
from commons.payload_param_name import PayloadParamName
from identity.models import UserEntity


class PostEntityView(BaseView,
                     CreateAPIView,
                     UpdateAPIView,
                     DestroyAPIView):
    http_method_names = [
        'get',
        'post',
        'put',
        'delete',
    ]
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)
        self.post_id: int = None
        self.user: UserEntity = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.post_id = request.query_params.get(PayloadParamName.id)

    def post(self, request, *args, **kwargs):
        self.post_entity = PostEntity.objects.get(id=self.post_id)
        initial_data = request.data
        result: Dict[str, Any] = dict()
        serializer = PostSerializer(data=initial_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=self.user.id)
            result[PayloadParamName.data] = serializer.data
            result[PayloadParamName.success] = "Post created successfully!"

            return Response(data=result, status=status.HTTP_201_CREATED)

        result[PayloadParamName.error] = "Creating post failed!"
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        self.post_entity = PostEntity.objects.get(id=self.post_id)
        result: Dict[str, Any] = dict()

        if not self.post_entity.check_post_permission(self.user.id):
            result[PayloadParamName.error] = "You don't have permission to update this post"
            return Response(data=result, status=status.HTTP_400_BAD_REQUEST)

        initial_data = request.data
        serializer = PostSerializer(data=initial_data, instance=self.post_entity)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            result[PayloadParamName.data] = serializer.data
            result[PayloadParamName.success] = "Post updated successfully!"

            return Response(data=result, status=status.HTTP_201_CREATED)

        result[PayloadParamName.error] = "Updating post failed!"
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        result: Dict[str, Any] = dict()

        if not self.post_entity.check_post_permission(self.user.id):
            result[PayloadParamName.error] = "You don't have permission to delete this post"
            return Response(data=result, status=status.HTTP_400_BAD_REQUEST)

        self.post_entity.delete()
        result[PayloadParamName.success] = "Post deleted successfully",

        return Response(data=result, status=status.HTTP_200_OK)


class ListPostEntityView(BaseView, ListAPIView):
    http_method_names = [
        'get',
    ]

    permission_classes = (AllowAny,)

    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)
        self.post_id: int = None
        self.user: UserEntity = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.post_id = request.query_params.get(PayloadParamName.id)

    def get(self, request, *args, **kwargs):
        result: Dict[str, Any] = dict()
        if self.post_id:
            self.post_entity_queryset = PostEntity.objects.filter(id=self.post_id)
        else:
            self.post_entity_queryset = PostEntity.objects.all()

        for post_entity in self.post_entity_queryset:
            result[post_entity.id] = {
                PayloadParamName.title: post_entity.title,
                PayloadParamName.body: post_entity.body,
            }

            # PayloadParamName.comments: {
            #     PayloadParamName.body: comment_body
            #     for comment_body in
            #     CommentEntity.objects.filter(post_id=post_entity.id).values(PayloadParamName.body)
            # }

            result[post_entity.id][PayloadParamName.comments] = list(
                CommentEntity.objects.filter(post_id=post_entity.id).order_by('post_id',
                                                                              'parent_comment_id',
                                                                              ).values(
                    PayloadParamName.id,
                    PayloadParamName.body,
                    PayloadParamName.parent_comment_id,
                    # PayloadParamName.post_id,
                ))

            # for post_comment in post_comments:
            #     post_id = post_comments.get(PayloadParamName.post_id)
            #     while post_id == post_comments.get(PayloadParamName.post_id):
            #         result[post_entity.id][PayloadParamName.comments] = {
            #             PayloadParamName.body
            #         }

        return Response(data=result, status=status.HTTP_200_OK)
