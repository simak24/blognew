from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
import uuid

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    blog_title=models.CharField(max_length=264,verbose_name='Put a title' )
    slug=models.SlugField(max_length=264,unique=True)
    blog_content=models.TextField(verbose_name='What is in your mind')
    blog_image=models.ImageField(upload_to='blog_pics',verbose_name='Image')
    publish_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-publish_date', )

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.blog_title

    # def save():
    #     self.slug=slugify(self.blog_title+ '-' + str(uuid.uuid4()))
    #     super(Blog,self).save()


class Comment(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment_blog')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user' )
    comment=models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-comment_date',)

    def __str__(self):
        return self.comment

class Likes(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='liked_blog')
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='liked_user')

    def __str__(self):
        return self.user + "likes" + self.blog
