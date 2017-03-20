# -*- coding : utf-8 -*-
from django.db import models
from django.utils import timezone
# Create your models here.
class PatchNotes(models.Model):
	title = models.CharField(max_length=200)
	subject = models.CharField(max_length=100) 
	text = models.TextField()
	patch_date = models.DateTimeField()

class TestPatchNotes(models.Model):
	title = models.CharField(max_length=200)
	subject = models.CharField(max_length=100)
	text = models.TextField()
	patch_date = models.DateTimeField()
