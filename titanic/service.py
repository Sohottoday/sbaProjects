# from titanic.entity import Entity
# import sys
# sys.path.insert(0, '/Users/user/SbaProjects')
# import pandas as pd
# import numpy as np

# # sklearn algorithm : classification, regression, clustring, reduction
# # classifier 을 많이 가져온 이유는 classification을 하기 위함
# # k값은 count의 의미로 이해
# from sklearn.tree import DecisionTreeClassifier         # dtree
# from sklearn.ensemble import RandomForestClassifier     # r-forest
# from sklearn.naive_bayes import GaussianNB              # nb
# from sklearn.svm import SVC                             # svm
# from sklearn.neighbors import KNeighborsClassifier      # knn
# from sklearn.model_selection import train_test_split
# from sklearn.model_selection import KFold               # fold는 접는다는 의미로 k가 있으므로 몇번 접느냐는 의미 : 데이터를 몇조각을 낼 것이냐는 의미에 가깝다.
# from sklearn.model_selection import cross_val_score


# """
# ### PassengerId  고객ID,           @ 문제
# ### Survived 생존여부,              @ 머신러닝 모델이 맞춰야 할 답
# Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
# Name,
# Sex,
# Age,
# SibSp 동반한 형제, 자매, 배우자,
# Parch 동반한 부모, 자식,
# ### Ticket 티켓번호,                @ 쓰레기 값
# Fare 요금,
# ### Cabin 객실번호,                 @ 쓰레기 값
# Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼

# """

# class Service:
#     def __init__(self):
#         self.entity = Entity()
#         pass      

#     # static으로 할 경우에는 @staticmethod 를 붙이고 동적(dynamic)으로 할 예정이면 매개변수에 self를 넣는다.(static일 경우 넣지 않는다.)
#     def new_model(self, payload) -> object:
#         this = self.entity
#                                     # setter 는 할당연산자 = 이 존재하고 getter는 할당연산자가 존재하지 않는다.
#         this.fname = payload
#         return pd.read_csv(this.context + this.fname)       # p.139     df = tensor

#     @staticmethod           # 계속 작동되고 있어야 하므로
#     def create_train(this) -> object:     
#         return this.train.drop('Survived', axis=1)      # train은 답이 제거된 데이터셋이다. => 생존자 목록 제거


#     @staticmethod
#     def create_label(this) -> object:         # 지도학습을 생성한다.
#         return this.train['Survived']       # label은 곧 답이 된다.

    
#     @staticmethod
#     def drop_feature(this, feature) -> object:        # 차원축소를 진행한다.
#         this.train = this.train.drop([feature], axis=1)       # 매트릭스에서 하나하나의 요소가 벡터
#         this.test = this.test.drop([feature], axis=1)       # p.140에 보면 훈련, 테스트 세트로 나눈다.
#         return this



#     @staticmethod
#     def pclass_ordinal(this) -> object: 
#         return this

#     @staticmethod
#     def title_nominal(this) -> object:          #name
#         combine = [this.train, this.test]
#         for dataset in combine:
#             dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
#         for dataset in combine:
#             dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
#             dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
#             dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
#             dataset['Title'] = dataset['Title'].replace('Mile', 'Mr')
#         title_mapping = {'Mr':1, 'Miss':2, 'Mrs':3, 'Master':4, 'Royal':5, 'Rare':6}
#         for dataset in combine:
#             dataset['Title'] = dataset['Title'].map(title_mapping)
#             dataset['Title'] = dataset['Title'].fillna(0)       # Unknown
#         this.train = this.train
#         this.test = this.test

#         return this

#     @staticmethod
#     def sex_nominal(this) -> object:        # male = 0, female = 1
#         combine = [this.train, this.test]       # 반복된 코드를 피하기 위해 사용, train과 test가 묶인다.
#         sex_mapping = {'male':0, 'female':1}
#         for dataset in combine:
#             dataset['Sex'] = dataset['Sex'].map(sex_mapping)

#         this.train = this.train     # overriding
#         this.test = this.test

#         # this.train = combine[0]
#         # this.test = combine[1]

#         # this.train['Sex'] = this.train['Sex'].map({'male':0, 'female':1})
#         # this.test['Sex'] = this.test['Sex'].map({'male':0, 'female':1})
#         return this

