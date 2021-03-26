from django.urls import path
from . import views 

app_name = 'User'
urlpatterns = [

   path('dashboard', views.DashboardView.as_view(), name="dashboard_view"),
   path('landing', views.LandingPageView.as_view(), name="landing_view"),
   path('event', views.EventView.as_view(), name="event_view"),
   path('notification', views.NotificationView.as_view(), name="notification_view")
]