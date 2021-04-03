from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from commons.payload_param_name import PayloadParamName
from identity.models import UserEntity


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserEntity
        fields = [
            PayloadParamName.first_name,
            PayloadParamName.last_name,
            PayloadParamName.email,
            PayloadParamName.is_active,
            PayloadParamName.password,
        ]
        extra_kwargs = {
            PayloadParamName.password: {
                PayloadParamName.write_only: True,
            },
        }

    def create(self, validated_data):
        try:
            validate_password(validated_data[PayloadParamName.password])
        except ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError({
                'password': serializer_error['non_field_errors']
            })
        user = UserEntity.objects.create(**{
            PayloadParamName.first_name: validated_data[PayloadParamName.first_name],
            PayloadParamName.last_name: validated_data[PayloadParamName.last_name],
            PayloadParamName.email: validated_data[PayloadParamName.email],
            PayloadParamName.is_active: True,

        })

        user.set_password(validated_data[PayloadParamName.password])
        user.save()

        return user
