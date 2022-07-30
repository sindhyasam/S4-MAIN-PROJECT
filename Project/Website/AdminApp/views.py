from django.shortcuts import render,redirect
from django .contrib.auth.models import User,auth
from devicesManage.models import Device_data, Devices_list
from django .contrib import messages
from django.db.models import Q


def get_device_count():
    # Active,Deactive,Total
    count_list = [] 
    try:
        count_list.append(len(Devices_list.objects.filter(status='ON')))
        count_list.append(len(Devices_list.objects.filter(status='OFF')))
        count_list.append(len(Devices_list.objects.all()))

    except:
         count_list = [0,0,0]
    return count_list 

def get_users_count():
    # Active,Deactive,Total
    count_list = [] 
    try:
        count_list.append(len(User.objects.filter(is_active=1)))
        count_list.append(len(User.objects.filter(is_active=0)))
        count_list.append(len(User.objects.all()))
    except:
         count_list = [0,0,0]
    return count_list 


def admin(request):

    return render(request,"Admin/index.html")

def dashboard(request):
    return render(request,"Admin/dashboard.html",{
        "deviceCount":get_device_count()[2],
        "userCount":get_users_count()[2],
        #"alertCount":get_alerts_count()[2],
    })

def logout(request):
    auth.logout(request)
    return redirect('/')

def devices(request):
    userData = User.objects.filter(~Q(username = 'admin'))
    return render(request,"Admin/device/add_device.html",{"allusers":userData,})


def add_device_manually(request):
        if request.method == "POST":
                mac_id  = request.POST['mac_id_m']
                assigned_to = request.POST['user_m']
                status = request.POST['status_m']


                if(assigned_to == 'Select User'):
                        messages.info(request,'Select User First !')
                        return redirect(devices)
                        
                if(status == 'Select Status'):
                        messages.info(request,'Select Status !')
                        return redirect(devices)
                        

                data = Devices_list(
                        mac_id=mac_id,
                        assigned_to=assigned_to,
                        status=status,
                )

                data.save()
                messages.info(request,'New Device Succesfully Added')
                return redirect(devices)




def assigndevices(request):
        deviceData = Devices_list.objects.all()
        userData = User.objects.filter(~Q(username = 'admin'))
        return render(request,"Admin/device/assign_device.html",{
            "deviceData":deviceData,
            "userData":userData,
            })

def assign_device_manually(request):
        if request.method == "POST":
                mac_id  = request.POST['mac_id']
                assigned_to = request.POST['username']


                if(assigned_to == 'Select User'):
                        messages.info(request,'Select User First !')
                        return redirect(devices)
                        
                        
                data = Devices_list(
                        mac_id=mac_id,
                        assigned_to=assigned_to,
                )

                data.save()
                messages.info(request,'New Device Succesfully Added')
                return redirect(assigndevices)


def assignDevicesList(request):
        deviceData = Devices_list.objects.all()
        return render(request,"Admin/device/list_assigned_device.html",{
            "deviceData":deviceData,
            })

def delete_assign(request):
    if request.method == "POST":
        id  = request.POST['id']
        try:
            deviceObj = Devices_list.objects.get(id = id)
            deviceObj.assigned_to = ""
            deviceObj.save()
            messages.success(request, "The Device assign is removed")            

        except User.DoesNotExist:
            messages.error(request, "Something went wrong")
    return redirect('assignDevicesList')



def listDevices(request):
        deviceData = Devices_list.objects.all()
        return render(request,"Admin/device/list_device.html",{
            "deviceData":deviceData,
            })

def removeDevices(request):
        deviceData = Devices_list.objects.all()
        return render(request,"Admin/device/remove_device.html",{
            "deviceData":deviceData,
            })

def delete_device(request):
    if request.method == "POST":
        id  = request.POST['id']
        try:
            deviceObj = Devices_list.objects.get(id = id)
            deviceObj.delete()
            messages.success(request, "The Device is removed")            

        except User.DoesNotExist:
            messages.error(request, "Something went wrong")
    return redirect('removeDevices')



def list_user(request):
    users_data_list = list(User.objects.values())
    for i in range(len(users_data_list)):
        del users_data_list[i]['password']
        del users_data_list[i]['last_login']
        del users_data_list[i]['is_superuser']
        del users_data_list[i]['is_staff']
        del users_data_list[i]['date_joined']
        del users_data_list[i]['is_active']
        users_data_list[i]=users_data_list[i]
 
    context = {
                'allUsersData': users_data_list,
                }

    return render(request,"Admin/users/list_user.html",context)


def status_user(request):
    users_data_list = list(User.objects.values())
    for i in range(len(users_data_list)):
        del users_data_list[i]['password']
        del users_data_list[i]['is_superuser']
        del users_data_list[i]['is_staff']
        users_data_list[i]=users_data_list[i]
 
    context = {
                'allUsersData': users_data_list,
                }

    return render(request,"Admin/users/status_user.html",context)

    
def remove_user(request):
    users_data_list = list(User.objects.values())
    for i in range(len(users_data_list)):
        del users_data_list[i]['password']
        del users_data_list[i]['last_login']
        del users_data_list[i]['is_superuser']
        del users_data_list[i]['is_staff']
        del users_data_list[i]['date_joined']
        del users_data_list[i]['is_active']
        users_data_list[i]=users_data_list[i]
 
    context = {
                'allUsersData': users_data_list,
                }

    return render(request,"Admin/users/remove_user.html",context)
    

def delete_user(request):
    if request.method == "POST":
        id  = request.POST['id']
        try:
            user = User.objects.get(id = id)
            user.delete()
            print(user.username)
            messages.success(request, "The user is deleted")            

        except User.DoesNotExist:
            messages.error(request, "User doesnot exist")    
        
    return redirect('remove_user')