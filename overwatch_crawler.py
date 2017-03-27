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


# html에서 태그 제거하고 텍스트만 가져오도록 하는 메서드
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    return True


def get_test_patch_notes():
    response = requests.get('https://playoverwatch.com/ko-kr/blog/')

    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    test_server_texts = soup.select('.h6.link-title')
    test_server_list = []

    for text in test_server_texts:
        if "오버워치 공개 테스트 서버 오픈" in text.text:
            test_server_list.append('https://playoverwatch.com' + text['href'])
        print('https://playoverwatch.com' + text['href'])

    test_patch_notes_list = []
    # print(test_server_list)
    for test_server in test_server_list:
        ts_response = requests.get(test_server)

        ts_html = ts_response.text
        ts_soup = BeautifulSoup(ts_html, 'html.parser')
        ts_title = ts_soup.select('.blog-title')[0].text
        ts_date = ts_soup.select('.publish-date')[0].text

        ts_content = ts_soup.select('.blog-content')

        full_text = ""
        for i in ts_content:
            full_text = full_text + i.text

        ts_list = [ts_title, '', ts_date, full_text]
        test_patch_notes_list.append(ts_list)

    print("Test patch notes Returned")
    return test_patch_notes_list


if __name__ == "__main__":
    get_test_patch_notes()
    get_patch_notes()
    # response_body = response.read()
    # xmlsoup = BeautifulSoup(response_body, 'html.parser')
    # print(xmlsoup)

    # print(response.getcode())
