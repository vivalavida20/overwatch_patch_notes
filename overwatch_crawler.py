# -*- coding : utf-8 -*-
import os
import sys
import requests
from bs4 import BeautifulSoup
# from lxml import html


def get_patch_notes():

	
	response = requests.get('https://playoverwatch.com/ko-kr/game/patch-notes/pc/')

	html = response.text
	soup = BeautifulSoup(html, 'html.parser')
	patch_notes_body = soup.select('.patch-notes-body')


	
	patch_notes_list = []

	
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



if __name__ == "__main__":
	get_patch_notes()
# response_body = response.read()
# xmlsoup = BeautifulSoup(response_body, 'html.parser')
# print(xmlsoup)

# print(response.getcode())