from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
# 默认charfield不能为空，添加blank参数使得可以为空
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.title
    
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
        
    class Meta:
        ordering = ['-created_time']
