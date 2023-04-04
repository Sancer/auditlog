from rest_framework import generics

from audit_log.models import Log
from audit_log.serializers import LogSerializer


class ListLogView(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
