from rest_framework import serializers

from blog.models import TrendEntity
from commons.payload_param_name import PayloadParamName


class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrendEntity
        exclude = [
            PayloadParamName.user,
            PayloadParamName.post,
            PayloadParamName.comment,
        ]
