from django_filters import FilterSet, CharFilter, DateTimeFilter

from audit_log.models import Log


class LogFilter(FilterSet):
    instance_type = CharFilter(lookup_expr="iexact")
    instance_id = CharFilter(lookup_expr="exact")
    created_from = DateTimeFilter(
        field_name="created",
        lookup_expr="gte",
    )
    created_to = DateTimeFilter(field_name="created", lookup_expr="lte")

    class Meta:
        model = Log
        fields = ("instance_type", "instance_id", "author")
