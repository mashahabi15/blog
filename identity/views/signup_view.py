from typing import Any, Dict

from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from commons.payload_param_name import PayloadParamName
from identity.serializers.user_entity_serializer import UserSignUpSerializer


class SignupView(CreateAPIView):
    serializer_class = UserSignUpSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        initial_data: Dict[str, Any] = request.data
        result: Dict[str, Any] = dict()
        serializer = self.get_serializer(data=initial_data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            result[PayloadParamName.data] = serializer.data
            result[PayloadParamName.success] = "User registered successfully!"
            if user:
                return Response(data=result, status=status.HTTP_201_CREATED)

        result[PayloadParamName.error] = "User signup failed!"

        return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
