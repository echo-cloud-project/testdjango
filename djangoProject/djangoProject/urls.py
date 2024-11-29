"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from webapp.views import index, elements, generic, login_view, signup_view, login_process, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('elements/', elements, name='elements'),
    path('generic/', generic, name='generic'),
    path('login/', login_view, name='login'),  # 로그인 페이지 URL 추가
    path('login_process/', login_process, name='login_process'),  # 추가
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),  # 로그인 페이지 URL 추가
]