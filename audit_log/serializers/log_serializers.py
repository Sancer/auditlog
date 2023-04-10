from django.conf import settings
from rest_framework import serializers

from audit_log.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"


class SearchQueryParamsLogSerializer(serializers.Serializer):
    instance_id = serializers.IntegerField(required=False)
    instance_type = serializers.CharField(required=False)
    created_from = serializers.DateTimeField(required=False)
    created_to = serializers.DateTimeField(required=False)
    author = serializers.CharField(required=False)
    limit = serializers.IntegerField(required=False)
    offset = serializers.IntegerField(required=False)

    class Meta:
        fields = (
            "instance_id",
            "instance_type",
            "created_from",
            "created_to",
            "author",
        )
