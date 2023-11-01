# Generated by Django 4.2.6 on 2023-10-31 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blok', '0003_remove_file_upload_remove_photo_upload_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.TextField(default='file'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='upload',
            field=models.FileField(default='01.09.1939', upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='upload',
            field=models.ImageField(default='01.09.1939', upload_to='uploads/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='URL_link',
            field=models.URLField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='site',
            name='name',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]