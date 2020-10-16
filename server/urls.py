from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('convert/', views.convert),
    path('seler/', views.seler),
]

urlpatterns = format_suffix_patterns(urlpatterns)
