# Generated by Django 5.0 on 2024-03-30 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shortener', '0002_remove_url_urlinput_url_link_alter_url_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='uuid',
            field=models.CharField(max_length=10),
        ),
    ]
