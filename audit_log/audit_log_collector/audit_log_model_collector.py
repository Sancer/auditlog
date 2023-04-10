import json

from django.db.models import Model
from django.forms import model_to_dict
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder

from .audit_log_repository import Log, AuditLogRepository
from audit_log.models import Auditable


class AuditLogModelCollector:
    auditlog_repository: AuditLogRepository

    def __init__(self, auditlog_repository: AuditLogRepository):
        self.auditlog_repository = auditlog_repository

    def __call__(
        self, actual_instance: Auditable, previous_instance: Auditable, author: str
    ) -> list:
        self.model_fields = self.get_fields(instance=actual_instance)

        log = Log(
            instance_type=actual_instance.get_auditable_type(),
            instance_id=actual_instance.pk,
            actual_state=self.get_raw_data(instance=actual_instance),
            previous_state=self.get_raw_data(instance=previous_instance),
            author=author,
            created=timezone.now(),
        )
        self.auditlog_repository.save(log=log)

    def get_fields(self, instance: Model) -> list:
        return [field.name for field in instance.__class__._meta.fields]

    def get_raw_data(self, instance: Model) -> dict:
        native_data = json.dumps(model_to_dict(instance, fields=self.model_fields), cls=DjangoJSONEncoder)
        return json.loads(native_data)


