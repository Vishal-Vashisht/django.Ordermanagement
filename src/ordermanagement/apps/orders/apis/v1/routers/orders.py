from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

# App imports
from apps.orders.models import Orders
from apps.orders.apis.v1.serializers import OrderSerializer
from apps.core.paginator import paginate
from apps.orders.apis.v1.controllers.orders import list_controller
from apps.core.request_handler import (
    api_exception_handler_cls
)


@api_exception_handler_cls(
    default_decorate=True,
)
class OrderViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    pagination_class = paginate
    decorate_methods = ["order_aggregator"]

    @action(detail=False, methods=["get"], url_path="aggregate")
    def order_aggregator(self, request, *args, **kwargs):
        """Aggregate orders data."""
        return list_controller(self, request)
