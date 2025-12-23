from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from apps.accounts.apis.v1 import serializers
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError
from django.conf import settings
from apps.core.exceptions import InvalidParameter
from apps.accounts import messages
from apps.accounts.apis.services import login as login_service


def login_controller(data: dict):
    """
    Docstring for login_controller

    :param data: Description
    :type data: dict
    """
    serializer = serializers.LoginSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]
    refresh = RefreshToken.for_user(
        user=user,
    )

    response = Response(
        {
            "access_token": str(refresh.access_token),
        }
    )
    return login_service.set_response_cookie(
        response=response,
        refresh=refresh,
    )


def cookie_refresh_token_handler(
    refresh_token: str,
) -> Response:
    """
    Docstring for cookie_refresh_token_handler

    :param refresh_token: Description
    :type refresh_token: str
    :return: Description
    :rtype: Response
    """
    if not refresh_token:
        raise InvalidParameter(
            title=messages.REFRESH_TOKEN_MISSING,
        )

    try:
        refresh = RefreshToken(refresh_token)
        access_token = str(refresh.access_token)
        if settings.SIMPLE_JWT.get("ROTATE_REFRESH_TOKENS"):
            refresh.set_jti()
            refresh.set_exp()
            refresh_token = str(refresh)

        response = Response({"access": access_token}, status=200)

        return login_service.set_response_cookie(
            response=response,
            refresh=refresh,
        )

    except TokenError:
        raise InvalidParameter(
            title=messages.REFRESH_TOKEN_MISSING,
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
