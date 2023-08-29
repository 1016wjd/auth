from django import forms
from .models import Article

# 모델을 제공하면 알아서 맞는 form 제공
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('title', 'content', )
        # exclude = ('user', )