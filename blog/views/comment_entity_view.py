from typing import Dict, Any

from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from blog.models import PostEntity, CommentEntity
from blog.serializers.comment_serializer import CommentSerializer
from blog.serializers.post_serializer import PostSerializer
from commons.base_view import BaseView
from commons.payload_param_name import PayloadParamName
from identity.models import UserEntity


class CommentEntityView(BaseView,
                        CreateAPIView, ):
    http_method_names = [
        'post',
    ]
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)
        self.post_id: int = None
        self.user: UserEntity = None
        self.parent_comment_entity = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.post_id = request.query_params.get(PayloadParamName.id)
        self.post_entity = PostEntity.objects.get(id=self.post_id)
        self.parent_comment_id = request.query_params.get(PayloadParamName.comment_id)
        if self.parent_comment_id:
            self.parent_comment_entity = CommentEntity.objects.get(id=self.parent_comment_id)

    def post(self, request, *args, **kwargs):
        initial_data = request.data
        result: Dict[str, Any] = dict()
        serializer = CommentSerializer(data=initial_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=self.user.id, post_id=self.post_id, parent_comment_id=self.parent_comment_id)
            result[PayloadParamName.data] = serializer.data
            result[PayloadParamName.success] = "Comment created successfully!"

            return Response(data=result, status=status.HTTP_201_CREATED)

        result[PayloadParamName.error] = "Creating comment failed!"
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)


class ListCommentView(BaseView, ListAPIView):
    http_method_names = [
        'get',
    ]

    permission_classes = (AllowAny,)

    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)
        self.post_id: int = None
        self.user: UserEntity = None
        self.parent_comment_entity = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.post_id = request.query_params.get(PayloadParamName.id)
        self.post_entity = PostEntity.objects.get(id=self.post_id)
        self.parent_comment_id = request.query_params.get(PayloadParamName.comment_id)
        if self.parent_comment_id:
            self.parent_comment_entity = CommentEntity.objects.get(id=self.parent_comment_id)

    def get(self, request, *args, **kwargs):
        self.comment_id = request.query_params.get(PayloadParamName.comment_id)
        if self.comment_id:
            comment_queryset = CommentEntity.objects.filter(id=self.comment_id)
        else:
            comment_queryset = CommentEntity.objects.filter(post_id=self.post_id)

        result = comment_queryset.values(PayloadParamName.id, PayloadParamName.body,
                                         PayloadParamName.parent_comment_id, )

        return Response(data=result, status=status.HTTP_200_OK)
