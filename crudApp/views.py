from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Contacts
from django.contrib.auth.models import User, auth
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    context={}
    if request.method=="POST":
        nm=request.POST["uname"]
        p=request.POST["pass"]
        cp=request.POST["cpass"]
        
        print(nm,p,cp)
        if nm=='' or cp=="":
            context["errmsg"]="Fields cannot be empty"
            return render(request,"register.html", context)
        
        elif p!=cp:
            context["errmsg"]="Password and cpassword did not match"
            return render(request,"register.html",context)

        elif User.objects.get(username=nm):
            context["errmsg"]="Username has already been registered. Try another username"
            return render(request,"register.html",context)

        else:
            u=User.objects.create(username=nm,email=nm)
            u.set_password(p) 
            u.save()
            context["success"]="Registration successfull!!"
            return render(request,"register.html",context)   
    return render(request,"register.html")


def ulogin(request):
    context={}
    if request.method=="POST":
        un=request.POST["uname"]
        p=request.POST["password"]
        print(un,p)

        if un=="" or p=="" :
            context["errmsg"]="Fields cannot be empty"
            return render(request,"login.html", context)
        else:
            u=auth.authenticate(username=un,password=p)
            print(u)
            if u is not None:
                auth.login(request, u)
                return redirect('dashboard')
            else:
                context["errmsg"]="Invalid username or password"
                return render(request,"login.html",context)
            
    return render(request,"login.html")

@login_required(login_url='login')
def ulogout(request):
    auth.logout(request)
    return redirect('/login')

def form(request) :
    print("The executed method :", request.method)
    if(request.method == 'POST'):
        n = request.POST['name']
        a = request.POST['age']
        m = request.POST['mobile']
        e = request.POST['email']
        msg = request.POST['message']
        # print(n, a, m, e, msg)
        f1 = Contacts.objects.create(name = n, age = a, mobile = m, email = e, message = msg) 
        f1.save()
    return render(request, 'form.html')

@login_required(login_url = 'login')
def dashboard(request):
    data = Contacts.objects.all()
    #for i in f2 :
    #    print(i.name, i.age, i.mobile, i.email, i.message)

    #fetching data and saving in a dictionary
    # data = serializers.serialize('python', f2)

    context = {
        'data' : data,
    }

    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def delete(request, rid) :
    data = Contacts.objects.all()
    context = {
        'data' : data,
    }
    el = Contacts.objects.filter(id = rid)
    el.delete()
    return render(request, 'dashboard.html', context)
    
@login_required(login_url='login')
def edit(request, uid) :
    if(request.method == 'GET') :
        data = Contacts.objects.filter(id = uid)
        context = {}
        context['data'] = data
        return render(request, 'edit.html', context)
    elif(request.method == 'POST') :
        n = request.POST['name']
        a = request.POST['age']
        m = request.POST['mobile']
        e = request.POST['email']
        msg = request.POST['message']
        contact = get_object_or_404(Contacts, id=uid)

        # Updating the contact
        contact.name = n
        contact.age = a
        contact.mobile = m
        contact.email = e
        contact.message = msg
        # f1 = Contacts.objects.get(name = n, age = a, mobile = m, email = e, message = msg)
        # f1.save()
        contact.save()
        return redirect('dashboard')