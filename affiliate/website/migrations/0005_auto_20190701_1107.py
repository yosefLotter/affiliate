# Generated by Django 2.2 on 2019-07-01 11:07

from django.db import migrations
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20190701_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='project_code',
            field=django_bleach.models.BleachField(blank=True, null=True),
        ),
    ]