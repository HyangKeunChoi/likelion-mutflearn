from django.http.request import QueryDict
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lecture
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import requests
# Create your views here.

def index(request):

    lectures = Lecture.objects.all().order_by('-created_at')

    context ={
        'lectures' : lectures,
    }

    return render(request, 'lecture/index.html', context)

def detail(request, lecture_id):

    lecture = Lecture.objects.get(id=lecture_id)
    context = {'lecture' : lecture}

    return render(request, 'lecture/detail.html', context)

@login_required
def new(request):

    return render(request, 'lecture/new.html')

@login_required
def create(request):

    user = request.user
    title = request.POST.get('title')
    body = request.POST.get('body')
    image = request.FILES.get('image')
    video_key = request.POST['video_key']

    lecture = Lecture(title=title, user=user, body=body, image=image, created_at=timezone.now(), video_key=video_key)
    lecture.save()

    return redirect('lecture:detail', lecture_id=lecture.id)

@login_required
def edit(request, lecture_id):
   
    try:
        lecture = Lecture.objects.get(id=lecture_id, user=request.user)
    except Lecture.DoesNotExist:
        return redirect('lecture:index')

    context = {'lecture' : lecture}

    return render(request, 'lecture/edit.html', context)

@login_required
def update(request, lecture_id):
    
    try:
        lecture = Lecture.objects.get(id=lecture_id, user=request.user)
    except Lecture.DoesNotExist:
        return redirect('lecture:index')

    lecture.title = request.POST.get('title')
    lecture.body = request.POST.get('body')
    image = request.FILES.get('image')
    
    if image: # image가 none이 아닌경우
        lecture.image = image

    lecture.save()

    context = {'lecture' : lecture}

    return redirect('lecture:detail', lecture_id=lecture.id)  

@login_required     
def delete(request, lecture_id):

    try:
        lecture = Lecture.objects.get(id=lecture_id, user=request.user)
    except Lecture.DoesNotExist:
        return redirect('lecture:index')

    lecture.delete()
    
    return redirect('lecture:index')

@login_required
def like(request, lecture_id):
    try:
        lecture = Lecture.objects.get(id=lecture_id)

        if request.user in lecture.liked_lectures.all():
            lecture.liked_lectures.remove(request.user)
        else:
            lecture.liked_lectures.add(request.user)
            
        return redirect('lecture:detail', lecture_id=lecture.id)
    
    except Lecture.DoesNotExist:
        pass 
    
    return redirect('lecture:index')