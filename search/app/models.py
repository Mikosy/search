from django.db import models

# Create your models here.




class Movies(models.Model):

    movie_genre =(
        ('HORROR', 'horror'),
        ('SCI-FI', 'sci-fi'),
        ('ROMANCE', 'romance'),
        ('DRAMA', 'drama'),
        ('COMEDY', 'comedy'),
        ('ACTION', 'action'),
    )


    title =  models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')
    description = models.TextField()
    release_year = models.CharField(max_length=50)
    genre = models.CharField(choices=movie_genre, max_length=200)

    class Meta:
        ordering =('-title',)
        verbose_name_plural = 'Movies'


    def __str__(self):
        return self.title





    # slug = models.SlugField()
    # related_post = models.BooleanField(default=False)
    # status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.name
