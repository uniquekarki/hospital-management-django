from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import uuid
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request , 'home.html')

@login_required(login_url='/login')
def logout_attempt(request):
    if request.user.is_authenticated == True:
        logout(request)
        return render(request, 'logout.html')

def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        department = request.POST.get('department')

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            send_verification_email(email , auth_token)
            return redirect('/token')
        except Exception as e:
            print(e)
    
    return render(request, 'register.html')

def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("\n\n\n\nHERE!!!")

        user_obj = User.objects.filter(username = username).first()
        if not user_obj:
            messages.success(request,'User not found!')
            return redirect('/login')
        
        profile_obj = Profile.objects.filter(user = user_obj).first()

        if profile_obj.is_verified == False:
            messages.success(request,'User not verified!')
            return redirect('/login')
        
        user = authenticate(username = username, password = password)
        if not user:
            messages.success(request,'Improper credentials')
            return redirect('/login')
        
        login(request, user)
        return redirect('/')
    return render(request, 'login.html')

def success(request):
    return render(request, 'success.html')

def token_send(request):
    return render(request, 'token_send.html')

def error_page(request):
    return render(request, 'error.html')

def schedule_appointments(request):
    form = AppointmentsForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Your appointment has been scheduled!')
        return redirect('/schedule')

    context = {
        'form':form
    }
    return render(request, 'schedule.html', context)

def view_appointment(request):
    data = Appointments.objects.all()
    context = {
        'data':data
    }
    return render(request, 'appointment.html', context)

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your email has been verified!')
                return redirect('/login')
            
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request,'Your email has been verified!')
            return redirect('/login')
        else:
            return redirect('/error')

    except Exception as e:
        print(e)
        return redirect('/login')

def send_verification_email(email, token):
    subject = 'Your account needs to be verified'
    message = f'Paste this link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)