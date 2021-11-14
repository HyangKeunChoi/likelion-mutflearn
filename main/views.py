from lecture.models import Lecture
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
       
   lectures = Lecture.objects.all().order_by('-created_at')[:4]

   context = {'lectures' : lectures}
   return render(request, 'main/main.html', context) 