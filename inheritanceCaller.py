'''
from ai.oop.oop_inheritance import Car

car01 = Car('GV70',4,2400)
car01.carInfo()
'''

# 패키지의 모듈에 정의되어 있는 모든 것을 가져옴 *
from ai.oop.oop_inheritance import *

# parent = Parent('부모','공무원')
# print('parent - ', parent)

# child01 = Child01('자식','강사',49)
# child01.childInfo()
# print(child01.display())

stu01 = StudentVO('정은경', 25, 'incheon', '2016')
print('stu Info -', stu01.stuInfo())

tea01 = TeacherVO('임정섭', 49, 'seoul', 'python')
print('tea Info - ', tea01.teaInfo())

emp01 = ManagerV0('장호연', 29, 'seoul', 'HRD')
print('emp Info - ', emp01.empInfo())

userDate = MyDate() # 매개변수 존재하지않음
userDate.year = -2021 # 인스턴스 소유 변수에 직접적으로 접근 -> 이걸 막기 위해서 정보은닉
print(userDate.getYear())

userDate = MyDate() # 매개변수 존재하지않음
userDate.setYear(-2021) # 정보은닉 -> 간접적으로만 접근가능
print(userDate.getYear())
# print(userDate.getYear())

hiding = HidingClass('eun','stu',100)
print('utype - ', hiding.utype)
print('name - ',hiding.name)
# print('dept - ',hiding.__dept)
print('num - ',hiding.num)
print('call getDept - ', hiding.getDept())
print('call __getInfo - ', hiding.__getInfo())

# 다형성
stu01 = StudentVO('정은경', 25, 'incheon', '2016')
tea01 = TeacherVO('임정섭', 49, 'seoul', 'python')
emp01 = ManagerV0('장호연', 29, 'seoul', 'HRD')

perList = []
perList.append(stu01)
perList.append(tea01)
perList.append(emp01)
print('perList - ', perList) # 객체들의 주소값 출력

''' 다형성을 모를 경우 - isinstance(런타임 시 타입확인)
for obj in perList :
    if isinstance(obj, StudentVO) :
        print(obj.stuInfo())
    elif isinstance(obj, TeacherVO) :
        print(obj.teaInfo())
    else :
        print(obj.empInfo())
'''

# 다형성 - 코드 간결화 가능
for obj in perList :
    print(obj.perInfo())

# Account Caller
account = Account('441-2919-1234',500000, 0.073)
account.accountInfo()
account.withDraw(600000)
account.deposit(200000)
account.accountInfo()
account.withDraw(600000)
account.accountInfo()
print('현재 잔액의 이자를 포함한 금액')
account.printInterestRate()

account = FundAccount('441-2919-1234',500000, 0.073,'F')
account.accountInfo()
account.withDraw(600000)
account.deposit(200000)
account.accountInfo()
account.withDraw(600000)
account.accountInfo()
print('현재 잔액의 이자를 포함한 금액')
account.printInterestRate()


