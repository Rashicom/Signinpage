from django.urls import path, include
from . import views

urlpatterns = [
    # login path
    path('', views.login, name="login"),
    # home path
    path('home/', views.homepage, name="homepage"),
    # logout path redirected to login
    path('logout/',views.logout, name="logout"),

]
