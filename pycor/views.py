import os
import pymysql

import pytesseract
import re
from .models import Djangotest
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from datetime import datetime
from PIL import Image

# 이미지 흑백의 대한 스케일을 올리기 위한 import
import numpy as np
from matplotlib import pyplot as plt
import cv
import cv2

from django.db import connection # 쿼리를 사용하기 위한 import
# 돌아가는 알고리즘
# 1, 일단 받아오는 이름을 기준으로 조회 있으면 텍스트문으로 -> 없어도 텍스트문으로 하지만 html에서 표시하기 즉, 비동기로 이루어져야함

def home(request):
    context = {}
    context['menutitle'] = 'HOME'
    return render(request, 'home.html', context)

def ocr_upload(request):
    context = {}
    context['menutitle'] = 'READCLEAR'
    filename = datetime.now()

    imgname = ''
    resulttext = [] # 약품의 이름 들고오기,
    Medicine_code = ' '
    wordlist = []
    textlist = []

    color = ('b', 'g', 'r')
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

            resulttext = re.sub(r"[a-zA-Z0-9!@#%※$/{}_.]",' ',pytesseract.image_to_string(imgfile, lang='kor')).replace(" ", '').replace("\n", " ").replace("내복",'').replace("점","정").replace("전","정")

            # data = resulttext.replace("\n", " ").replace("내복",'').replace("점","정").replace("전","정")

            resulttext = resulttext.split()

            for word in resulttext:
                   if word.endswith("정"):
                       wordlist.append(word)
                   elif word.endswith("주"):
                       wordlist.append(word)

            Medicine_code = re.sub(r"[^0-9]",' ',pytesseract.image_to_string(imgfile, lang='kor')).replace("\n"," ")

            # image = cv2.imread(fileSelect, cv2.IMREAD_GRAYSCALE) # 이미지 흑백으로 만들기
            #
            # image_enhanced = cv2.equalizeHist(image)

            # plt.imshow(image_enhanced, cmap="gray"),plt.axis("off")
    # OCR의 기준으로 정, 점, 전으로 끝나는 단어들 불러와야함
    context['Medicine_code'] = Medicine_code.split()
    context['imgname'] = imgname
    context['dbsavefilename'] = filename
    context['resulttext'] = resulttext
    context['wordlist'] =  wordlist

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

    reSource = Djangotest.objectn.fliter()
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
