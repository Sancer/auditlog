from django.db import models


class Category(models.Model):
    log_type = 'category'

    example_field1 = models.CharField(max_length=250, null=True, blank=True)
    example_field2 = models.CharField(max_length=250, null=True, blank=True)
    example_field3 = models.CharField(max_length=250, null=True, blank=True)
    example_field4 = models.CharField(max_length=250, null=True, blank=True)
    example_field5 = models.CharField(max_length=250, null=True, blank=True)
    example_field6 = models.CharField(max_length=250, null=True, blank=True)
    example_field7 = models.CharField(max_length=250, null=True, blank=True)
    example_field8 = models.CharField(max_length=250, null=True, blank=True)
    example_field9 = models.CharField(max_length=250, null=True, blank=True)
    example_field10 = models.CharField(max_length=250, null=True, blank=True)
    example_field11 = models.CharField(max_length=250, null=True, blank=True)
