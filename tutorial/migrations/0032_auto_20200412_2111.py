# Generated by Django 3.0 on 2020-04-12 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorial', '0031_auto_20200412_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='starby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]