# Generated by Django 2.2 on 2019-07-07 16:35

from django.db import migrations
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_article_links_lottery_supplier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lottery_supplier',
            name='content_box_4',
        ),
        migrations.RemoveField(
            model_name='lottery_supplier',
            name='content_box_5',
        ),
        migrations.RemoveField(
            model_name='lottery_supplier',
            name='content_box_6',
        ),
        migrations.AddField(
            model_name='lottery_supplier',
            name='link_1',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AddField(
            model_name='lottery_supplier',
            name='link_2',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AddField(
            model_name='lottery_supplier',
            name='link_3',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AlterField(
            model_name='article_links',
            name='article_1',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AlterField(
            model_name='article_links',
            name='article_10',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AlterField(
            model_name='article_links',
            name='article_2',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AlterField(
            model_name='article_links',
            name='article_3',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AlterField(
            model_name='article_links',
            name='article_4',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AlterField(
            model_name='article_links',
            name='article_5',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AlterField(
            model_name='article_links',
            name='article_6',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AlterField(
            model_name='article_links',
            name='article_7',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AlterField(
            model_name='article_links',
            name='article_8',
            field=django_bleach.models.BleachField(blank=True),
        ),
        migrations.AlterField(
            model_name='article_links',
            name='article_9',
            field=django_bleach.models.BleachField(blank=True),
        ),
    ]