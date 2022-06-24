from django.db import models

# Create your models here.
from django.db import models
from email import message
from statistics import mode
from django.db import models
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from froala_editor.fields import FroalaField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Publish'),
    )
    SECTION = (
        ('Home', 'Home'),
        ('featured', 'featured'),
        ('Recent', 'Recent'),
        ('Frettir', 'Frettir'),
    )

    fetured_image = models.ImageField(upload_to='Images', blank=True)
    alt_tag = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50, blank=True)
    # author_image = models.ImageField(upload_to='Images', blank=True)
    # author_content = models.CharField(max_length=500, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    content = FroalaField()
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)
    meta_title = models.CharField(max_length=65)
    meta_descripations = models.CharField(max_length=150)
    meta_keywords = models.CharField(max_length=65)
    status = models.CharField(choices=STATUS, max_length=100)
    section = models.CharField(choices=SECTION, max_length=100)

    def __str__(self):
        return self.title


def Create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return Create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = Create_slug(instance)


pre_save.connect(pre_save_post_reciver, Post)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Keypoints(models.Model):
    key_title = models.CharField(max_length=100)

    def __str__(self):
        return self.key_title


# Skodun model, which appears in the admin panel for the users with permission
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    #file_pdf = models.FileField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    # def get_default(self):
    #     if self.myfile:
    #         return self.myfile
    #     else:
    #         return settings.MEDIA_ROOT + '/Images/IGINTERNATIONAL22-02_1.jpg'

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    Sno = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.fullname
