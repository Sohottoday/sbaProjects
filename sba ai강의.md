

[진돌이/인공지능/직장인] [오전 9:00] https://meetingsapac45.webex.com/meet/pr1709324153

설진욱 강사님

010-3511-9528

ugcadman@naver.com

cafe.naver.com/ugcadman







- 패키지(폴더)
  - 관련성이 있는 모듈(파일)들을 별도로 묶어서 관리하는 개념
  - 유지 보수성
- 모듈 : 한개의 파일을 모듈이라고 한다.



- 크롤링
  - 웹 페이지의 링크들을 돌아다니면서 데이터를 수집하는 행위
  - 어떤 페이지에서 필요한 정보를 추출하는 행위
  - BeautifulSoup4(정적 페이지), Selenium(동적 페이지, 자바 스크립트)



sqlite3

``` sqlite
ddl(데이터 정의어)
create table students(id text primary key, name text, birth text)

주의
문자열이나 날짜 형은 반드시 외따옴표를 넣어줘야 한다.
행 추가, 수정, 삭제 등은 반드시 커밋을 해줘야 한다.

dml(데이터 조작어)
행 추가
insert into students(id, name, birth) values('lee', '이승기', '1989/12/25');
insert into students(id, name, birth) values('kang', '강감찬', '1111/11/11');

트랜잭션 : commit <-> rollback
commit : 적용시킴
rollback : 되돌리기
commit;

행 정보 수정
update students set name = '이순신' where id = 'lee';

강감찬의 생일을 1000/10/10 으로 변경해보시오
update students set birth = '1000/10/10' where name = '강감찬';

모든 행 삭제
delete from students;
commit;

데이터 제거하기
drop table students;

```

``` sqlite
dql(데이터 질의어)
모든 데이터 조회
select * from students;

id가 'ko'인 학생 조회
select * from students where id = 'ko';

order by : 정렬하는 것(asc, desc)
select * from students order by name desc;

like연산자 : whildcard를 사용한 조회
_(언더바) 는 한글자를 의미
%는 0개 이상 무한개 이하를 의미
select * from students where name like '%이%';

이% : 성씨가 '이'씨인 사람
%이 : 이름의 끝이 '이'로 끝나는 사람
%이% : 이름의 가운데가 '이'인 사람

fetch(패치) : 내용물의 요소를 바깥으로 끄집어내는 동작
	fetch_one(), fetch_all()
	
```



조인 : 2개 이상의 테이블을 합쳐서 만드는 새로운 데이터 셋

seleft 컬럼들

from 테이블A join 테이블B

on 테이블A.컬럼a = 테이블B.컬럼b;

``` sqlite
select * from students join sungjuk
on students.id = sungjuk.id;

별칭을 사용
select * from students st join sungjuk sg
on st.id = sg.id;

select st.id, st.name, st.birth, sg.subject, sg.jumsu from students st join sungjuk sg
on st.id = sg.id;

sql = " select st.id, st.name, st.birth, sg.subject, sg.jumsu"
sql += " from students st join sungjuk sg "
sql += " on st.id = sg.id"
문잡을 합칠때는 띄워쓰기를 주의해야 한다.
```

``` sqlite
이름이 '이문세'인 친구의 성적을 구해보자
select id from students where name = '이문세';

select * from sungjuk where id = 'lee';

메인 쿼리 : 외부에 있는 select 구문
서브 쿼리 : 메인 쿼리 내부에 들어 있고, 메인 쿼리보다 우선적으로 실행이 되는 쿼리

select * from sungjuk
where id = (select id from students where name = '이문세')

고아라의 시험 점수만 출력하기
select jumsu from sungjuk
where id = (select id from students where name = '고아라')


sql = "select * from sungjuk"
sql += " where id = (select id from students where name = '이문세')"
```





- MVC 에서의 코딩하는 순서

  - 구조(frame)를 만듭니다.

    1. model을 만들고 view를 만들어서 controller로 연결(network) 한다.

       model = entity + service 속성 + 기능 => 모델객체

       view = Reactjs로 전환된다



​					model과 view가 언어가 다르다.

​					마치 한국인과 미국인이 만나 서로 언어를 몰라 통역을 부르는 느낌

​					controller가 통역의 역할을 한다. 그런데 그 통역하는 사람이 한국인



