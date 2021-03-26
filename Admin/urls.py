from django.urls import path
from . import views 

app_name = 'Admin'
urlpatterns = [

   path('dashboard', views.DashboardView.as_view(), name="dashboard_view"),
]