from django.http import JsonResponse
from rest_framework.views import APIView

from audit_log.audit_log_collector.audit_log_model_collector import AuditLogRepository, Log
from audit_log.audit_log_collector.audit_log_repository_django import audit_log_repository
from audit_log.serializers import SearchQueryParamsLogSerializer


class V2ListLogView(APIView):
    audit_log_repository: AuditLogRepository = audit_log_repository

    def get(self, request):
        serializer = SearchQueryParamsLogSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        search = serializer.data
        logs: list[Log] = self.audit_log_repository.search(**search)
        context = {
            'results': [log.dict() for log in logs]
        }
        # TODO: falta definir la paginación (con el limite de elementos por pagina)
        return JsonResponse(data=context)
