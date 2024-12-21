# Generated by Django 5.1.4 on 2024-12-21 15:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_creating_post_model'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=5000)),
                ('creation_date', models.DateTimeField()),
                ('update_date', models.DateTimeField(null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('responded_comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment_Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_liked', models.BooleanField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='users_reactions',
            field=models.ManyToManyField(related_name='comment_users_reactions', through='blog.Comment_Reaction', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Post_Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_liked', models.BooleanField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='users_reactions',
            field=models.ManyToManyField(related_name='post_users_reactions', through='blog.Post_Reaction', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Saved_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag_In_Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tag')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(through='blog.Tag_In_Post', to='blog.tag'),
        ),
        migrations.AddConstraint(
            model_name='comment_reaction',
            constraint=models.UniqueConstraint(models.F('comment'), models.F('user'), name='unique_comment_reaction'),
        ),
        migrations.AddConstraint(
            model_name='post_reaction',
            constraint=models.UniqueConstraint(models.F('post'), models.F('user'), name='unique_post_reaction'),
        ),
        migrations.AddConstraint(
            model_name='saved_post',
            constraint=models.UniqueConstraint(models.F('post'), models.F('user'), name='unique_saved_post'),
        ),
        migrations.AddConstraint(
            model_name='tag_in_post',
            constraint=models.UniqueConstraint(models.F('post'), models.F('tag'), name='unique_tag_in_post'),
        ),
    ]