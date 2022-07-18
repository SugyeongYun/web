from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    topic = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    contents = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
