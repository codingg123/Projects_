# Generated by Django 4.1.5 on 2024-01-19 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marks_app', '0009_staff_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]