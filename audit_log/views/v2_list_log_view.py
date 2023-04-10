from django.http import JsonResponse
from rest_framework.generics import GenericAPIView

from audit_log.audit_log_collector import PaginatedResponse, Log, AuditLogRepository
from audit_log.audit_log_collector.audit_log_repository_django import (
    audit_log_repository,
)
from audit_log.serializers import SearchQueryParamsLogSerializer, LogSerializer


class V2ListLogView(GenericAPIView):
    audit_log_repository: AuditLogRepository = audit_log_repository
    serializer_class = LogSerializer  # only for open-api/swagger

    def get(self, request):
        serializer = SearchQueryParamsLogSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        search = serializer.data
        response: PaginatedResponse[Log] = self.audit_log_repository.search(**search)
        context = response.dict()
        # TODO: falta definir la paginación (con el limite de elementos por pagina)
        return JsonResponse(data=context)
