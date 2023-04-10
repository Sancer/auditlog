from django.urls import path

from .views import ListLogView, V2ListLogView

app_name = "audit_log"
urlpatterns = [
    path(
        "v1/log/", ListLogView.as_view(), name="v1_list_log"
    ),  # django standard
    path(
        "v2/log/", V2ListLogView.as_view(), name="v2_list_log"
    ),  # implementing dependency inversion to allow easy change of persistence
]
