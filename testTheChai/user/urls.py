from django.urls import path
from . import views

urlpatterns = [
    path('', views.userList, name='userList'),
    path('<int:user_id>/', views.getAnUser, name='userDetails')
]