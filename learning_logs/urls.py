from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,  name='index'),
    path('pg2', views.pg2, name='pg2'),
    path('pg3', views.pg3, name='pg3'),
    path('pg4', views.pg4, name='pg4'),
    path('topics', views.topics, name='topics'),
    path('topic/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic', views.new_topic, name='new_topic'),
]