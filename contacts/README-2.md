클래스 하나가 단위 unit 이 된다.
이제 확장을 하겠스빈다.
객체지향에서는 디자인패턴이라는 개념이 존재한다.
1994년 GoF 4인방 개발자 에릭 감마 ... 패턴 23개로 정의...
이 분이 vscode 개발자이다.

패턴조합을 통해 큰 개념의 패턴이 나온다 -> MVC 패턴이라고 한다.
model, view, controller 이렇게 조합한다.        -> Java, C 언어에서 주로 사용하는 개념

model : 데이터처리  -> API 서버 -> Python   -> Tensorflow
view : 화면, UI 처리    -> React.js
controller : model과 view를 연결 --> 네트워크라고 한다. -> Flask(app.py) -> RESTful 방식

이 지점에서 팀내에서 나의 역할을 고민
곧 취업시 자신을 어필할 수 있는 혹은 자신있는 혹은 흥미있는 카테고리를 결정
Backend Tier(API 서버 구축담당 : Java, C, Python, SQL)
Frontend Tier(UI 서버 구축 담당 : Javascript, HTML, rEATJS)

모델을 제작하고 뷰를 만들어서 컨트롤러로 연결
프로토타입
독자적으로 움직이는 --> 모듈.
5개의 모듈(개인이 작성)을 합쳤을 때, 조립이 잘 되서 작동이 잘 되면 1단계를 패스한다.

캐글

dataset(test.csv, train,csv)를 모델이 추가

titanic 폴더에
dataset(test.csv, train.csv) 이게 존재하고
entity(속성) + service(기능) = 객체(object)

def __init__(self, .....) => 속성
def abc() : => 기능
결국 class 는 객체를 정의하는 것이다.

class가 여러개(entity, service)모여서 다시 큰 개념의 객체를 이룬다. 그때 이것을 클래스라 하지 않고 model이라고 한다.

패키지는 같은 컨셉을 공유하는 클래스의 집합... 모듈 - (진화) -> 모델
모델에 AI 개념이 없으면 web에서 말하는 모델이고
AI 개념이 존재하면 인공지능 모델이 된다.

여기서 AI 개념이라고 하면 머신러닝(기계학습) 코딩의 유무
dataset을 추가하면 이를 지도학습이라고 한다.
dataset이 없으면 이를 비지도학습이라고 한다.
지금 타이타닉은 dataset을 모델에 넣었으므로 이는 지도학습을 하겠다는 의미가 된다.