​					python과 javascript가 만났지만 서로 syntax가 다르다(grammer와 달리 조금만 틀려도 호환 X)

​					그래서 transfer를 불러 data를 주고받을 수 있다.

​					flask가 transfer 역할을 한다. 그 역할하는 객체의 언어가 python



​					각각 하는 일이 다르다.

​					뇌의 역할을 하는 모델이 python

​					

​					프로젝트를 만드는데 칩을 이식하면 단기간에 성능이 올라간다.

​					유료칩(스타트업)도 있고, 무료칩도 있는데 이 중 성능이 검증된 유명한 것이 텐서플로(구글), 파이토치(페이스북)이 양강

​					이 과정은 텐서플로 사용법을 배우는 과정으로 코딩 컨벤션을 결국 텐서플로에 최적화시켜야 한다.

​					그래서 객체지향(class 단위) 방식으로 바꾼 것

​					인공지능을 담당하는 미세조정 파트는 텐서플로에 의존한다.



- machine vs model 다른점
  - 컴퓨터공학에서는 상태를 통해 구문 state
  - 머신은 러닝을 한다.
  - 모델은 러닝을 하지 않는다.
  - 머신러닝에서는 알고리즘을 공부하는 것이 아니라 내가 만든 머신을 공부시키는 것이라는 개념
  - 우리의 고민은 어떤 알고리즘을 우리가 만드는 모델에 주입을 시킬 것인가 하는 지점



- 모델을 만들 때

  1. 모델을 훈련시킬 데이터에서 쓰레기값 제거(데이터 전처리) = feature를 줄이는 것

  ex) 타이타닉 정보를 통해 만약 A라는 가상의 인물이 당시 1912년 침몰 당시 타이타닉에 승선했다면 생조노학률은 어찌 될 것인가?

  ​	더 나아가 현재 승객 안전을 위한 조치를 어떻게 하면 비슷한 사고 발생시 생존률을 올릴 수 있을 것인가 하는 문제로 귀결될 수 있다.

  

- **variable(변하는 상태)** vs **constant(변하지 않는 상태)**

  - variable은 분류가 가능하다

    분류기준을 두고 나누는데 크게 2분하면

    cate, norminal(= : name)

    다시 cate는 ordinal(순서)(=: order), numeric(수치)(=: number)

  - 그래서 결국은 ordinal, numeric, norminal 로 나뉜다.

  - 변수에 따라 어떠한 방식으로 편집할지 판단해야 한다.



- 교과서 138p를 보면 누락된 값 처리 방식이 나온다.

  embarked 기준으로 할 때

  embarked는 지우면 안되고 즉, dropna를 쓰면 안되고 139p 대체하는 방식을 사용해야 한다.

  null 값을 무엇으로 넣을 것인가?

  교재에는 평균값을 넣는다고 써 있다.

  그러나 embarked값은 str이라 평균값을 구할 수 없으므로 가장 많이 승선한 항구로 대체한다.

  물론 통계를 왜곡할 수 있지만 null의 수가 적으므로 무시한다.

  빈 값이 존재하면 아예 그 변수를 사용할 수 없으므로 차선책을 택한다는 의미이다.

  

- 코딩은 반복된 코드를 싫어하므로 반복문 등을 사용

``` python
@staticmethod
    def sex_nominal(this) -> object:        # male = 0, female = 1
        combine = [this.train, this.test]       # 반복된 코드를 피하기 위해 사용, train과 test가 묶인다.
        sex_mapping = {'mail':0, 'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)

        this.train = this.train     # overriding
        this.test = this.test

        # this.train = combine[0]
        # this.test = combine[1]

        # this.train['Sex'] = this.train['Sex'].map({'male':0, 'female':1})
        # this.test['Sex'] = this.test['Sex'].map({'male':0, 'female':1})
        return this
```



- Data 수집
  - 방법론
  - 정형(csv) - 스키마구조 존재
  - 비정형() - 스키마구조 존재하지 않는다. Computer 인식 불가 =>
    - 웹 -> 웹 크롤링
    - 문서 -> 텍스트 마이닝
    - 전처리를 위해 정규 표현식이 필요하다.



- 정규표현식 re
  - ? : unique
  - = : all
  - \+ : not null
  - {n} : 

