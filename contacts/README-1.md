Object = 기능(function) + 속성(Property, Attribute, Feature) => 파라미터(AI 파트)
하나의 { ... } 에 같이 있음
() : 라운드 => 컨티션, 파라미터존, tuple
{} : 컬 => 블락, json, Dict
[] : 스퀘어 브레이스 => array, [[]] => matricx
총 3가지 ==> notation 이라고 한다.
=> 언어 기호학

기본적으로 컴퓨터 공학에서는 0과 1만이 존재한다. 이진수 - binary code

T, F판단 : 1850년 --> 전선(모스부호) --> 컴퓨터

선택지는 항상 두가지 중에 하나를 선택하는 구조 -> 컴퓨터공학에서의 해법

on, off의 개념
요소가 존재, 비존재로 나뉜다. ==> Decision Tree (Origin AI 알고리즘)

Q 객체지향 VS 함수형 프로그래밍 중 구분하는 기준은 무었이 있고 없고인가?
=> 속성이 있으면 객체지향, 없으면 함수형

class Calculator:
    def __init__(self, num1, num2):
    # 생성자 함수 --> 인스턴스(객체)를 만드는 함수 __ 언더스코어 라고 한다. 2개를 사용. 접근제한 private
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 == 0:
            return '두번째 숫자에 0이 들어갈 수 없습니다.'
        else:
            return self.num1 // self.num2

if __name__ == "__main__":
    calc = Calculator(6, 2)     # num1 = 4, num2 = 6
    sumResult = calc.sum()
    subResult = calc.subtract()
    multiResult = calc.multiplication()
    diviResult = calc.division()
    print(f'덧셈 결과 {sumResult}')
    print(f'뺄셈 결과 {subResult}')
    print(f'곱셈 결과 {multiResult}')
    print(f'나눗셈 결과 {diviResult}')


결론 : 객체지향은 속성이 존재해야 한다. 그리고 속성을 정의하는 곳은 __init__(속성파라미터) 이다.
self는 객체내부의 속성에 접근하는 키워드
속성은 은닉화때문에 반드시 self. 로만 접근할 수 있다.
이는 보안의 기본처리이다. __init__은 클래스 내부에서만 접근한다.

클래스 내부에서 메소드의 종류는 몇가지인가? dynamic 동적, static 정적
해석 : 
기준 - self 입니다.
self exist dynamic -> 데이터를 메모리에서 유효한 시간동안만 존재. 그 메서드가 소멸된 후 값은 self에 저장된다.
self !exist static -> 반 영속적으로 저장된다.()


