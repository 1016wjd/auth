from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta: # 우리가 가져온 데이터를 사용하기 위함!
        model = User
        # fields = '__all__'
        fields = ('username', )


class CustomAuthenticationForm(AuthenticationForm):
    pass
