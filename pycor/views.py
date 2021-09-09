import os
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from datetime import datetime
from PIL import Image
import pytesseract
import re
from .models import Djangotest
from django.db import connection # 쿼리를 사용하기 위한 import


def home(request):
    context = {}
    context['menutitle'] = 'HOME'
    return render(request, 'home.html', context)

def ocr_upload(request):
    context = {}
    context['menutitle'] = 'READCLEAR'
    filename = datetime.now()

    imgname = ''
    resulttext = ''
    if 'fileSelect' in request.FILES:
        fileSelect = request.FILES.get('fileSelect', '')

        if fileSelect != '':
            name_old = fileSelect.name # org_file_name으로 저장되어야함
            # 받아와야하는 정보들 user_id, user_name, ext, org_file_name
            # 날짜별로 폴더 생성 후 날짜+시간으로 파일이름 저장, reg_id, reg_dt
            name_ext = os.path.splitext(name_old)[1] # png, jpg, jpeg 등 이미지 확장작만 받을 수 있게 해줘야함

            fs = FileSystemStorage(location='static/source') # 파일을 받아와 static/source 밑에 저장하는 과정
            imgname = fs.save(f"src_{name_old}", fileSelect) # 파일 이름을 원래의 파일이름이 아닌 저장시 알 수 있게 src_를 붙힌다.

            imgfile = Image.open(f"./static/source/{imgname}")

            resulttext = re.sub(r"[0-9]",' ',pytesseract.image_to_string(imgfile,lang='kor'))

            # wordlist = []
            #
            # for word in resulttext:
            #     if '정' in word:
            #         wordlist.append(word)

    context['imgname'] = imgname
    context['dbsavefilename'] = filename
    context['resulttext'] = [resulttext.replace(".", ''),resulttext.split()]
    # context['wordlist'] = wordlist
    return render(request, 'ocr_upload.html', context)



def ocr_list(request):
    context = {}
    context['menutitle'] = 'OCR_List'

    reSource = Djangotest.objects.all()
    context['reSource'] = reSource

    return render(request, 'ocr_list.html', context)


def FindPass(request):
    context = {}
    context['menutitle'] = 'OCR_List'

    reSource = Djangotest.object.fliter()
    context['reSource'] = reSource

    return render(request, 'ocr_list.html', context)


def NewCreate(request):
    context = {}
    context['menutitle'] = 'OCR_List'

    reSource = Djangotest.object.fliter()
    context['reSource'] = reSource

    return render(request, 'ocr_list.html', context)


def LoginPage(request):
    context = {}
    context['menutitle'] = 'OCR_List'

    reSource = Djangotest.object.fliter()
    context['reSource'] = reSource

    return render(request, 'ocr_list.html', context)
