# Generated by Django 3.0 on 2020-04-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0022_auto_20200410_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
