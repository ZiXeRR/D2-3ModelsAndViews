from django.urls import path
from . import views
from .views import detail




urlpatterns = [
    path('news_list/', views.news_list, name='default'),
    path('new/<str:slug>', detail, name='detail')
    #path('authors/', views.AuthorsPage()),
    path('post/<int:pk>/', views.new),

] 