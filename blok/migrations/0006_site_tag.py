# Generated by Django 4.2.6 on 2023-11-11 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blok', '0005_tab_delete_file_delete_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='tag',
            field=models.CharField(choices=[('Szkola', 'Szkola'), ('Osobiste', 'Osobiste'), ('Inne', 'Inne')], default='Szkola', max_length=10),
        ),
    ]
