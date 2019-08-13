from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Books(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    author_book = models.CharField(max_length=500, default='')
    book = models.CharField(max_length=200)
    cat = models.CharField(max_length=200)
    sub_cat = models.CharField(max_length=200)
    read = models.BooleanField()
    link = models.CharField(max_length=500)
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.book

class HelpfulResources(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=700)

    def __str__(self):
        return self.description