# Generated by Django 3.0 on 2020-04-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0006_auto_20200405_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]
