# Generated by Django 3.0 on 2020-04-17 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendindeed', '0003_auto_20200418_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='from_user',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='friend',
            name='to_user',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
