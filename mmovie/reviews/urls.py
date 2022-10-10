from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('info/<int:pk>', views.info, name='info'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]