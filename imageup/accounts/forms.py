from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth import get_user_model
#회원정보수정
from django.contrib.auth.forms import UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields =  ['username', 'email', 'password1', 'password2']

#회원정보수정
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')