from titanic.entity import Entity
import sys
sys.path.insert(0, '/Users/user/SbaProjects')
import pandas as pd
import numpy as np

"""
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼

"""



class Service:
    def __init__(self):
        self.entity = Entity()
        pass      

    # static으로 할 경우에는 @staticmethod 를 붙이고 동적(dynamic)으로 할 예정이면 매개변수에 self를 넣는다.(static일 경우 넣지 않는다.)
    def new_model(self, payload) -> object:
        this = self.entity
                                    # setter 는 할당연산자 = 이 존재하고 getter는 할당연산자가 존재하지 않는다.
        this.fname = payload
        return pd.read_csv(this.context + this.fname)       # p.139     df = tensor

    @staticmethod           # 계속 작동되고 있어야 하므로
    def create_train(this) -> object:     
        return this.train.drop('Survived', axis=1)      # train은 답이 제거된 데이터셋이다. => 생존자 목록 제거


    @staticmethod
    def create_label(this) -> object:         # 지도학습을 생성한다.
        return this.train['Survived']       # label은 곧 답이 된다.

    
    @staticmethod
    def drop_feature(this, feature) -> object:        # 차원축소를 진행한다.
        this.train = this.train.drop([feature], axis=1)       # 매트릭스에서 하나하나의 요소가 벡터
        this.test = this.test.drop([feature], axis=1)       # p.140에 보면 훈련, 테스트 세트로 나눈다.
        return this



    
