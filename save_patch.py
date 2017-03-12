from datetime import datetime
from overwatch_crawler import get_patch_notes
import sys
# python timezone library인 것으로 아는데 무슨 소용인지는 모름
import pytz
import os
import django 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patch_notes.settings")
django.setup()

from patch_app.models import PatchNotes

patch_notes_list = get_patch_notes()

#패치 노트의 내용을 db에 저장 

def find_objects():
	objects_all = list(PatchNotes.objects.all())

	if objects_all != []:
		last_title = objects_all[0].title
		return last_title
	else:
		return objects_all

find_objects = find_objects()
print(find_objects)

if find_objects == [] or find_objects != patch_notes_list[0][0]:
	
	for patch in patch_notes_list:
		patch_date = datetime.now()
		PatchNotes(title=patch[0], subject=patch[1], text=patch[2] + patch[3], patch_date=patch_date).save()
		print("Successfully saved.")

else:
	print("There's nothing to update.")	
