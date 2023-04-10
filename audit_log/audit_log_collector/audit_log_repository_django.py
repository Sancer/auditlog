from datetime import datetime, timedelta
from logging import getLogger

from django.conf import settings

from audit_log.models import Log as LogModel

from .audit_log_repository import AuditLogRepository, Log
from .paginated_respone import PaginatedResponse

logger = getLogger(__name__)


class AuditLogRepositoryDjango(AuditLogRepository):
    def save(self, log: Log) -> None:
        # it could be done with __dict__ and then spread operator, but I prefer to be explicit
        log_model = LogModel(
            instance_type=log.instance_type,
            instance_id=log.instance_id,
            previous_state=log.previous_state,
            actual_state=log.actual_state,
            author=log.author,
            created=log.created,
        )
        log_model.save()

    def search(
        self,
        instance_type: str = None,
        instance_id: int = None,
        created_from: str = None,
        created_to: str = None,
        author: str = None,
        limit: int = settings.PAGINATION_PAGE_SIZE,
        offset: int = 0,
    ) -> PaginatedResponse[Log]:
        default_creted_from = datetime.now() - timedelta(
            days=7
        )  # TODO: move the magic number to settings
        filters = {}
        created_from = created_from if created_from else default_creted_from

        if instance_type:
            filters["instance_type"] = instance_type

        if instance_id:
            filters["instance_id"] = instance_id

        if created_from:
            filters["created__gte"] = created_from

        if created_to:
            filters["created__lte"] = created_to

        if author:
            # TODO: We would have to consult the filtering strategy e.g.: (start, exact, ...)
            filters["author__icontains"] = author

        logs = LogModel.objects.filter(**filters)
        paginated_logs = logs[offset:offset+limit]

        return PaginatedResponse(
            count=logs.count(), results=[self._to_native(log) for log in paginated_logs]
        )

    def _to_native(self, log: LogModel) -> Log:
        return Log(
            instance_type=log.instance_type,
            instance_id=log.instance_id,
            previous_state=log.previous_state,
            actual_state=log.actual_state,
            author=log.author,
            created=log.created,
        )


# TODO: move it to a dependency container
audit_log_repository = AuditLogRepositoryDjango()
