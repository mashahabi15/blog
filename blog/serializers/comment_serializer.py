from django.db import models
from rest_framework import serializers

from blog.models import CommentEntity, PostEntity
from commons.payload_param_name import PayloadParamName


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentEntity
        exclude = [
            PayloadParamName.post,
            PayloadParamName.user,
            PayloadParamName.parent_comment,
        ]
