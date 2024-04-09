# Generated by Django 5.0.2 on 2024-02-27 04:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_alter_bio_burning_desire_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "bio_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "connections_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "testimonials_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "gallery_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "email_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "contact_details_visibility",
                    models.CharField(
                        choices=[
                            ("all", "All"),
                            ("connections", "My Connections"),
                            ("none", "None"),
                        ],
                        default="all",
                        max_length=12,
                    ),
                ),
                (
                    "post_notifications",
                    models.CharField(
                        choices=[
                            ("every_time", "Every time a new post is added"),
                            ("daily", "Once per day (daily digest)"),
                            ("weekly", "Once per week (weekly digest)"),
                            ("never", "Do not email me"),
                        ],
                        default="every_time",
                        max_length=10,
                    ),
                ),
                (
                    "alternate_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                ("forward_messages", models.BooleanField(default=False)),
                ("forward_sent_mail", models.BooleanField(default=False)),
                ("forward_connection_requests", models.BooleanField(default=False)),
                ("forward_recommendation_requests", models.BooleanField(default=False)),
                (
                    "country_settings_for_group_notifications",
                    models.CharField(default="Default", max_length=50),
                ),
                (
                    "alternate_notification_email",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="account_settings",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
