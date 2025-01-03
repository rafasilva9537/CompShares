# Generated by Django 5.1.4 on 2024-12-19 23:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_creating_custom_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_users', to=settings.AUTH_USER_MODEL)),
                ('follower_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='folllows',
            field=models.ManyToManyField(through='accounts.Follow', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(models.F('followed_user'), models.F('follower_user'), name='unique_user_follows'),
        ),
    ]
