from django.urls import path
from . import views

urlpatterns = [
#path('', views.top, name='top'),
#path('create', views.create, name='create'),
#path('login',views.login, name='login')
path('login/', views.loginView.as_view(), name="login"),
path('logout/', views.logoutView.as_view(), name="logout"),
path('top/', views.TopView.as_view(), name="top"),
path('userpage/', views.userpage, name='userpage'),
path('create/', views.create, name='usercreate'),




]
