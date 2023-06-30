from django.db import models

class MovieManager(models.Manager):
    def get_name(self, movie_id):
        movie = Movie.objects.get(pk=movie_id)
        return movie.name

class Movie(models.Model):

    objects = MovieManager()
    TYPES = {
        (1, 'Аниме'),
        (2, 'Фильм'),
        (3, 'Сериал')
    }

    name = models.CharField(max_length=40)
    type = models.PositiveSmallIntegerField( ("type"), choices=TYPES, null=True)
    description = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to='movie')
    torrent = models.FileField(upload_to='torrent', null=True)
    NUsersEstimated = models.IntegerField(null=True, blank=True)
    inter_score = models.FloatField(null=True, blank=True)
    movieTotalScore = models.FloatField(null=True, blank=True)
    name_lower = models.CharField(max_length=255, null=True, editable=False)

    def save(self, *args, **kwargs):
        self.name_lower = self.name.lower() if self.name else None
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильм'

    def __str__(self):
        return self.name
