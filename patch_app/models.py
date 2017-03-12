from django.db import models
from django.utils import timezone
# Create your models here.
class PatchNotes(models.Model):
	title = models.CharField(max_length=200) # 오버워치 패치노트 타이틀 
	subject = models.CharField(max_length=100) # 오버워치 패치노트 서브주제 (ex)일반, 영웅업데이트, 패치 하이라이트 등..)
	text = models.TextField()
	patch_date = models.DateTimeField()