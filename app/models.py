from django.db import models
from django.shortcuts import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# from django.utils import timezone
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextUploadingField()
    publish = models.DateField(auto_now_add=True)


    # get url of unique id
    def get_absolute_url(self):
        return reverse("app1:news-query", args=[str(self.id), self.title])

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'New'
        verbose_name_plural = "New's"



class Blog(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextUploadingField()
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    # todo: create other things like blog page and linking and add moreeee things in data bases
    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse("app1:blogs-query", args=[str(self.id), self.name])

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Blog'


class NazarSanji(models.Model):
    """ model for nazar ha """
    comment = models.TextField()
    now = models.DateTimeField(auto_now_add=True)
    isRead = models.BooleanField(default=False)
