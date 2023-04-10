from abc import abstractmethod
from uuid import uuid4

from django.db import models

from audit_log.enums import ImplementedModelsEnum


class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    instance_type = models.CharField(max_length=250, choices=ImplementedModelsEnum.choices())
    instance_id = models.IntegerField()
    previous_state = models.JSONField()
    actual_state = models.JSONField()
    author = models.CharField(max_length=250)
    created = models.DateTimeField()

    index_together = [
        ["instance_type", "instance_id", "created"],
    ]

    def __str__(self) -> str:
        return f"{self.instance_type}:{self.instance_id}:{self.created.isoformat()}"
