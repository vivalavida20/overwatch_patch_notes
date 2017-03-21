# -*- coding : utf-8 -*-
from django.shortcuts import render
from .models import PatchNotes, TestPatchNotes

# Create your views here.
def patch_notes(request):
	patch_notes = PatchNotes.objects.filter(title__contains='오버워치 패치 노트') + TestPatchNotes.objects.all()
	return render(request, 'patch_app/patch_notes.html', {'patch_notes':patch_notes})
