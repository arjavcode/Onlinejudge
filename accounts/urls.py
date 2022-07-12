from django.urls import path
from . import views
from judge import views as api2

app_name = 'accounts'
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='loginuser'),
    path('logout/', views.logoutUser, name='logout'),
    path('', api2.problems  , name='problems'),
] 
