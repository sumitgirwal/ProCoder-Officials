# Generated by Django 3.0 on 2020-04-09 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0017_auto_20200408_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='view',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
