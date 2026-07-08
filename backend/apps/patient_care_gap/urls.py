from django.urls import path

from . import views

urlpatterns = [
    path('view_patient/', views.patient_list, name='patient_list'),
    path('create_patient/', views.patient_create, name='patient_create'),
    path('view_care_gaps/', views.care_gap_list, name='care_gap_list'),
    path('create_care_gap/', views.care_gap_create, name='care_gap_create'),
]
