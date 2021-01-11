'''
oop
- 상속(is ~ a)
- 다형성
- 은닉화
- 추상화
lib(has ~ a), (is ~ a)
'''

''' 파이썬에서 생성자는 한번만! / 그렇지않을 경우 TypeError
class Car :
    def __init__(self):
        pass
    def __init__(self,name,door,cc):
        self.name = name
        self.door = door
        self.cc = cc

car01 = Car() # Car의 생성자 호출
# car01.함수
# car01.변수
'''

class Car :
    def __init__(self,name,door,cc):
        self.name = name
        self.door = door
        self.cc = cc
    def carInfo(self):
        print('%s 는 %d cc이고, 문짝은 %d 개입니다' % (self.name, self.cc, self.door))

# car01 = Car('GV70',4,2400)
# car01.carInfo()

'''
object : 부모클래스, Sup가 object를 상속받음
object < Sup < Sub
class Sup(object) :
    pass
class Sub(Sup) :
    pass
'''

# 상속 후 부모에 대한 객체생성은 의미가 없음
# 부모의 구성요소를 자식이 포함하고 있기때문!
class Parent(object) :
    # 초기화함수, 생성자
    def __init__(self, name, job):
        self.name = name
        self.job = job
    # repr 함수와 동일
    def display(self):
        return '당신의 이름은 {} 이고 직업은 {} 이다'.format(self.name,self.job)

class Child01(Parent) :
    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age
    def childInfo(self):
        print('당신의 이름은 {} 이고 직업은 {} 이며 나이는 {}입니다'.format(self.name,self.job,self.age))

class child02(Parent) :
    pass

# 상속과 다형성
class Person(object) :
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def perInfo(self):
        return self.name + '\t' + str(self.age) + '\t' + self.address

# super() : 부모의 생성자 호출
class StudentVO(Person) :
    def __init__(self, name, age, address, stuId):
        super().__init__(name, age, address)
        self.stuId = stuId
    def stuInfo(self):
        return super().perInfo() + '\t' + self.stuId
    def perInfo(self):
        return super().perInfo() + '\t' + self.stuId

class TeacherVO(Person) :
    def __init__(self, name, age, address, subject):
        super().__init__(name, age, address)
        self.subject = subject
    def teaInfo(self):
        return super().perInfo() + '\t' + self.subject
    def perInfo(self):
        return super().perInfo() + '\t' + self.subject

class ManagerV0(Person) :
    def __init__(self, name, age, address, dept):
        super().__init__(name, age, address)
        self.dept = dept
    def empInfo(self):
        return super().perInfo() + '\t' + self.dept
    def perInfo(self):
        return super().perInfo() + '\t' + self.dept

# encapsulation(은닉화)
# information hiding(정보은닉)
# 초기화 함수를 지정하지 않으면 매개변수가 없는 클래스임
class MyDate(object) :
    def setYear(self, year):
        if year < 0 :
        # __변수 : 정보은닉(숨겨짐) -> 외부에서 변수에 대한 접근불가능
            self.__year = 2021
        else :
            self.__year = year

    def getYear(self):
        return self.__year

'''
public vs private
instance variable - public 변경 private ? __instance variable
instance function - public 변경 private ? __instance function
'''

class HidingClass(object) :
    def __init__(self, name, dept, num):
        self.utype = self.__class__.__name__ # type check
        self.name = name
        self.__dept = dept
        self.num = num

    def getDept(self):
        return self.__dept

    def __getInfo(self):
        return '__로 시작했기 때문에 해당 함수는 외부에서 접근불가능'

'''
다형성
상위 클래스에 정의된 함수를 하위 클래스에서 해당 함수 재정의(method overriding)
'''

# [실습]
# 1. Account class 작성 - account, balance, interestRate
# 2. accountInfo() - 계좌의 정보를 출력한다(account, balance, interestRate)
# 3. deposit(amount) - 계좌 잔액에 매개변수로 들어온 amount를 누적한다.
# 4. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 자리 2자리까지 출력한다.
# 5. withDraw(amount) - 매개변수로 들어온 금액만큼을 출금하여 잔액을 변경한다.
# 단) 잔고가 부족할 경우 '잔액이 부족하여 출금할 수 없습니다' 출력한다.

class Account(object) :
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate
    def accountInfo(self):
        print('계좌번호 {}, 현재잔액 {}'.format(self.account,self.balance))
    def deposit(self, amount):
        self.balance += amount
    def printInterestRate(self):
        print('%2f' % float(self.balance + (self.balance * self.interestRate)))
    def withDraw(self, amount):
        if self.balance < amount :
            print('잔액이 부족하여 출금 불가능')
        else:
            self.balance -= amount

# [실습]
# 1. Account class 작성 - account, balance, interestRate, type(계좌 종류 S|F)
# 1-1. SavingAccount , FundAccount 추가 (상속)
# 1-2.  |                       |
# 1.3.  -- printInterestRate()  -- printInterestRate() (overridding)
# 1.4  SavingAccount - printInterestRate()
#      기본 이자율에 만기시 이자율을(0.1) 복리로 계산
# 1.5  FundAccount - printInterestRate()
#      기본 이자율에 잔액 10만원 이상이며 10%
#      기본 이자율에 잔액 50만원 이상이며 15%
#      기본 이자율에 잔액 100만원 이상이며 20%
# 2. accountInfo() - 계좌의 정보를 출력한다(account, balance, interestRate)
# 3. deposit(amount) - 계좌 잔액에 매개변수로 들어온 amount를 누적한다.
# 4. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 자리 2자리까지 출력한다.
# 5. withDraw(amount) - 매개변수로 들어온 금액만큼을 출금하여 잔액을 변경한다.
# 단) 잔고가 부족할 경우 '잔액이 부족하여 출금할 수 없습니다' 출력한다.

class Account(object) :
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate
    def accountInfo(self):
        print('계좌번호 {}, 현재잔액 {}'.format(self.account,self.balance))
    def deposit(self, amount):
        self.balance += amount
    def printInterestRate(self):
        print('%2f' % float(self.balance + (self.balance * self.interestRate)))
    def withDraw(self, amount):
        if self.balance < amount :
            print('잔액이 부족하여 출금 불가능')
        else:
            self.balance -= amount

class SavingAccount(Account) :
    def __init__(self, account, balance, interestRate, type):
        super().__init__(account, balance, interestRate)
        self.type = type
    def printInterestRate(self):
        self.balance += self.interestRate * 0.1

class FundAccount(Account):
    def __init__(self, account, balance, interrestRate, type):
        super().__init__(account, balance, interrestRate)
        self.type = type
    def printInterestRate(self):
        if 0 < self.balance < 100000 :
            self.balance += self.interestRate
            print(self.balance)
        elif self.balance < 500000 :
            self.balance += self.interestRate * 0.1
            print(self.balance)
        elif self.balance < 1000000 :
            self.balance += self.interestRate * 0.2
            print(self.balance)
