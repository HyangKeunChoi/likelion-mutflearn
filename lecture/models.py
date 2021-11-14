from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Lecture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField() # 대용량의 타입의 필드
    image = models.ImageField(upload_to='lecture', null=True)
    created_at = models.DateTimeField() # 날짜 타입의 필드
    liked_lectures = models.ManyToManyField(User, related_name='liked_lectures')
    title = models.CharField(max_length=200, null=True)
    video_key = models.CharField(max_length=12, null=True)

    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.body}'
        else:
            return f'{self.body}'
