# url, parser, path, api, apikey ==> str 타입
from dataclasses import dataclass

@dataclass
class Entity:
    url : str = 'https://comic.naver.com/webtoon/weekday.nhn'
    parser : str = 'html.parser'
    path : str = 'd:\\imsi\\'
    api : str = ''
    apikey : str = ''
    
    
    