#     @staticmethod
#     def age_ordinal(this) -> object:
#         train = this.train
#         test = this.test
#         train['Age'] = train['Age'].fillna(-0.5)            # age는 평균으로 넣기도 애매하고, 다수결로 넣기도 근거가 없다. 특히 age는 생존률 판단에서 가중치(weight)가 높으므로 디테일한 접근이 필요
#         test['Age'] = test['Age'].fillna(-0.5)              # 나이를 모르는 승객은 모르는 상태로 처리해야 값의 왜곡을 줄일 수 있기 때문에 -0.5라는 경계값(어느쪽에도 속하지 않는 값)으로 처리
#         bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]       # 안의 숫자는 양 숫자 사이의 범위를 의미
#         labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']      # [] 에 있으므로 변수명으로 판단,
#         train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
#         test['AgeGroup'] = pd.cut(test['Age'], bins, labels=labels)
#         age_title_mapping = {
#             0: 'Unknown',
#             1: 'Baby',
#             2: 'Child',
#             3: 'Teenager',
#             4: 'Student',
#             5: 'Young Adult',
#             6: 'Adult',
#             7: 'Senior'
#         }   # []에서 {}으로 처리하면 labels를 값으로 처리하겠다는 의미
        
#         for x in range(len(train['AgeGroup'])):
#             if train['AgeGroup'][x] == 'Unknown':
#                 train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]
#         for x in range(len(test['AgeGroup'])):
#             if test['AgeGroup'][x] == 'Unknown':
#                 test['AgeGroup'][x] = age_title_mapping[test['Title'][x]]

#         age_mapping = {
#             'Unknown' : 0,
#             'Baby' : 1,
#             'Child' : 2,
#             'Teenager' : 3,
#             'Student' : 4,
#             'Young Adult' : 5,
#             'Adult' : 6,
#             'Senior' : 7
#         }
#         train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
#         test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
#         this.train = train
#         this.test = test
        
#         return this


#     @staticmethod
#     def sibsp_numeric(this) -> object:
#         return this

#     @staticmethod
#     def parch_numeric(this) -> object:
#         return this

#     @staticmethod
#     def fare_ordinal(this) -> object:
#         this.train['FareBand'] = pd.qcut(this['Fare'], 4, labels={1, 2, 3, 4})          # qcut 은 분할 해준다는 의미(분할하려는것, 분할하려는 등분(여기서는 4이므로 4등분), 부여하려는 값)
#         this.test['FareBand'] = pd.qcut(this['Fare'], 4, labels={1, 2, 3, 4})
#         return this

#     @staticmethod
#     def fareBand_nominal(this) -> object:           # 요금이 다양하니 클러스터링을 하기위한 준비
#         this.train = this.train.fillna({'FareBand' : 1})        # FareBand는 존재하지 않는 변수지만 추가시킴
#         this.test = this.test.fillna({'FareBand' : 1})
#         return this



#     @staticmethod
#     def embarked_nominal(this) -> object:
#         this.train = this.train.fillna({'Embarked': 'S'})
#         this.test = this.test.fillna({'Embarked': 'S'})
#         # 많은 머신러닝 라이브러리는 클래스 레이블이 '정수'로 인코딩 되었다고 기대함
#         # 교과서 146 문자 blue = 0, green = 1, red = 2 로 치환
#         this.train['Embarked'] = this.train['Embarked'].map({'S':1, 'C':2, 'Q':3})        # ordinal 아님
#         this.test['Embarked'] = this.test['Embarked'].map({'S':1, 'C':2, 'Q':3})
#         return this


    
#     # Machine Learning  :   dtree, rforest, nb, knn, svm 이것을 대표로 사용

#     @staticmethod
#     def create_k_fold():            # 먼저 데이터를 조각내준다..?
#         return KFold(n_splits=10, shuffle=True, random_state=0)

    
#     def accuracy_by_dtree(self, this):
#         dtree = DecisionTreeClassifier()
#         score = cross_val_score(dtree, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
#         return round(np.mean(score) * 100, 2)

#     def accuracy_by_rforest(self, this):
#         rforest = RandomForestClassifier()
#         score = cross_val_score(rforest, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
#         return round(np.mean(score) * 100, 2)

#     def accuracy_by_nb(self, this):
#         nb = GaussianNB()
#         score = cross_val_score(nb, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
#         return round(np.mean(score) * 100, 2)

#     def accuracy_by_knn(self, this):
#         knn = KNeighborsClassifier()
#         score = cross_val_score(knn, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
#         return round(np.mean(score) * 100, 2)

#     def accuracy_by_svm(self, this):
#         svm = SVC()
#         score = cross_val_score(svm, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
#         return round(np.mean(score) * 100, 2)


    

    

