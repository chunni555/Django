from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request,'user.html')

def info(request):
       
    info_list ={
        'name':"Myat Thiri Khant",
        'address':"Kan Road,Hlaing Township",
        'phone_no':"0956789"
    }
    return render(request,'user_info.html',{
        'name':info_list['name'],
        'address':info_list['address'],
        'phone_no':info_list['phone_no']
        })

