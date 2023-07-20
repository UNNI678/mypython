
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import Movie_Form
# Create your views here.
def index(request):
    mv=movie.objects.all()
    context={
        'movie_list':mv
    }
    return render(request,"index.html",context)

def detail(request,movie_id):
    m=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'mo':m})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        mymo=movie(name=name,desc=desc,year=year,img=img)
        mymo.save()
    return render(request,'add.html')

def update(request,id):
    mov=movie.objects.get(id=id)
    form=Movie_Form(request.POST or None, request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'fo':form,'movie':mov})

def delete(request,id):
    if request.method=='POST':
        movi=movie.objects.get(id=id)
        movi.delete()
        return redirect('/')
    return render(request,'delete.html')


