from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Contacts
from django.core import serializers

# Create your views here.
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

def delete(request, rid) :
    data = Contacts.objects.all()
    context = {
        'data' : data,
    }
    el = Contacts.objects.filter(id = rid)
    el.delete()
    return render(request, 'dashboard.html', context)
    

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