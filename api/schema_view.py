from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="PoC Api with audit log",
        default_version='v1',
        description="Example of system to generate audit log",
        contact=openapi.Contact(email="urielreina@gmail.com"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
