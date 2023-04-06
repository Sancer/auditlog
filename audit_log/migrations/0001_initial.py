# Generated by Django 4.1.7 on 2023-04-06 21:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("instance_type", models.CharField(max_length=250)),
                ("instance_id", models.IntegerField()),
                ("previous_state", models.JSONField()),
                ("actual_state", models.JSONField()),
                ("author", models.CharField(max_length=250)),
                ("created", models.DateTimeField()),
            ],
        ),
    ]
