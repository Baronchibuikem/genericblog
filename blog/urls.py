from django.urls import path
from . import views
from .feeds import LatestPostFeed

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('feeds/', LatestPostFeed(), name='post_feed'),
    path('<category_slug>/', views.post_list, name='post_list_by_category'),
    path(r'<int:year>/<int:month>/<int:day>/' r'<str:post>/', views.post_detail, name='post_detail')
]