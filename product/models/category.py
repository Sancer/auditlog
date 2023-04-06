from django.db import models

from audit_log.models import Auditable


class Category(Auditable, models.Model):
    title = models.CharField(max_length=250, null=True, blank=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    example_field3 = models.CharField(max_length=250, null=True, blank=True)
    example_field4 = models.CharField(max_length=250, null=True, blank=True)
    example_field5 = models.CharField(max_length=250, null=True, blank=True)
    example_field6 = models.CharField(max_length=250, null=True, blank=True)
    example_field7 = models.CharField(max_length=250, null=True, blank=True)
    example_field8 = models.CharField(max_length=250, null=True, blank=True)
    example_field9 = models.CharField(max_length=250, null=True, blank=True)
    example_field10 = models.CharField(max_length=250, null=True, blank=True)
    example_field11 = models.CharField(max_length=250, null=True, blank=True)
    example_field12 = models.CharField(max_length=250, null=True, blank=True)
    example_field13 = models.CharField(max_length=250, null=True, blank=True)
    example_field14 = models.CharField(max_length=250, null=True, blank=True)
    example_field15 = models.CharField(max_length=250, null=True, blank=True)

    def get_auditable_type(self):
        return "category"
