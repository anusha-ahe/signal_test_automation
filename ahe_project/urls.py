from django.contrib import admin
from django.urls import path, include
from django.urls import path
from test_signal.views import simulation_page, upload_folder
from test_signal import views

urlpatterns = [
    path('sim/', views.simulation_page, name='simulation_page'),
    path('upload_folder/', upload_folder, name='upload_folder'),
]
