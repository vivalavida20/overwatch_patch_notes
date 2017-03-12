import os
import sys
import requests
from bs4 import BeautifulSoup
# from lxml import html


def get_patch_notes():

	# requests로 오버워치 패치 노트 내용을 가져온다. 
	response = requests.get('https://playoverwatch.com/ko-kr/game/patch-notes/pc/')

	html = response.text
	soup = BeautifulSoup(html, 'html.parser')
	patch_notes_body = soup.select('.patch-notes-body')


	#빈 리스트에 날짜별로 patch notes 쌓기 
	patch_notes_list = []

	# patch_notes_body를 풀어서 patch_notes_list
	for patch_note in patch_notes_body:
		one_patch_note = []

		one_patch_note.append(str(patch_note.select('h1')[0].text))
		one_patch_note.append(str(patch_note.select('h2')[0].text))
		one_patch_note.append(str(patch_note.select('p')[0].text))
		
		patch_lists = patch_note.select('ul')
		for patch in patch_lists:
			one_patch_note.append(str(patch.select('li')[0].text))

		patch_notes_list.append(one_patch_note)

	return patch_notes_list

	# 	file.write("제목 : " + str(patch_note.select('h1')[0].text))
	# 	file.write('\n' + '-'*20 + '\n')

	# 	file.write("소제목 : " + str(patch_note.select('h2')[0].text))
	# 	file.write('\n' + '-'*20 + '\n')

	# 	words = patch_note.select('p')
	# 	for word in words:
	# 		file.write("내용 : " + str(word.text))
	# 	file.write('\n' + '-'*20 + '\n')

	# 	file.write("패치 내용 : ")
	# 	file.write('\n')
	# 	patch_lists = patch_note.select('ul')
	# 	for patch_list in patch_lists:
	# 		file.write(str(patch_list.text))
	# 	file.write('\n' + '-'*20 + '\n')
	# file.close()

if __name__ == "__main__":
	get_patch_notes()
# response_body = response.read()
# xmlsoup = BeautifulSoup(response_body, 'html.parser')
# print(xmlsoup)

# print(response.getcode())