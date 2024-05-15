# Generated by Django 5.0.6 on 2024-05-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.URLField(default='https://imdb-api.com/images/128x176/nopicture.jpg', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.URLField(default='https://imdb-api.com/images/128x176/nopicture.jpg', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='thumbnail',
            field=models.URLField(default='https://imdb-api.com/images/128x176/nopicture.jpg', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.URLField(default='https://imdb-api.com/images/128x176/nopicture.jpg', null=True),
        ),
    ]
