from django.db import models

from audit_log.models import Auditable


class Product(Auditable, models.Model):
    title = models.CharField(max_length=250, null=True, blank=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    example_field3 = models.IntegerField(null=True, blank=True)
    example_field4 = models.BooleanField(null=True, blank=True)
    example_field5 = models.DateField(null=True, blank=True)
    example_field6 = models.DateTimeField(null=True, blank=True)
    example_field7 = models.FloatField(null=True, blank=True)
    example_field8 = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    example_field9 = models.JSONField(null=True, blank=True)
    example_field10 = models.PositiveBigIntegerField(null=True, blank=True)
    example_field11 = models.PositiveIntegerField(null=True, blank=True)
    example_field12 = models.PositiveSmallIntegerField(null=True, blank=True)
    example_field13 = models.TimeField(null=True, blank=True)
    example_field14 = models.UUIDField(null=True, blank=True)
    example_field15 = models.URLField(null=True, blank=True)

    def get_auditable_type(self):
        return "product"
