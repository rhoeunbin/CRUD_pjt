from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', 'content', 'movie_name', 'grade']
        labels = {
            'title':'리뷰 제목',
            'content':'리뷰 내용',
            'movie_name': '영화 제목',
            'grade':'영화 평점'
        }