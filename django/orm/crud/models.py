from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    
    
# 정리 
# class Post : Django - Model, DB - Table
# post = Post() : Django - Instance or Object , DB - Record or Row
# title : Django - Field , DB - Column

