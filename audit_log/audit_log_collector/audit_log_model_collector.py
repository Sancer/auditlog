from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

from django.db.models import Model
from django.forms import model_to_dict
from django.utils import timezone

from audit_log.models import Auditable


@dataclass
class Log:
    instance_type: str
    instance_id: int
    previous_state: dict
    actual_state: dict
    author: str
    created: datetime

    def dict(self):
        return self.__dict__


class AuditLogRepository(ABC):
    @abstractmethod
    def save(self, log: Log) -> None:
        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        instance_type: str,
        instance_id: int,
        created_from: str = None,
        created_to: str = None,
        author: str = None,
    ) -> list[Log]:
        raise NotImplementedError


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
        return model_to_dict(instance, fields=self.model_fields)
