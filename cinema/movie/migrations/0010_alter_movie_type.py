# Generated by Django 4.0.5 on 2022-07-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_alter_movie_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Сериал'), (1, 'Аниме'), (2, 'Фильм')], null=True, verbose_name='type'),
        ),
    ]
