# orders/controllers.py
from rest_framework.request import Request

from apps.orders.apis.gateways import orders


def list_controller(self, request: Request):
    """Handle list method core logic."""
    group_by_date = request.query_params.get('group_by_date')
    filters = {
        "group_by_date": group_by_date
    }
    return orders.filter_queryset(
        self,
        filters=filters
    )
