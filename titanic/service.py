from titanic.entity import Entity

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

    # static으로 할 경우에는 @staticmethod 를 붙이고 동적(dynamic)으로 할 예정이면 매개변수에 self를 넣는다.(static일 경우 넣지 않는다.)
    def new_model(self, payload):
        this = self.entity
        this.context = './data'         # setter 는 할당연산자 = 이 존재하고 getter는 할당연산자가 존재하지 않는다.
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod           # 계속 작동되고 있어야 하므로
    def create_train(this):     
        return this.train.drop('Survived', axis=1)      # train은 답이 제거된 데이터셋이다. => 생존자 목록 제거


    # self 없이 create_label 기능을 만듭니다.
    # self 없이 차원축소하기 위해 drop_feature 기능을 만듭니다.

    @staticmethod
    def create_label(this):         # 지도학습을 생성한다.
        return this.train['Servived']       # label은 곧 답이 된다.

    
    @staticmethod
    def drop_feature(this):         # 차원축소를 진행한다.
        pass
