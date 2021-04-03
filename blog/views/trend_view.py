from typing import Dict, Any

from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from blog.models import PostEntity, CommentEntity, TrendEntity
from blog.serializers.trend_serializer import TrendSerializer
from commons.base_view import BaseView
from commons.payload_param_name import PayloadParamName


class TrendView(BaseView,
                CreateAPIView,
                UpdateAPIView,
                DestroyAPIView):
    http_method_names = [
        'post',
        'put',
        'delete',
    ]
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs, ):
        super().__init__(*args, **kwargs)
        self.comment_entity = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self.post_id = request.query_params.get(PayloadParamName.id)
        self.post_entity = PostEntity.objects.get(id=self.post_id)
        self.comment_id = request.query_params.get(PayloadParamName.comment_id)

        if self.comment_id:
            self.comment_entity = CommentEntity.objects.get(id=self.comment_id)

    def create(self, request, *args, **kwargs):
        result: Dict[str, Any] = dict()
        if TrendEntity().check_if_user_liked_or_disliked_before(user_id=self.user.id, post_id=self.post_id,
                                                                comment_id=self.comment_id):
            result[PayloadParamName.error] = "You have liked/disliked before!"
            return Response(data=result, status=status.HTTP_403_FORBIDDEN)

        initial_data = request.data
        serializer = TrendSerializer(data=initial_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user_id=self.user.id, post_id=self.post_id, comment_id=self.comment_id)
            result[PayloadParamName.data] = serializer.data
            result[PayloadParamName.success] = "Trend created successfully!"

            return Response(data=result, status=status.HTTP_201_CREATED)

        result[PayloadParamName.error] = "Creating trend failed!"
        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
