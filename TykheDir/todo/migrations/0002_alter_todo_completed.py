# Generated by Django 3.2 on 2021-04-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
