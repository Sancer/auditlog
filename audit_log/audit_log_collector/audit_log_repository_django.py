from logging import getLogger

from audit_log.models import Log as LogModel
from audit_log.audit_log_collector.audit_log_model_collector import AuditLogRepository, Log

logger = getLogger(__name__)


class AuditLogRepositoryDjango(AuditLogRepository):
    def save(self, log: Log) -> None:
        log_model = LogModel(
            instance_type=log.instance_type,
            instance_id=log.instance_id,
            previos_state=log.previous_state,
            actual_state=log.actual_state,
            author=log.author,
            created=log.created,
        )
        log_model.save()
