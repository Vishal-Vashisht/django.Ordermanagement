# decorators.py
from functools import wraps
import traceback
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from .exceptions import (
    BaseOrderExceptions,
    ValidationError,
)
from rest_framework import status

import logging

logger = logging.getLogger(__name__)


def api_exception_handler(func):
    """
    Standardized API exception handler.
    Converts all exceptions to consistent format.
    """

    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            return func(request, *args, **kwargs)

        except APIException as e:
            error_details = e.get_full_details()
            error_response = ValidationError(
                invalid_params=error_details
            )
            return Response(error_response._to_dict(), status=e.status_code)

        except BaseOrderExceptions as e:
            error_response = e._to_dict()
            return Response(error_response, status=e.status_code)
        except Exception as e:
            print(e, traceback.format_exc())
            error_response = {
                "detail": "Something wen wrong internally, we are working on to fix this"
            }
            return Response(
                error_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    return wrapper


def api_exception_handler_cls(
        default_decorate: bool = False,
):
    def decorator(cls):
        methods_to_decorate = getattr(cls, "decorate_methods", [])
        # wrap standard CRUD methods
        crud_methods = ["list", "retrieve", "create", "update", "partial_update", "destroy"]
        if default_decorate:
            for method_name in crud_methods:
                if hasattr(cls, method_name):
                    orig = getattr(cls, method_name)
                    setattr(cls, method_name, api_exception_handler(orig))

        if methods_to_decorate:
            for method_name in methods_to_decorate:
                if hasattr(cls, method_name):
                    orig = getattr(cls, method_name)
                    setattr(cls, method_name, api_exception_handler(orig))

        return cls
    return decorator
