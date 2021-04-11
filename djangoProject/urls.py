"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from djangoProject import views as UserView

from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addUser/',UserView.addUser,name="addUser"),
    path('update_info/',UserView.user_form_info,name="update_user_info"),
    path('<int:id>/',UserView.user_form_info,name='user_update'),
    path('delete/<int:id>',UserView.delete_user,name="delete_user"),
    path('user_list/',UserView.user_list,name="user_list"),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('teacher/',include('schoolSystemManagment.urls'))
]
