from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.admin,name="admin"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('logout/', views.logout,name="logout"),

    path('devices',views.devices,name="devices"),
    path('add_device_manually',views.add_device_manually,name="add_device_manually"),
    path('assign_device_manually',views.assign_device_manually,name="assign_device_manually"),
    path('assigndevices',views.assigndevices,name="assigndevices"), 
    path('assignDevicesList',views.assignDevicesList,name="assignDevicesList"),
    path('delete_assign',views.delete_assign,name="delete_assign"),
    path('listDevices',views.listDevices,name="listDevices"),
    path('removeDevices',views.removeDevices,name="removeDevices"),
    path('delete_device',views.delete_device,name="delete_device"), 
    path('list_user',views.list_user,name="list_user"),
    path('remove_user',views.remove_user,name="remove_user"),
    path('delete_user',views.delete_user,name="delete_user"),
    path('status_user',views.status_user,name="status_user"), 
]
