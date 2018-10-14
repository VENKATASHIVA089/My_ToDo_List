from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import List,User
from .forms import ListForm,UserForm,CreateForm
from django import forms
from django.contrib import messages
active=[]
def home(request,id=None):
    if request.method == 'POST':
        if id not in active:
            messages.success(request,('Session expired Please login'))
            return redirect('login')
        #print(active)
        user = User.objects.get(pk=id)
        form=ListForm(request.POST or None)
        if 'logout' in form.data:
            active.remove(id)
            messages.success(request,('Succesfully Logged Out'))
            return redirect('login')
        if form.is_valid():
            item=form.data['item']
            user.list_set.create(item=item.title(),completed=False)
            #all_items=user.list_set.all()
            #print(all_items)
            messages.success(request,('Item Has Been Added To List'))
            return redirect('home',user.id)
    else:
        if id not in active:
            messages.success(request,('Session expired Please login'))
            return redirect('login')
        user=User.objects.get(pk=id)
        all_items=user.list_set.all()
        #print(all_items)
        return render(request,'home.html',{'user':user,'all_items':all_items})
def delete(request,list_id):
    if request.method == 'POST':
        form=forms.Form(request.POST or None)
        item = List.objects.get(pk=list_id)
        userid=item.user.id
        if 'yes' in form.data:
            item.delete()
            messages.success(request,('Succesfully deleted'))
            return redirect('home',userid)
        else :
            return redirect('home',userid)
    else:
        item=List.objects.get(pk=list_id)
        return render(request,'delete.html',{'item':item})
def cross_off(request,list_id):
    item=List.objects.get(pk=list_id)
    item.completed=True
    item.save()
    return redirect('home',item.user.id)
def uncross(request,list_id):
    item=List.objects.get(pk=list_id)
    item.completed=False
    item.save()
    return redirect('home',item.user.id)
def edit(request,list_id):
    if request.method == 'POST':
        item=List.objects.get(pk=list_id)
        form=ListForm(request.POST or None)
        item.item=form.data['item'].title()
        item.save()
        print(item.user.id)
        return redirect('home',item.user.id)
    else:
        item=List.objects.get(pk=list_id)
        return render(request,'edit.html',{'item':item})
def login(request):
    if request.method =='POST':
        form=UserForm(request.POST or None)
        email=form.data['email']
        try:
            user=User.objects.get(email=email)
        except:
            user=None
        if user:
            password=form.data['password']
            if user.password == password:
                #all_items=user.list_set.all()
                active.append(user.pk)
                print(active)
                return redirect('home',id=user.pk)
            else:
                messages.success(request,('Password wrong'))
                return redirect('login')
        else:
            messages.success(request,('Not a member please register'))
            return redirect('login')
    else:
        #print(active)
        if len(active) > 0:
            return redirect('home', active[0])
        return render(request,'login.html',{})
def create(request):
    if request.method=='POST':
        form=CreateForm(request.POST or None)
        email=form.data['email']
        try:
            user=User.objects.get(email=email)
        except:
            user=None
        if user==None:
            form.save()
            messages.success(request,('User created- please login'))
            return redirect('login')
        else:
            messages.success(request,('Email ID allready exist : Please Login'))
            return redirect('login')
    else:
        return render(request,'create.html',{})



