# Generated by Django 2.2 on 2019-07-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_auto_20190713_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meta_tags_for_winner',
            name='meta_description',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='meta_tags_for_winner',
            name='meta_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
