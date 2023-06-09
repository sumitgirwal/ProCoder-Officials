# Generated by Django 3.0 on 2020-04-17 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tutorial', '0034_auto_20200412_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=200, null=True)),
                ('to_user', models.CharField(max_length=200, null=True)),
                ('friend', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('from_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_info', to='tutorial.UserProfile')),
                ('to_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_info', to='tutorial.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CRID', models.CharField(max_length=200, null=True)),
                ('message', models.TextField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutorial.UserProfile')),
            ],
        ),
    ]