import sys
sys.path.insert(0, '/Users/user/SbaProjects')       # vscode가 자동경로를 못잡기 때문
import pandas as pd
import numpy as np
from titanic.entity import Entity
from titanic.service import Service

"""
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Fare 요금,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼

"""

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()


    def modeling(self, train, test): # -> object
        service = self.service
        this = self.preprocessing(train, test)
        print(f'훈련 컬럼 : {this.train.columns}')
        this.label = service.create_label(this)
        this.train = service.create_train(this)

        return this


    def preprocessing(self, train, test): # -> object
        service = self.service
        this = self.entity
        this.train = service.new_model(train)       # payload
        this.test = service.new_model(test)         # payload
        this.id = this.test['PassengerId']          # machine에게는 이것이 question이 된다.
        print(f'드롭 전 변수 : {this.train.columns}')
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        print(f'드롭 후 변수 : {this.train.columns}')
        this = service.embarked_nominal(this)
        print(f'승성한 항구 정제결과 : {this.train.head()}')
        this = service.title_nominal(this)
        print(f'타이틀 정제결과 : {this.train.head()}')
        # name 변수에서 title을 추출했으니 name은 필요가 없어졌고, str이니 후에 ML-lib가 이를 인식하는 과정에서 에러를 발생시킬 것이다.
        this = service.drop_feature(this, 'Name')
        this = service.drop_feature(this, 'PassengerId')
        this = service.age_ordinal(this)
        print(f'나이 정제결과 : {this.train.head()}')
        this = service.drop_feature(this, 'SibSp')
        this = service.sex_nominal(this)
        print(f'성별 정제결과 : {this.train.head()}')
        this = service.fareBand_nominal(this)
        print(f'요금 정제결과 : {this.train.head()}')
        this = service.drop_feature(this, 'Fare')
        print('###########TRAIN 정제 결과##########')
        print(f'전체 정제결과 : {this.train.head()}')
        print('###########TEST 정제 결과##########')
        print(f'전체 정제결과 : {this.test.head()}')
        print('###########train na 체크##########')
        print(f'train na 체크 : {this.train.isnull().sum()}')
        print('###########test na 체크##########')
        print(f'test na 체크 : {this.test.isnull().sum()}')
    

        return this


    def learning(self, train, test):
        service = self.service
        this = self.modeling(train, test)
        print('-----------------Learning 결과----------------')
        print(f'결정트리 검증결과 : {service.accuracy_by_dtree(this)}')
        print(f'랜덤포리 검증결과 : {service.accuracy_by_rforest(this)}')
        print(f'나이브베이즈 검증결과 : {service.accuracy_by_nb(this)}')
        print(f'KNN 검증결과 : {service.accuracy_by_knn(this)}')
        print(f'SVM 검증결과 : {service.accuracy_by_svm(this)}')


    def submit(self):           # machine이 된다. 이 단계에서는 캐글에게 내 머신을 보내서 평가받게 하는 것.
        pass

if __name__ == '__main__':
    ctrl = Controller()
    ctrl.learning('train.csv', 'test.csv')