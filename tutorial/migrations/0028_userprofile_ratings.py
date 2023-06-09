# Generated by Django 3.0 on 2020-04-12 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0027_remove_userprofile_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ratings',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=0, max_length=3),
        ),
    ]
