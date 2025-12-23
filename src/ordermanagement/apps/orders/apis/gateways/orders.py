from django.db.models import Count
from django.db.models.functions import TruncDate
from django.db.models import QuerySet

from apps.orders.models import Orders as OrderModel
from apps.orders.apis.v1.serializers.order import OrderAggregateSerializer


def filter_queryset(self, filters: dict):
    """Filter queryset"""
    queryset = self.filter_queryset(self.get_queryset())
    if filters.get("group_by_date") in [True, "true"]:
        queryset = (
            OrderModel.objects
            .annotate(order_date=TruncDate("order_create_date"))
            .values("order_date")
            .annotate(total_orders=Count("id"))
            .order_by("-order_date")
        )

        page = self.paginate_queryset(queryset)

        date_to_orders = {}
        date_list = [d["order_date"] for d in page]

        orders_qs = OrderModel.objects.filter(
            order_create_date__date__in=date_list,
        ).order_by("order_create_date")
        for o in orders_qs:
            date_to_orders.setdefault(o.order_create_date.date(), []).append(o)

        queryset = [
            {
                "order_date": d["order_date"],
                "total_orders": d["total_orders"],
                "orders": date_to_orders.get(d["order_date"], [])
            }
            for d in page
        ]

    if isinstance(queryset, QuerySet):
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    serializer = OrderAggregateSerializer(queryset, many=True)
    return self.get_paginated_response(serializer.data)
