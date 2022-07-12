from django.urls import path
from . import views
from judge import views as api1

app_name = 'accounts'
urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', api1.problems  , name='problems'),
] 
