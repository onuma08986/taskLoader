"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import SignUp
from accounts import views

urlpatterns = [
    # システム認証機能
    path("admin/", admin.site.urls),
    # トップ画面
    path("", views.top, name="top"),
    # 汎用画面
    path("", include("django.contrib.auth.urls")),
    # ユーザ登録画面
    path("signup/", SignUp.as_view(), name="signup"),
    # メイン機能
    # path('main', include('main.urls')),
    # RESTAPI機能
    path("rest/", include("apis.urls")),
]
