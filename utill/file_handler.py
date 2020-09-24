from dataclasses import dataclass

'''
contextPath : /Users/user/SbaProjects
fnamePath : /titanic/data/

'''

# @dataclass 는 __init__, __repr__, __eq__
@dataclass          # https://sjquant.tistory.com/30
class FileReader:

    context : str = ''
    fname : str = ''
    train : object = None
    test : object = None
    id : str = ''
    label : str = ''