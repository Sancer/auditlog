from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from audit_log.filters import LogFilter
from audit_log.models import Log
from audit_log.serializers import LogSerializer


class ListLogView(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LogFilter
