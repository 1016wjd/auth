from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass 

    # 자동생성
    # article_set = 
    # comment_set = 