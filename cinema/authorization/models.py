from django.db import models

class MSManager(models.Manager):
    def create_movie(self, movie_id, name, score, user_id):
        movie = self.create(movieId=movie_id, movie_name=name, score=score, user_id=user_id)
        return movie

class movieScore(models.Model):
    movieId = models.IntegerField(null=True)
    movie_name = models.CharField(max_length=50, null=True)
    score = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)
    objects = MSManager()

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return str(self.movie_name) + " оценено на " + str(self.score) + " баллов;"

class UserManager(models.Manager):
    def create_user(self, login, password, email, ava):
        user = self.create(login=login, password=password, email=email, ava=ava)
        return user

    def get_password(self, log):
        user = User.objects.get(login=log)
        return user.password

    def get_email(self, log):
        user = User.objects.get(login=log)
        return user.email

    def get_ava(self, log):
        user = User.objects.get(login=log)
        print(user.ava)

class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    ava = models.ImageField(upload_to='avatar', blank=True)
    #movie = models.ForeignKey(movieScore, on_delete=models.CASCADE, null=True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.login