# Generated by Django 3.0 on 2020-04-12 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorial', '0029_remove_userprofile_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='starby',
        ),
        migrations.AddField(
            model_name='rating',
            name='is_rating',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='rating_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tutorial.UserProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
