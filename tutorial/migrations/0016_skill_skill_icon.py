# Generated by Django 3.0 on 2020-04-08 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0015_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='skill_icon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
