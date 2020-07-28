from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify

User=settings.AUTH_USER_MODEL
# Create your models here

class Post(models.Model):
    user=models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=120,unique=True)
    content = models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='image/',blank=True,null=True)
    publish_date= models.DateTimeField(auto_now=False,auto_now_add=False,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    

    def get_absolute_url(self):
        return f"{self.id}"


    def get_edit_url(self):
        return f"/blogger/update/{self.id}"


    def get_delete_url(self):
        return f"/blogger/delete/{self.id}"
