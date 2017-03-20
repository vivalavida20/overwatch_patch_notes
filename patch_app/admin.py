from django.contrib import admin
from patch_app.models import PatchNotes, TestPatchNotes
# Register your models here.

admin.site.register(PatchNotes)
admin.site.register(TestPatchNotes)