from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    author = models.ForeignKey(User , on_delete=models.SET_NULL, null=True , blank=True , related_name='articles')
    title = models.CharField(max_length=80)
    category = models.ManyToManyField(Category , related_name="articles")
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(blank=True , unique=True)
    objects = models.Manager()

    class Meta:
        ordering = ('-updated','-created')


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})




    def __str__(self):
        return f"{self.title} - {self.body[:30]}"




class Comment(models.Model):
    article = models.ForeignKey(Article , on_delete=models.CASCADE , related_name='comments')
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='comments')
    parent = models.ForeignKey('self' , on_delete=models.CASCADE ,null= True , blank=True ,  related_name='replies')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]





class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True , null=True)
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title