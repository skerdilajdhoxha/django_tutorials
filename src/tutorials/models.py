from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Category(models.Model):
    title = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Category"

    def get_absolute_url(self):
        # return "/blog/%s" %(self.id)
        return reverse("category_detail", kwargs={"slug": self.slug})


CHOICES = (
    ('beginner', 'beginner'),
    ('intermediate', 'intermediate'),
    ('advanced', 'advanced'),
)


class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    photo = models.FileField(max_length=200, upload_to='media_cdn/', blank=True)
    slug = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=20, choices=CHOICES, default='beginner')
    categories = models.ForeignKey(Category)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['author']

    def get_absolute_url(self):
        # return "/blog/%s" %(self.id)
        return reverse("tutorial_detail", kwargs={"slug": self.slug})


class TutorialDetail(models.Model):
    name = models.CharField(max_length=100)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)    # , related_name='tut_detail'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Video(models.Model):
    title = models.CharField(max_length=200)
    youtube_id = models.CharField(max_length=500, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #slug = models.CharField(max_length=200, unique=True)
    tutorialdetail = models.OneToOneField(TutorialDetail, on_delete=models.CASCADE, primary_key=True)

    def __unicode__(self):
        return self.title





