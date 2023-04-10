from audit_log.audit_log_collector.audit_log_model_collector import (
    AuditLogModelCollector,
)
from audit_log.audit_log_collector.audit_log_repository_django import (
    AuditLogRepositoryDjango,
)
from audit_log.enums import ImplementedModelsEnum
from audit_log.middlewares import get_current_user
from django.db.models import Model
from django.db.models.signals import pre_save
from django.dispatch import receiver

audit_log_collector = AuditLogModelCollector(
    auditlog_repository=AuditLogRepositoryDjango()
)


@receiver(pre_save)
def ingest(sender: Model, instance, *args, **kwargs):
    try:
        instance_type = ImplementedModelsEnum(instance.__class__.__name__)
    except ValueError:
        return

    try:
        previous_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    user = get_current_user()
    # the author value (str) is delegated to USER_CLASS, this is opinionated
    audit_log_collector(
        actual_instance=instance,
        previous_instance=previous_instance,
        author=str(user),
        instance_type=instance_type,
    )
