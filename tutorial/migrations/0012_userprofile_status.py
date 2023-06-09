# Generated by Django 3.0 on 2020-04-07 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0011_auto_20200407_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('USER', 'USER'), ('BLOCK', 'BLOCK'), ('DEACTIVE', 'DEACTIVE')], default='USER', max_length=100),
        ),
    ]