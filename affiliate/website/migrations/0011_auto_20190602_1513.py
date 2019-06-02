# Generated by Django 2.1.7 on 2019-06-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20190601_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='winner',
            old_name='a_first_small_content',
            new_name='a_content',
        ),
        migrations.RenameField(
            model_name='winner',
            old_name='a_top_big_title',
            new_name='a_title',
        ),
        migrations.RenameField(
            model_name='winner',
            old_name='a_top_big_content',
            new_name='b_content',
        ),
        migrations.RenameField(
            model_name='winner',
            old_name='b_top_big_title',
            new_name='b_title',
        ),
        migrations.RenameField(
            model_name='winner',
            old_name='b_first_small_content',
            new_name='c_content',
        ),
        migrations.RenameField(
            model_name='winner',
            old_name='b_top_big_content',
            new_name='d_content',
        ),
        migrations.RemoveField(
            model_name='winner',
            name='a_first_small_title',
        ),
        migrations.RemoveField(
            model_name='winner',
            name='b_first_small_title',
        ),
        migrations.AddField(
            model_name='article',
            name='name_of_article',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='winner',
            name='c_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='winner',
            name='d_title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='winner',
            name='profil_bild',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
    ]
