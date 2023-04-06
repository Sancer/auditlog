from abc import abstractmethod
from uuid import uuid4

from django.db import models


class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    instance_type = models.CharField(max_length=250)
    instance_id = models.IntegerField()
    previous_state = models.JSONField()
    actual_state = models.JSONField()
    author = models.CharField(max_length=250)
    created = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.instance_type}:{self.instance_id}:{self.created.isoformat()}"


class Auditable(models.Model):
    @abstractmethod
    def get_auditable_type(self):
        # I don't use the __class__.__name__ to avoid that if you change the class it changes without realizing it.
        raise NotImplementedError

    class Meta:
        abstract = True
