# Generated by Django 4.0.5 on 2022-07-04 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_alter_movie_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Аниме'), (3, 'Сериал'), (2, 'Фильм')], null=True, verbose_name='type'),
        ),
    ]
