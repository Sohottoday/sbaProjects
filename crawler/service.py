from bs4 import BeautifulSoup as bs
import urllib.request
from urllib.request import urlopen

import sys
sys.path.insert(0, '/Users/user/SbaProjects')

from crawler.entity import Entity
import pandas as pd
from pandas import DataFrame as df
import os, shutil


class Service:
    def __init__(self):
        pass


    def bugs_music(self):
        pass


    def naver_movie(self):
        url = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        html = urllib.request.urlopen(url)
        soup = bs(html, 'html.parser')

        tags = soup.findAll('div', attrs={'class':'tit3'})

        for tag in tags:
            print(tag.a.string)

        url_header = 'https://movie.naver.com'
        for tag in tags:
            print(url_header+tag.a['href'])

        mytrs = soup.find_all('tr')
        no = 0          # 순서를 의미하는 번호
        totallist = []  # 전체를 저장할 리스트

        for one_tr in mytrs:
            #print(one_tr)
            #print('@' * 30)
            title = ''
            up_down = ''    # 상승/하강/불변을 표현하기 위함

            mytd = one_tr.find('td', attrs={'class':'title'})
            if(mytd != None):
                no += 1
                newno = str(no).zfill(2)

                mytag = mytd.find('div', attrs={'class':'tit3'})
                # string 속성 : 해당 태그가 가지고 있는 문자열을 추출
                title = mytag.a.string
                # td요소중에 3번째 요소를 추출
                mytd = one_tr.select_one('td:nth-of-type(3)')
                myimg = mytd.find('img')
                if myimg.attrs['alt'] == 'up':
                    up_down = '상승'
                elif myimg.attrs['alt'] == 'down':
                    up_down = '강등'
                else:
                    up_down = '불변'

                change = one_tr.find('td', attrs={'class':'range ac'})
                change = change.string

                # print(newno + '/' + title + '/' + up_down + '/' + change)
                totallist.append((newno, title, up_down, change))      

        mycolumn = ['순위', '제목', '변동', '변동값']
        myframe = df(totallist, columns=mycolumn)

        filename = 'naverMovie.csv'
        myframe.to_csv(filename)





    def naver_cartoon(self):
        myparser = 'html.parser'
        myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
        response = urlopen(myurl)
        soup = bs(response, myparser)
        print(type(soup))
        self.service = Service()

        mytarget = soup.find_all('div', attrs={'class':'thumb'})

        mylist = []
        for abcd in mytarget:
            myhref = abcd.find('a').attrs['href']

            myhref = myhref.replace('/webtoon/list.nhn?', '')
            result = myhref.split('&')

            mytitleId = result[0].split('=')[1]
            myweekday = result[1].split('=')[1]

            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?', '').replace(':', '')

            mysrc = imgtag.attrs['src']

            self.service.create_folder_weekend(mysrc, myweekday, mytitle)

            sublist = []
            sublist.append(mytitleId)
            sublist.append(myweekday)
            sublist.append(mytitle)
            sublist.append(mysrc)
            mylist.append(sublist)

        mycolumns = ['타이틀번호', '요일', '제목', '링크']
        myframe = df(mylist, columns=mycolumns)

        filename = 'cartoon.csv'

        myframe.to_csv(filename, encoding='utf-8', index=False)
        print(filename + ' 파일로 저장됨')




# 요일별 폴더 생성
    def create_folder_weekend(self, mysrc, myweekday, mytitle):
        weekday_dict = {'mon': '월요일', 'tue': '화요일', 'wed': '수요일', 'thu': '목요일', 'fri': '금요일', 'sat': '토요일', 'sun': '일요일'}

    # shutil : shell utility : 고수준 파일 연산. 표준 라이브러리
        myfolder = 'd:\\imsi2\\' # 유닉스 기반은 '/'이 구분자

        try:
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

                if os.path.exists(mypath):
                    # rmtree : remove tree
                    shutil.rmtree(mypath)
                    

                os.mkdir(mypath)

        except FileExistsError as err:
            print(err)

        image_file = urlopen(mysrc)
        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
        myfile = open(filename, mode='wb')
        myfile.write(image_file.read())
        myfile.close()    






