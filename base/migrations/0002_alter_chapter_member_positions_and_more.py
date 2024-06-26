# Generated by Django 5.0.6 on 2024-05-26 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='member_positions',
            field=models.ManyToManyField(blank=True, related_name='chapters', to='base.chaptermemberposition'),
        ),
        migrations.AlterField(
            model_name='mainprofile',
            name='Chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='base.chaptername'),
        ),
    ]
