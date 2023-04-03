from django.db.models import Model
from django.db.models.signals import pre_save
from django.dispatch import receiver

from audit_log.audit_log_collector.audit_log_model_collector import AuditLogModelCollector
from audit_log.audit_log_collector.audit_log_repository_django import AuditLogRepositoryDjango

audit_log_collector = AuditLogModelCollector(auditlog_repository=AuditLogRepositoryDjango())


@receiver(pre_save)
def ingest(sender: Model, instance, *args, **kwargs):
    if not hasattr(instance, 'log_type'):
        return

    try:
        previous_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return

    audit_log_collector(actual_instance=instance, previous_instance=previous_instance, author='pending')
