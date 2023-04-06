from rest_framework import serializers

from audit_log.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"


class SearchQueryParamsLogSerializer(serializers.Serializer):
    instance_id = serializers.IntegerField()
    # TODO: aquí sería bueno poner las choises con un enum
    instance_type = serializers.CharField()
    created_from = serializers.DateTimeField(required=False)
    created_to = serializers.DateTimeField(required=False)
    author = serializers.CharField(required=False)

    class Meta:
        fields = (
            "instance_id",
            "instance_type",
            "created_from",
            "created_to",
            "author",
        )
