from django.urls import path
from django.conf.urls import include
from survey_app import views


urlpatterns = [    
    path('fill/', views.survey_details),
    path('results/', views.survey_result),
]
