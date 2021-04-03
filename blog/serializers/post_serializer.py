from rest_framework import serializers

from blog.models.post_entity import PostEntity
from commons.payload_param_name import PayloadParamName


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostEntity

        exclude = [
            PayloadParamName.user,
        ]


class ReadPostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField('get_post_comments')

    def get_post_comments(self, post_entity: PostEntity):
        return post_entity.post_comments

    class Meta:
        model = PostEntity

        exclude = [
            PayloadParamName.user,
        ]
