# Generated by Django 2.2 on 2019-07-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_loser'),
    ]

    operations = [
        migrations.AddField(
            model_name='loser',
            name='meta_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='loser',
            name='meta_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
