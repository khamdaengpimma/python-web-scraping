from django.shortcuts import render
from django.http import HttpResponse
from devapp import scrap

def index(request):
    print(request.POST)
    return render(request,"index.html",{"items":scrap.menu(),'action':'/book'})
def books(request):
    if request.method =='POST':
        key = request.POST["key"]
        title =request.POST["title"]
        print(request.POST)
        return render(request,"category.html",{"items":scrap.category(key),'texth':title,'action':'/book1'})
    
    return render(request,"index.html",{"items":scrap.menu()})
    
def bookone(request):
    if request.method =='POST':
        key = request.POST["key"]
        title =request.POST["title"]
        return render(request,"book.html",{"items":scrap.bookone(key),'texth':title})
    return render(request,"index.html",{"items":scrap.menu()})

def code(request):
    return render(request,"code.html")
def sinhvien(request):
    return render(request,"sinhvien.html")
    