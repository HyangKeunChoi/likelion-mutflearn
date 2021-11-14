from django.contrib import admin
from .models import Lecture
from embed_video.admin import AdminVideoMixin


# Register your models here.

admin.site.register(Lecture)