import django_filters

from product.models import Category


class CategoryFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ('title',)
