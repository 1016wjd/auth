from django.db import models
from accounts.models import User
from django.conf import settings #settings.py를 가져옴 / 맨 마지막 즐 변수화를 가져오기 위해
from django.contrib.auth import get_user_model
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    # comment_set = 장고가 자동으로 추가해주는 칼럼

    # 유저모델을 참조하는 경우
    # 방법1 (권장하지 않음 > 유지보수 어려움)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 방법2 (권장)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # 방법3 (권장)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    


class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 1:N 관계설정
    # article_id = 장고가 자동으로 저장해주는 칼럼
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
