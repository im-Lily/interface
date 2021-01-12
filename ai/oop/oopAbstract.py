'''
다중상속
추상화
데코레이션
제너레이터
이터레이터
'''

class Animal(object) :
    def cry(self):
        pass

#상속과 오버라이딩
class Tiger(Animal) :
    def jump(self):
        print('jump')
    def cry(self):
        print('어흥')

class Lion(Animal) :
    def bite(self):
        print('bite')
    def cry(self):
        print('그르렁')

# 다중상속
# 1차 우선순위 : 가장 먼저 정의된 부모(namespace)
class Liger(Tiger, Lion) :
    def play(self):
        print('play')

# 추상클래스
'''
- 클래스를 만드는 이유 : 객체를 생성하기 위해
- 추상클래스는 객체생성 불가능
- 추상메서드(함수)를 하나이상 포함하면 추상클래스
- 함수 구현을 강제하기 위해 사용
'''

from abc import *

# 추상메서드를 포함한 추상클래스 -> 객체생성 불가능
class Base(metaclass=ABCMeta) :
    @abstractmethod # 어노테이션 -> 추상메서드
    # 자식들에게 study 함수를 강제하고 싶음
    def study(self):
        pass # 추상메서드는 호출할 일이 없으므로 빈 메서드로 만듦

    def goToShchool(self):
        print('hard study')

# 부모의 추상메서드를 상속받아 객체생성 불가능 -> 오버라이딩
# 추상 클래스를 상속받았다면 추상메서드를 모두 구현해주어야함
class Student(Base) :
    def study(self):
        print('공부하자')

'''
특수문법 - 데코레이션(코드 간결화)
공통의 모듈을 외부로 빼내어 데코레이터를 이용하여 정의
Decorator는 함수의 인자로 다른 함수를 전달하는 과정에서 적용
'''

def outerFunc(func) :
    def innterFunc() :
        func()
    return innterFunc

def userFunc() :
    print('userFunc 함수수행')
# userFunc()

decoratorFunc = outerFunc(userFunc)
decoratorFunc()

import time
def userOuterFunc(func):
    def userInnerFunc():
        print('{} 함수수행 시간 계산'.format(func.__name__))
        start = time.time()
        func()
        end = time.time() - start
        print('{} 함수수행 시간은 {} 이다'.format(func.__name__,end))
    return userInnerFunc

decoratorUserFunc = userOuterFunc(userFunc)
decoratorUserFunc()

import datetime
def loggerLoginEun() :
    print("eun's login")
loggerLoginEun()

def loggerLoginJeong() :
    print("jeong's login")

def loggerLoginKing() :
    print("king's login")

def datetimeDecorator(func) :
    def wrapper() :
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return wrapper

eun = datetimeDecorator(loggerLoginEun)
eun()
king = datetimeDecorator(loggerLoginKing)
king()

@datetimeDecorator
def dumpFunc():
    print('함수 실행')

dumpFunc()

'''
데코레이터 호출 방법 
1. 외부함수의 인자값으로 함수받아서 호출
2. @decorator 입력하여 호출
'''

''' 데코레이션 [실습]
1. typeChecker Decorator 생성(인자의 유효성 검사)
- digit01, digit02 를 곱한 값을 출력하는 함수
- typeChecker Decorator digit01, digit02가 정수가 아니면
- 'only integer support' 출력
'''
def typeChecker(func) :
    def innerFunc02(digit01, digit02):
        if type(digit01) != int or type(digit02) != int :
            print('only integer support')
            return # if안에서 return을 만나면 함수종료
        return func(digit01, digit02)
    return innerFunc02

# 데코레이터 사용
@typeChecker
def div(digit01, digit02) :
    return digit01 * digit02

msg = div(2, 1)
print(msg)

# 파라미터와 관계없이 모든 함수에 적용가능한 데코레이터 생성
# *args, **kargs - 가변인자 사용

def generalDeco(func) :
    def wrapper(*args, **kargs) :
        print('this is decorated')
        return func(*args, **kargs)
    return wrapper

@generalDeco
def userSquare(digit) :
    return digit * digit
print(userSquare(2))
@generalDeco
def userPlus(digit01, digit02) :
    return digit01 * digit02
print(userPlus(2,3))
@generalDeco
def userQuad(digit01, digit02, digit03, digit04) :
    return digit01 * digit02 * digit03 * digit04
print(userQuad(2,3,4,5))

def makeBold(func) :
    def wrapper(sting) :
        return '<b>' + func(sting) + '</b>'
    return wrapper

def makeFont(func) :
    def wrapper(sting) :
        return '<i>' + func(sting) + '</i>'
    return wrapper

# 데코레이터 실행순서 -> 위에서 아래로
@makeBold
@makeFont
def makeBoldFont(string) :
    return string

print(makeBoldFont('두개의 데코레이터를 활용'))

