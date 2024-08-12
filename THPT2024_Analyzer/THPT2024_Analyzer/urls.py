"""
URL configuration for THPT2024_Analyzer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from kafka_app.views import send_score, save_student_scores
from Analyzer_score.views import get_all_scores, index, get_median_score

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/send-score/', send_score, name='send_score'),
    path('api/save-scores/', save_student_scores, name='save_student_scores'),
    path('api/all-scores/', get_all_scores, name='get_all_scores'),
    path('', index, name ='index'),
    path('api/median_score/', get_median_score, name ='get_median_score')
]
