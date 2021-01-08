# python 객체지향 프로그래밍 (oop)
'''
패키지(package) > 모듈(module) > 클래스(class) > 함수(function)
Object Oriented Programming (OOP)
'''

# class를 이용해서 한 학생의 데이터를 논리적인 하나의 단위로 묶어서 사용
'''
class VS instance
namespace : 객체를 인스턴스화할 때 저장되는 공간
class variable : 직접 접근간으 및 공유
instance variable : 객체소유로 별도 존재
self - instance 소유의 멤버라는 것을 명시함

class 
- 함수의 모임
- 역할 : 여러 개의 함수와 데이터를 묶어서 객체를 생성할 수 있는 템플릿
- 구성 : 멤버 - 변수(데이터) + 메서드(함수), 생성자(초기화)
'''

class Calc :
    x = 0
    y = 0

    def __init__(self):
        print('객체 생성시 호출되는 초기화함수임')

    def plus(self):
        print('사용자정의함수, 인스턴스의 소유임')

# instance 생성하는 문법
obj = Calc() # init이 호출됨
obj.plus() # 사용자정의함수가 호출됨

'''
user define function
- setXXXX (바인드)
- getXXXX (리턴)
- isXXXX (True/False)
'''

class Student :

    def __init__(self, name, major, num, grade):
        self.name = name # 무조건 인스턴스의 소유임!
        self.major = major
        self.num = num
        self.grade = grade

    def __repr__(self): # 주소대신 입력한 문자 출력
        return self.name + '\t' +self.num

    def getInfo(self): # repr 함수와 비슷한 역할
        return '이름 : {} \t 전공 : {}'.format(self.name,self.major)

stu01 = Student('은갱','통계','2016','A') # 4개의 인자값이 있어야함
print(stu01.name)
print('stu01 adress -', stu01) # repr 함수 호출

stuList = []
stuList.append((Student('홍길동','철학', '2016', 4.5)))
stuList.append((Student('뽀로로','철학', '2016', 4.5)))
for stu in stuList :
    print(stu.getInfo())

# 인스턴스 소유의 변수가 아닌 클래스 소유의 변수
# namespace (instance -> class -> super class)
class Student :

    scholarshipRate = 3.5 # self가 붙지않아 클래스 소유임!

    def __init__(self, name, major, num, grade):
        self.name = name # 무조건 인스턴스의 소유임!
        self.major = major
        self.num = num
        self.grade = grade

    def __repr__(self): # 주소대신 입력한 문자 출력
        return self.name + '\t' +self.num

    def getInfo(self): # repr 함수와 비슷한 역할
        return '이름 : {} \t 전공 : {}'.format(self.name,self.major)

    def isSch(self):
        if self.grade >= Student.scholarshipRate : # 클래스 소유의 변수는 클래스변수로 접근해야함!
            return True
        else :
            return False

stu01 = Student('eun','stat',2016,4.5)
print('장학금 여부 - ',stu01.isSch(),Student.scholarshipRate)

# 인스턴스 소유가 아닌  class method
'''
self X
클래스 함수 : cls인 인자를 받고 모든 인스턴스가 공유하는 클래스 변수와
같은 데이터를 생성, 변경 또는 참조하기 위해 사용됨
'''

class Employee :

    raiseRate = 1.1 # 급여인상률 class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return '현재 {}님의 급여는 {}입니다'.format(self.name,self.salary)

    @classmethod
    def updateRate(cls, rate):
        cls.raiseRate = rate
        print('인상률이 {}로 변경되었음'.format(rate))

    def applyRaise(self):
        self.salary = int(self.salary * Employee.raiseRate)

''' # static 함수
    @staticmethod
    def isValid(salary):
        if salary < 0 :
            print('음수가 될 수 없음')
'''

emp01 = Employee('eun', 1000) # 인스턴스 소유
print('인상 전 급여 - ', emp01.getSalary())

Employee.updateRate(1.5) # 클래스 소유
emp01.applyRaise()
print('인상 후 급여 - ', emp01.getSalary())
Employee.isValid()