# class - function decorator 적용
def tagH1(func) :
    # 인스턴스를 인자로 받을 수 있도록 self 입력해주어야함
    def wrapper(self, *args, **kwargs) :
        return '<h1>{}</h1>'.format(func(self, *args, **kwargs))
    return wrapper

# 외부의 데코레이터 사용
class Per(object) :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @tagH1
    def getName(self):
        return (self.name, self.age)

per = Per('eun', 25)
print('per - ', per.getName())

''' Iterable Object -> Iterator
- iterable object
list, set, tuple, dict, Text sequence  - (collection)
for ~ in collection:
    pass
    
- iterator -> 파이썬 모듈이 가지고 있는 내장함수 iter()
-> 순차적으로 다음 데이터 리턴가능한 객체
-> 내장함수 next() 사용해서 순환하는 다음 값 반환
'''

for num in [1,2,3,4,5] :
    print(num)

for char in 'text sequence' :
    print(char)

# 오류 발생 -> userList는 iterator 객체가 아님
userList = [1,2,3,4,5]
# print(next(userList))

userIter = iter(userList)
print(type(userIter), type(userList))
print(next(userIter))

# 사용자 정의 iterator 클래스 생성
# iterable 작업
class Counter :
    def __init__(self, stop):
        self.stop = stop
    def __iter__(self):
        return CounterIter(self.stop)

# iterator 작업
class CounterIter :
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    def __next__(self):
        if self.current < self.stop :
            rtnVale = self.current
            self.current += 1
            return rtnVale
        else :
            pass

cntIter = iter(Counter(10))
print(next(cntIter))

## ohter

class Counter :
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.stop :
            r = self.current
            self.current += 1
            return r
        else :
            raise StopIteration

for i in Counter(3) :
    print(i, end= ' ')

# 배수 이터레이터
class MultipleInter :
    def __init__(self, stop, multiple):
        self.stop = stop
        self.multiple = multiple
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.current += 1
        if self.current * self.multiple < self.stop :
            return self.current * self.multiple
        else :
            raise StopIteration

for i in MultipleInter(20,3) :
    print(i, end=' ')
print()
for i in MultipleInter(30,5) :
    print(i, end=' ')

# Comprehension
'''
[출력표현식 for 요소 in sequence [if 조건식]] - list type
{출력표현식 for 요소 in sequence [if 조건식]} - set type, python 3.0 이상
{key-value for 요소 in sequence [if 조건식]} - dict type, python 3.0 이상
'''

dataset = [4, True, 'eun', 3.3, 10]
# 정수값만 출력
intType = [data ** 2 for data in dataset if type(data) == int]
print(intType, type(intType))

dataset =[1,1,2,2,3,3,3,4,4]
setType = {value * value for value in dataset}
print(setType, type(setType))

dataset = {1 : 'eun', 2 :'jeong', 3 : 'kyung'}
print('dict keys - ', dataset.keys())
print('dict values - ', dataset.values())
print('dict items - ', dataset.items()) # tuple형식으로 출력

# key값이 1 이상인 데이터를 값:키 형식으로 새로운 set으로 생성
# keySet = {key for key in dataset if dataset.keys() if key > 1}
# print(keySet, type(keySet))

keySet = {value:key for key, value in dataset.items() if key > 1}
print(keySet, type(keySet))

# key값을 10단위로 한번에 바꾸기
keySet = {key*10:value for key, value in dataset.items()}
print(keySet, type(keySet))

# generator - 메모리 성능 위하여 루프를 컨트롤하기 위해 쓰이는 루틴
'''
iterator를 만들어주는 기능
yield 키워드 이해 필요
'''

def textSequenceFunc() :
    msg = 'hi python'
    for txt in msg :
        yield txt
       # return txt # return - 함수종료
       # print(txt)

# print(textSequenceFunc)
textSequenceFunc()
# 함수도 iterator로 생성가능
charIter = iter(textSequenceFunc())
print(type(charIter))
print(next(charIter)) # StopIteration 예외발생

'''
yeild - 잠시 함수의 실행을 멈추고 호출한 곳에 값을 전달
- 현재 실행된 상태 계속 유지
-> 다시 해당 함수 호출 시 현재 실행된 상태를 기반으로 다음 코드 실행
'''

# print(textSequenceFunc)
textSequenceFunc() # generator
charIter = iter(textSequenceFunc())
next(charIter)

def userGeneratorFunc(data) :
    for tmp in data :
        yield tmp * 2

twiceList = userGeneratorFunc([1,2,3,4,5])
print(type(twiceList))
# print('next - {}'.format(next(twiceList)))

# 동일해보이지만 개념이 다름!
for t in twiceList :
    print(t)

# Generator Comprehension ()
# (Lazy Operation)
'''
(출력형식 for 요소 in collection)
'''
squareData = (num ** 2 for num in range(5))
print(type(squareData))
print(squareData) # 변수의 값 출력X, 주소번지 출력 -> Lazy Operation
# print(sum(squareData))
for data in squareData :
    print(data, end='\t')

