# -*- coding : utf-8 -*-
from django.utils import timezone 
from overwatch_crawler import get_patch_notes, get_test_patch_notes
import sys

import pytz
import os
import django 
# from django.conf import settings

# settings.configure(DEBUG=True)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patch_notes.settings")
django.setup()

from patch_app.models import PatchNotes, TestPatchNotes

patch_notes_list = get_patch_notes()
test_patch_notes = get_test_patch_notes()
#업데이트 날짜
patch_date = timezone.now()

#현재 내 DB에 있는 리스트 중 가장 최근의 리스트를 가져옴 
# (날짜별이 아니고, 그냥 첫번째 걸로 가져오는 것이기 때문에 날짜 별로 걸러내는 방법이 필요)
def find_objects():
	objects_all = list(PatchNotes.objects.all())

	if objects_all != []:
		last_title = objects_all[0].title
		return last_title
	else:	
		return objects_all



# def find_test_objects():
#     objects_all = list(TestPatchNotes.objects.all())

    # print(objects_all[0])

# find_test_objects()

def save_patches():
    find_objects = find_objects()
    # 정식 패치노트 DB 저장
    if find_objects == [] or find_objects != patch_notes_list[0][0]:
        for patch in patch_notes_list:
            PatchNotes(title=patch[0], subject=patch[1], text=patch[2] + patch[3], patch_date=patch_date).save()
        print("Patch Notes : Successfully saved.")

    else:
        print("Patch Notes : There's nothing to update.")

    #테스트 서버 패치노트 DB 저장
    if test_patch_notes == []:
        for test_patch in test_patch_notes:
            TestPatchNotes(title=test_patch[0], subject=test_patch[1], text=test_patch[3], patch_date=patch_date).save()
        print("Test patch Notes : Successfully saved")
    elif test_patch_notes != []:
        print("Test patch Notes : There's nothing to save.")

    # 현재 내 testpatchnotes 테이블의 리스트 중 가장 최근의 리스트를 가져옴
    # (날짜별이 아니고, 그냥 첫번째 걸로 가져오는 것이기 때문에 날짜 별로 걸러내는 방법이 필요)




