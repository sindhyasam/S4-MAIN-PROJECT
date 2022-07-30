from django.shortcuts import render,redirect
from django .contrib.auth.models import User,auth
from devicesManage.models import  Device_data, Devices_list,Alert_data


def is_staff_logged(request):
    key = "staff_username"
    if key not in request.session:
        return 0
    else:
        return 1

def get_user_name(request):
    return request.session['staff_username']

def user(request):
    return render(request,"User/index.html")


def device_count(username):
    device_count =  0
    obj = Devices_list.objects.filter(assigned_to = username)
    device_count = len(obj)
    return device_count

def gas_latest_value(username):
    temp_list = []
    obj = Devices_list.objects.filter(assigned_to = username)

    try:
        for each in obj:
            dataObj = Device_data.objects.filter(mac_id = each.mac_id).order_by('-crnt_time')[:1]
            for each in dataObj:
                temp_list.append(each.gas_value)
    except Exception as e:
        print(e)

    return temp_list

def alert_count(username):
    obj = Devices_list.objects.filter(assigned_to = username)
    dids = [each.mac_id for each in obj]
    count= len(Alert_data.objects.filter(mac_id__in = dids))
    return count

def alert_obj(username):
    obj = Devices_list.objects.filter(assigned_to = username)
    dids = [each.mac_id for each in obj]
    aObj= Alert_data.objects.filter(mac_id__in = dids)
    return aObj


def data_obj(username):
    obj = Devices_list.objects.filter(assigned_to = username)
    dids = [each.mac_id for each in obj]
    dObj= Device_data.objects.filter(mac_id__in = dids)
    return dObj

def staffDashboard(request):
    username = get_user_name(request)

    context = {
        "d_count":device_count(username),
        "gas" : gas_latest_value(username),
        "alert":alert_count(username)
    }
    return render(request,"User/dashboard.html",context)


def viewalerts(request):
    username = get_user_name(request)
    context={
        "data":alert_obj(username),
    }
    return render(request,"User/alerts/viewalerts.html",context)

def view_readings(request):
    username = get_user_name(request)
    context={
        "data":data_obj(username),
    }
    return render(request,"User/alerts/viewreadings.html",context)


def staffListDevices(request):
        if(not is_staff_logged(request)):
            return redirect('login')
        try:
            deviceData = Devices_list.objects.filter(assigned_to = request.session['staff_username'])
        except:
            deviceData= Devices_list()
        
        return render(request,"User/device/list_device.html",{
            "deviceData":deviceData,
            })


def staffStatusDevices(request):
        if(not is_staff_logged(request)):
            return redirect('login')
        try:
            deviceData = Devices_list.objects.filter(assigned_to = request.session['staff_username'])
        except:
            deviceData= Devices_list()
        return render(request,"User/device/status_device.html",{
            "deviceData":deviceData,
            })


def logout(request):
    auth.logout(request)
    return redirect('/')


