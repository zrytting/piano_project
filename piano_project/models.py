from django.db import models
from django.utils.text import slugify

# Create your models here.

class teacher(models.Model):
    name = models.CharField(max_length=200)
    studio = models.CharField(max_length=500)
    message = models.TextField(max_length=2000)
    about = models.TextField(max_length=2000)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20)
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(teacher, self).save(*args, **kwargs)

    photo = models.ImageField(upload_to='images/')

    
