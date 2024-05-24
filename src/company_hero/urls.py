from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/token/", views.obtain_auth_token),
]
