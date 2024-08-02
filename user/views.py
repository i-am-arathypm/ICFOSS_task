import re
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            messages.info(request,'Invalid Credentials')
            return redirect('/')
        else:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/dashboard')
    messages.info(request,'Invalid credentials')            
    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password1']

        if User.objects.filter(email=email).exists():
            messages.info(request,'Email already exists')
            return redirect('/register')
        if User.objects.filter(username=username).exists():
            messages.info(request,'User exists')
            return redirect('/register')
        if (len(username) < 6):
            messages.error(request, "Username must be at least 6 characters long.")
            return redirect('/register')
        if not first_name.isalpha():
            messages.error(request, "First name must only contain alphabetic characters.")
            return redirect('/register')

        if not last_name.isalpha():
            messages.error(request, "Last name must only contain alphabetic characters.")
            return redirect('/register')
        else:
            if password != password2:
                messages.info(request,'Passwords not matching')
                return redirect('/register')
            
            if len(password) < 8:
                messages.error(request, "Password must be at least 8 characters long.")
                return redirect('/register')

            if not re.search(r'[A-Z]', password):
                messages.error(request, "Password must contain at least one uppercase letter.")
                return redirect('/register')

            if not re.search(r'[0-9]', password):
                messages.error(request, "Password must contain at least one number.")
                return redirect('/register')

            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                messages.error(request, "Password must contain at least one special character.")
                return redirect('/register')

            else:
                user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                messages.info(request,'Account created successfully')
                return redirect('/')
        
    return render(request,'register.html')


@login_required(login_url='/')
def dashboard(request):
    email=request.user.email

    return render(request,'dashboard.html')


@login_required(login_url='/')
def edit(request,b_id):
    if request.method =='POST':
        record = get_object_or_404(Bot, pk=b_id)
        name =  request.POST['name']
        content = request.POST['content']
        record.name = name
        record.content = content
        record.save()
        return redirect('/dashboard') 
    bot = Bot.objects.filter(id = b_id).first()
    return render(request,'edit.html',{'bot':bot})




def change_password(request):
    if request.method == 'POST':
        user = request.user
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        new_password2 = request.POST['new_password2']

        # Check if current password matches
        if not user.check_password(current_password):
            messages.error(request, 'Incorrect current password')
            return redirect('/password')

        # Check if new passwords match
        if new_password != new_password2:
            messages.error(request, 'New passwords do not match')
            return redirect('/password')

        # Change the password
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)  # Important for retaining the user's session
        messages.success(request, 'Password changed successfully')
        return redirect('/')

    return render(request, 'password.html')



@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('/')



