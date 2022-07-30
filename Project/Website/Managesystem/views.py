from django.shortcuts import render,redirect
from django .contrib.auth.models import User,auth
from django .contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from devicesManage.models import Device_data,Devices_list,Alert_data

from django.core.mail import send_mail
from django.conf import settings

def send_emails(subject,user,message,toemail):
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [toemail, ]
    send_mail( subject, message, "jobinjofficial@yahoo.com", recipient_list )
# jobinjofficial@yahoo.com


# Create your views here.
def home(request):
    return render(request,"Home/index.html")

def about(request):
    return render(request,"Home/about.html")

def login(request):
    return render(request,"Home/login.html")

def register(request):
    return render(request,"Home/register.html")
def contact(request):
    return render(request,"Home/contact.html")
def services(request):
    return render(request,"Home/services.html")



def login_user(request):
    if request.method == "POST":
        username    = request.POST['user']
        password    = request.POST['pass']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            userObj = User.objects.all().get(username=username)
            if(userObj.is_superuser):
                request.session['username'] = username
                auth.login(request,user)
                return redirect('admin')
            else:
                request.session['staff_username'] = username
                auth.login(request,user)
                return redirect('user')
        else:
            messages.info(request,'Incorrect Login Credentials... Try again...!')
            
            

    return redirect('home')

def register_user(request):
    if request.method == "POST":
        first_name  = request.POST['fname']
        last_name   = request.POST['lname']
        username    = request.POST['user']
        password1   = request.POST['pass']
        email       = request.POST['email']

        if(password1 == password1):
            if(User.objects.filter(username=username).exists()):
                messages.info(request,'Username already taken!')
                return redirect('home')
            elif(User.objects.filter(email=email).exists()):
                messages.info(request,'Email already taken!')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'Succesfully created your account...')
                return redirect('login_user')
        else:
            messages.info(request,'Passwords not matching...')
            return redirect('register')
    else:
        return render(request,"Home/index.html") 

import json

@csrf_exempt
def readings(request):
    if request.method == "POST":
        json_data = json.loads(request.body) # request.raw_post_data w/ Django < 1.4
        try:
            gas_value = json_data['gas_value']
            device_id = json_data['device_id']
        except KeyError:
            HttpResponseServerError("Malformed data!")
    
        #gas_value  = request.POST['gas_value']
        #device_id  = request.POST['device_id']

        obj = Device_data()
        obj.mac_id = device_id
        obj.gas_value = gas_value

        obj.save()

        print(obj.id) # db id

        print(gas_value)
        print(device_id)


        # alerts email send here  .............................
        # get user details
        user = "User"
        email = ""
        try:
            dObj = Devices_list.objects.get(id=device_id)
            uObj = User.objects.get(username=dObj.assigned_to)
            user = uObj.username
            email = uObj.email 
            print(user)
        except Exception as e:
            print(e)

        toemail = email
        threshold = 200000000
        subject = "Gas Leakage Alert!"
        message = "Alert from gas leakage system \n Gas is detected......"
        if int(gas_value) > threshold:
            
            print("email sent")

            alertObj = Alert_data()
            alertObj.mac_id = device_id
            alertObj.gas_value = gas_value
            alertObj.save() 

            send_emails(subject,user,message,toemail)

        return HttpResponse("Data received successfully")