from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from apps.core.request_handler import api_exception_handler_cls
from apps.accounts.apis.v1.controllers import (
    login_controller,
    cookie_refresh_token_handler
)


@api_exception_handler_cls()
class LoginHandler(APIView):
    permission_classes = [AllowAny]
    decorate_methods = ["post"]

    def post(self, request):
        """
        Docstring for post

        :param self: Description
        :param request: Description
        """
        return login_controller(request.data)


@api_exception_handler_cls()
class RefreshTokenHandler(APIView):
    """
    Docstring for RefreshTokenHandler
    """
    permission_classes = [AllowAny]
    decorate_methods = ["post"]

    def post(self, request):
        # Get refresh token from HttpOnly cookie
        refresh_token = request.COOKIES.get("refresh_token")
        return cookie_refresh_token_handler(
            refresh_token=refresh_token,
        )
