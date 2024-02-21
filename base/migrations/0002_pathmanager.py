# Generated by Django 4.1.9 on 2023-12-28 04:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PathManager",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("path", models.CharField(max_length=400)),
                ("file", models.FileField(upload_to="Files/")),
                ("category", models.CharField(max_length=50)),
                ("title", models.CharField(max_length=255)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
