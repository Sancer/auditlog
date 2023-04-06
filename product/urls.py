from django.urls import path

from .views import (
    ListCreateProductView,
    RetrieveUpdateDestroyProductView,
    RetrieveUpdateDestroyCategoryView,
    ListCreateCategoryView,
)

app_name = "product"
urlpatterns = [
    path(
        "product/<int:pk>/",
        RetrieveUpdateDestroyProductView.as_view(),
        name="retrieve_update_destroy_product",
    ),
    path("product/", ListCreateProductView.as_view(), name="list_create_product"),
    path(
        "category/<int:pk>/",
        RetrieveUpdateDestroyCategoryView.as_view(),
        name="retrieve_update_destroy_category",
    ),
    path("category/", ListCreateCategoryView.as_view(), name="list_create_category"),
]
