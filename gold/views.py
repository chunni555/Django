from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return render(request,'index.html')

def browse(request):
    product_list = [
        {'id':1,'name':"Gold Bar",'price':25000000 },
        {'id':2,'name':"Necklace",'price':56000000 },
        {'id':3,'name':"Hand Chain",'price':18000000 },
        ]
    
    return render(request,'browse.html',{
        'product_list':product_list,
        })

def detail(request, id):
    product_list = [
        {'id':1,'name':"Gold Bar",'price':25000000 },
        {'id':2,'name':"Necklace",'price':56000000 },
        {'id':3,'name':"Hand Chain",'price':18000000 },
        ]
    for product in product_list:
        if id == product['id']: 
            return render(request,'detail.html',{
                'product_name':product['name'],
                'price':product['price'],
                })
    