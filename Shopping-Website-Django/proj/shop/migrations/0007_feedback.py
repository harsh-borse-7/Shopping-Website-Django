# Generated by Django 4.2.1 on 2023-05-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=1000)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
    ]
