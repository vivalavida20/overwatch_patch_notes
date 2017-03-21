# -*- coding : utf-8 -*-
from django.shortcuts import render
from .models import PatchNotes, TestPatchNotes

# Create your views here.
# heroku update test
def patch_notes(request):
	patch_notes = PatchNotes.objects.filter(title__contains='오버워치 패치 노트')
	test_patch_notes = TestPatchNotes.objects.all()
	context = {'patch_notes':patch_notes, 'test_patch_notes':test_patch_notes}
	return render(request, 'patch_app/patch_notes.html', context=context)
