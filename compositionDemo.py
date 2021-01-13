'''
학습목표
- Compositon == Aggregation
-> 상속을 회피하고 클래스의 일부 기능을 그대로 활용하고 싶을 때 사용
-> 상속관계가 복잡할 경우 코드 이해 어려움
-> 컴포지션은 명시적 선언, 상속은 묵시적 선언
- Exception
- File 입출력
'''

# Compositon 상속, 오버라이딩과 전혀 다른 개념임!
class Calc01(object) :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def substract(self):
        return self.x - self.y

class Calc02(object) :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def multiply(self):
        return self.x * self.y

class UserCalc :
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cal02 = Calc02(x,y) # 해당 클래스의 객체 생성
    def add(self):
        return self.x + self.y
    def substract(self):
        return self.x - self.y
    def multiply(self): # Calc02의 메서드를 그대로 사용
        return self.cal02.multiply()

clac = UserCalc(3,4)
print('clac multiply - ', clac.multiply())

'''
- 예외(Exception) - SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError ,,, 
- 예외 처리가능한 구문이해
try :
    에러가 발생할 가능성이 있는 코드
    정상코드
    에러가 발생할 가능성이 있는 코드
    정상코드
except xxxError :
    1. 프로그램의 흐름을 정상으로 컨트롤 -> 운영단계
    2. 예외발생에 대한 디버깅 -> 개발단계
    3. 로그파일 생성하여 예외정보 저장 -> 개발단계
except xxxError :
    각각의 에러를 잡기위한 객체정의(에러발생개수와 동일하게)
else :
    에러가 발생되지 않을 때 실행되는 블럭
finally :
    에러발생과 상관없이 항상 수행
'''

# 여러가지 에러발생
# print('error)
# a = 10
# b= 20
# print(c)
# print(100/0)
# x = [1,2,3]
# print(x[3])
# dict = {'name' : 'eun', 'age' : 25, 'city' : 'incheon'}
# print(dict['hobby'])
# print(dict.get('age'))

# 예외가 없는것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외처리 권장
# import time
# print(time.time2())

# 다중 except를 사용하지 않을경우 Exception 사용 -> 모든 예외처리 가능
def userKeyIn() :
    try :
        age = int(input('나이를 입력하세요 :')) # 예외발생구문
    except Exception :
        # print('error - ', e)
        print('문자열이 아닌 정수를 입력하세요')
        userKeyIn() # 재호출
    else :
        print('age - ', age)
        print('함수실행 종료')
    finally :
        print('난 항상 실행돼')

userKeyIn()

nameList = ['kim', 'lee', 'park', 'lim']
try :
    name = 'cho'
    idx = nameList.index(name)
except Exception :
    print('{} not found it'.format(name))
else :
    print('{} found it'.format(name, idx + 1))
finally :
    print('예외 여부와 상관없이 항상 실행')
print('프로그램 종료')

# 클래스에 정의된 함수에 예외처리 적용 및 강제 예외 발생(raise)
class Account :
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate
    def withDraw(self, amount):
        try : # 예외 발생 구문
            if self.balance < amount :
                raise Exception # 임의적으로 예외발생
        except Exception : # 예외처리
            print('잔액부족')
        else :
            self.balance -= amount

account = Account('100', 100000, 0.073)
account.withDraw(200000)
print('프로그램 종료')

# 사용자 정의 예외 클래스 작성 -> Exception 상속
class InsufficientError(Exception) :
    def __init__(self, msg):
        self.msg = msg

class Account :
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate
    def withDraw(self, amount):
        try :
            if self.balance < amount :
                raise InsufficientError('잔액부족')
        except Exception as e :
            print(str(e))
        else :
            self.balance -= amount

    def withDraw02(self, amount):
        if self.balance < amount :
            raise InsufficientError('잔액부족')
        else :
            self.balance -= amount

account = Account('100', 100000, 0.073)
try :
    account.withDraw02(200000)
except InsufficientError as e :
    print(str(e))
print('프로그램 종료')

'''
객체생성 - 클래스(인스턴스 소유의 변수와 함수)
클래스없이 객체를 생성하는 방법(변수)
usage)
collections.namedtuple('실제 클래스 이름', (변수) [변수])
'''
import collections

# Person = collections.namedtuple('Person', ['name','id']) # 클래스처럼 보이지않지만 클래스임
# Person = collections.namedtuple('Person', 'name id') # tuple
Person = collections.namedtuple('Person', 'name, id') # string
per = Person('eun', 100)
print(per,type(per))

# 속성에 접근 -> 인덱스로 접근
print('idx 0 -', per[0])
print('idx 1 -', per[1])

for idx in range(len(per)) :
    print('idx {} - {}'.format(idx, per[idx]))

# 속성에 접근 2 -> 직접 접근
print(per.name)
print(per.id)

# 속성에 접근 3
name, id = per
print(name, id)

'''
1. 직장인 이름, 나이, 부서를 속성으로 갖는 클래스 생성
2. 직장인 이름, 나이, 부서를 속성으로 갖는 클래스를 namedTuple로 생성 
'''
class Emp :
    def __init__(self, name, age, dept):
        self.name = name
        self.age = age
        self.dept = dept

Emp = collections.namedtuple('Emp', ['name','age','dept'])
emp = Emp('eun','age','edu')
print(emp,type(emp))
print(emp.name, emp.age, emp.dept)

