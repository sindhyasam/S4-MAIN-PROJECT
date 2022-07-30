from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.user,name="user"),  
    path('staffDashboard',views.staffDashboard,name="staffdashboard"),
    path('staffListDevices',views.staffListDevices,name="staffListDevices"),
    path('staffStatusDevices',views.staffStatusDevices,name="staffStatusDevices"), 
    path('viewalerts',views.viewalerts,name="viewalerts"),
    path('view_readings',views.view_readings,name="view_readings"),
    path('logout/', views.logout,name="logout"),
]

