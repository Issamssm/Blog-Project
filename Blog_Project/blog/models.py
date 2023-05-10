from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

STATUS_CHOICES = (
    (("programming"), ("programming")),
    (("Ethical Hacking"), ("Ethical Hacking")),
    (("Marketing"), ("Marketing")),
    (("Another"), ("Another")),
)
class Post(models.Model):
    title = models.CharField(max_length=100)
    title1 = models.CharField(max_length=100, null=True)
    title2 = models.CharField(max_length=100, null=True)
    content = models.TextField()
    content2 = models.TextField(null=True)
    post_date = models.DateTimeField(default=timezone.now)
    post_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categry = models.CharField(max_length=50 ,null=True, choices=STATUS_CHOICES, default='Another')
    image = models.ImageField(default='default_post.png', upload_to='post_pics')
    image2 = models.ImageField(default='', null=True, upload_to='post_pics2')
    
    def __str__(self):
        return f'{self.title} in {self.categry}'
    
    def  get_absolute_url(self):
        # return f'/detail/{self.pk}'
        return reverse('detaile', args=[self.pk])
    
    class Meta:
        ordering = ('-post_date', )
        
        
        
class CommentSysteme(models.Model):
    body = models.TextField(null=True)
    coment_date = models.DateTimeField(default = timezone.now)
    name = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,null=True, on_delete=models.CASCADE, related_name='comment')
    
    
    def __str__(self):
        return f'{self.name} commented on {self.post}'
    
    class Meta:
        ordering = ('-coment_date', )
        
        
        
        
        
        

    
