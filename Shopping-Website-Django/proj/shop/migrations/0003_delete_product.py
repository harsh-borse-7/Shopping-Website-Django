# Generated by Django 4.2.1 on 2023-05-29 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_delete_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
