# Generated by Django 5.0.6 on 2024-05-15 04:23

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('movie_page', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.movie')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_profile', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentsLikesDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=False)),
                ('disliked', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comments')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='user_ld',
            field=models.ManyToManyField(through='comments.CommentsLikesDislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('movie_page', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.movie')),
                ('parent_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='comments.comments')),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reply_profile', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Replies', to=settings.AUTH_USER_MODEL)),
                ('user_replying_to', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='replied_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RepliesLikesDislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked', models.BooleanField(default=False)),
                ('disliked', models.BooleanField(default=False)),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.replies')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='replies',
            name='user_ld',
            field=models.ManyToManyField(through='comments.RepliesLikesDislike', to=settings.AUTH_USER_MODEL),
        ),
    ]
