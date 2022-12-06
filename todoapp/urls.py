#Nava_217530216-Segura_214804382

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('login/',views.loginpage, name= 'login'),
    path('logout/', views.LogoutView, name='logout'),
    path('delete-task/<str:name>/', views.DeleteTask, name='delete'),
    path('update/<str:name>/', views.Update, name='update'),
]