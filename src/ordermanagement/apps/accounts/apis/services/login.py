"""Login service implementation."""

from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.conf import settings

from apps.accounts import constants


def set_response_cookie(
        response: Response,
        refresh: RefreshToken,
) -> Response:
    """
    Set cookie in response object.

    Args:
    ----
        response(Response): Response object

    Returns:
    -------
        Response: Response set http cookie
    """
    response.set_cookie(
        key=constants.REFRESH_KEY,
        value=str(refresh),
        httponly=True,
        secure=True,
        samesite=constants.STRICT_POLICY,
        path=constants.REFRESH_PATH,
        max_age=settings.SIMPLE_JWT.get("REFRESH_TOKEN_LIFETIME").total_seconds(),

    )

    return response
