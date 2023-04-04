from datetime import datetime, timedelta
from logging import getLogger

from audit_log.audit_log_collector.audit_log_model_collector import AuditLogRepository, Log
from audit_log.models import Log as LogModel

logger = getLogger(__name__)


class AuditLogRepositoryDjango(AuditLogRepository):
    def save(self, log: Log) -> None:
        log_model = LogModel(  # TODO: se podría hacer con __dict__ y luego spread operator, pero prefiero ser explicito
            instance_type=log.instance_type,
            instance_id=log.instance_id,
            previos_state=log.previous_state,
            actual_state=log.actual_state,
            author=log.author,
            created=log.created,
        )
        log_model.save()

    def search(self, instance_type: str, instance_id: int, created_from: str = None, created_to: str = None,
               author: str = None) -> list[Log]:
        default_creted_from = datetime.now() - timedelta(days=7)  # TODO: mover el magic number a settings
        created_from = created_from if created_from else default_creted_from
        filters = {
            "instance_type": instance_type,
            "instance_id": instance_id,
            "created__gte": created_from,
        }

        if created_to:
            filters['created__lte'] = created_to

        if author:
            # TODO: Tendríamos que consultar la estategía de filtrado ejem: (start, exact, ...)
            filters['author__icontains'] = author

        logs = LogModel.objects.filter(**filters)

        return [self._to_native(log) for log in logs]

    def _to_native(self, log: LogModel) -> Log:
        return Log(
            instance_type=log.instance_type,
            instance_id=log.instance_id,
            previous_state=log.previous_state,
            actual_state=log.actual_state,
            author=log.author,
            created=log.created,
        )


# TODO: sacarlo a un contenedor de dependencias, hago esto así para no estar generando instancías todo el rato
audit_log_repository = AuditLogRepositoryDjango()
