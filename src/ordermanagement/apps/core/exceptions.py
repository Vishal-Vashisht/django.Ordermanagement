# exceptions.py
from datetime import datetime


class BaseOrderExceptions(Exception):
    """Base exception for order-related errors"""

    def __init__(
        self,
        detail: str = "",
        code: int = 400,
        title: str = "Error",
        invalid_params: list = None,
    ):
        self.detail = detail
        self.code = code
        self.title = title
        self.error_code = code or self._get_error_code(code)
        self.invalid_params = invalid_params or []
        super().__init__(detail)

    def _get_error_code(self, http_code: int) -> str:
        """Map HTTP status to error code"""
        code_map = {
            400: "BAD_REQUEST",
            401: "UNAUTHORIZED",
            403: "FORBIDDEN",
            404: "NOT_FOUND",
            409: "CONFLICT",
            500: "INTERNAL_SERVER_ERROR",
        }
        return code_map.get(http_code, "ERROR")

    def _to_dict(self) -> dict:
        """Convert exception to standard error format"""
        return {
            "success": False,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "code": self.code,
            "detail": self.detail,
            "invalid_params": self.invalid_params or [],
            "title": self.title,
        }


# Specific exception types
class OrderNotFoundException(BaseOrderExceptions):
    def __init__(self, order_id: int):
        super().__init__(
            detail=f"Order with ID {order_id} not found",
            code=404,
            error_code="ORDER_NOT_FOUND",
        )


class InsufficientBalanceException(BaseOrderExceptions):
    def __init__(self, required: float, available: float):
        super().__init__(
            detail=f"Insufficient balance. Required: ${required}, Available: ${available}",
            code=400,
            error_code="INSUFFICIENT_BALANCE",
        )


class OrderAlreadyProcessedException(BaseOrderExceptions):
    def __init__(self, order_id: int):
        super().__init__(
            detail=f"Order {order_id} has already been processed",
            code=409,
            error_code="ORDER_ALREADY_PROCESSED",
        )


class InvalidParameter(BaseOrderExceptions):
    """Invalid Parameter Exception Class handling incorrect arguments."""

    def __init__(
        self,
        title: str,
        invalid_params: list | None = None,
        code: str | None = "",
        detail: str | None = "",
        status_code: int = 400,
    ) -> None:
        self.status_code = status_code

        super().__init__(
            title=title,
            invalid_params=invalid_params,
            detail=detail,
            code=code,
        )


class ValidationError(BaseOrderExceptions):
    def __init__(self, invalid_params):
        self.status_code = 400

        super().__init__(
            detail="Missing Required Fields",
            code=400,
            invalid_params=invalid_params or [],
            title="Validation Error",
        )
