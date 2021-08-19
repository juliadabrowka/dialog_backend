from django.db import models


class Serie(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    slug = models.SlugField(max_length=100, blank=False, unique=True)
    image = models.ImageField(upload_to='uploads/')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return f'/serie/{self.slug}/'

    def get_image(self):
            return 'http://127.0.0.1:8000' + self.image.url


class Token(models.Model):
    serie = models.ForeignKey(Serie, related_name='tokens', on_delete=models.CASCADE)
    number = models.CharField(max_length=200)
    author = models.CharField(max_length=300)
    title = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    date = models.DateField(auto_now=True)

    def get_image(self):
            return 'http://127.0.0.1:8000' + self.image.url