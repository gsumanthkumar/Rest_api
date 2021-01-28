from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('tasklist',views.taskList,name='taskList'),
    path('taskpost',views.taskpost,name='taskpost'),
    path('taskdetail/<str:pk>/',views.taskdetail,name='taskdetail'),
    path('taskedit/<str:pk>/',views.taskedit,name='taskedit'),
    path('taskdelete/<str:pk>/',views.taskdelete,name='taskdelete')
]