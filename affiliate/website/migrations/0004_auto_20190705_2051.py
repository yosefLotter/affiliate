# Generated by Django 2.2 on 2019-07-05 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190704_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Montly_subscribes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namn', models.CharField(blank=True, max_length=50)),
                ('email_adress', models.CharField(blank=True, max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Customer',
            new_name='Contact_us',
        ),
    ]
