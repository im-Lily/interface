# python function
'''
함수는 가독성을 높이기 위한 방법으로
하나 이상의 본문을 가지는 코드는 함수로 정의하는 것이 좋다
내장함수 | 사용자정의함수
함수 정의 시 : def 이용
'''

# user difine function
def userPrint() :
    print('userPrint')

# 패키지에 있는 모듈, 함수를 활용하는 방법
# from digital.python import packagefuntionDemo as f
from digital.python.packagefuntionDemo import printCoins
printCoins()

from digital.python import packagefuntionDemo as f

rtnMsg = f.returnFunc()
print(rtnMsg)

echoMsg = f.sayEcho('은경')
print(echoMsg)

domain = f.makeUrl('naver')
print(domain)

# return값이 존재하지 않을경우 호출만 해주면 됨
f.badFunc('eun')

tupRtn = f.tupleFunc(1,2,3,4,5)
print(tupRtn)

f.dictFunc(name='eun', age=25)

(oddSum, evenSum) = f.cntSum(100,500)
print('홀수의 합 {}, 짝수의 합 {}'.format(oddSum,evenSum))

# 인자로 넘겨받은 년도 사이의 윤년을 찾아 리턴
# list type
leapYearList = f.leapYearFunc(1900,2021)
print(leapYearList)

dictMsg = f.rtnDictFunc(10)
print(dictMsg,type(dictMsg))

for value in dictMsg.values() :
    print('dict_values - ', value)

# defalut parameter 사용 - z = True
# worker function
def defalutParam(x, y, z = True) :
    paramSum = x + y
    if paramSum > 10 and z :
    # if paramSum > 10 :
        return paramSum
    else :
        return 0

# caller function
result = defalutParam(10, 20)
print('caller defaultParam() - ', result)

# 함수의 입력인자가 list, dict - mutable(가변)
tmpList = [10]

def mutableFunc(argList) :
    argList.append(100)

mutableFunc(tmpList)
print(tmpList)

# 함수의 입력인자가 숫자, 문자열, tupel - immutable(불변)
tmpList = [10]
tmpX = 10

def mutableFunc(argX, argList) :
    argX += 100 # immutable이기 때문에 조작값 반영x
    argList.append(100)

mutableFunc(tmpX, tmpList)
print(tmpX, tmpList)

# variable(변수) - 선언위치에 따라서 (local, global)
# local 변수가 우선적임
tmp = 100 # global

def myFunc(x) :
    tmp = 0 # 함수안에 동일한 이름의 변수선언, local
    tmp += x
    return tmp

print('call myFunc - ', myFunc(100))

tmp = 100 # global

def myFunc(x) :
    global tmp # global변수 사용
    tmp += x
    return tmp

print('call myFunc - ', myFunc(100))

def personInfo(weight, height, **other) :
    print('weight - ', weight)
    print('height - ', height)
    print('extra - ', other, type(other))

personInfo(80,180,name = 'eun', adress = 'seoul') # dict : key-value형식으로 assign

# * args03 : tuple의 가변인자
# ** args04 : dict의 가변인자
def overroll(args01, args02, *args03, **args04) :
    print(args01, args02, args03, args04)
overroll(10,20,'jeong','eun','kyung',age01=20,age02=30,age=40)

# nested function (중첩함수)
def outerFunc(outernum) :
    def innerFunc(num) :
        print('innerFunc - ', num)
    innerFunc(outernum + 100)

outerFunc(100)

''' 
def outerFunc(num) :
    print('outerFunc - ', num)
    def innerFunc(x) :
        print('innerFunc - ', x)
    innerFunc(num + 100)

outerFunc(100)
'''

# innerFunc(100) - 외부에서 innerFunc 호출불가능

'''
중첩함수 활용 예)
outer 함수 : 자료(data) 생성, inner 함수 포함
inner 함수 : 자료 연산/처리(합계, 평균)
'''

# closuer(클로저)
def calFunc(data) :
    dataset = data
    def sumFunc() :
        total = sum(dataset)
        return total
    def avgFunc(total) :
        avg = total / len(dataset)
        return avg
    return sumFunc, avgFunc # 중첩함수 return 가능
data = list(range(1,101))
print('range data - ', data)
rtnSumFunc, rtnAvgFunc = calFunc(data) # 변수가 함수로 변환가능
tot = rtnSumFunc()
print(tot)
avg = rtnAvgFunc(tot)
print(avg)

'''
재귀함수 (self-recursive function)
- 함수 내부에서 자신의 함수를 반복 호출하는 기법
- 용도 : 반복적으로 변수를 변경해서 연산할 때 (누적, 팩토리얼)
'''

def countFunc(n) : # 5 -> 1,2,3,4,5
    if n == 0 : # 종료조건
        return 0
    else :
        countFunc(n-1) # stack [5,4,3,2,1] -> 반환 시 마지막에 들어온게 가장 먼저나감
        print(n, end = ' ')

countFunc(5) # 1 2 3 4 5
countFunc(0) # 0

# 누적 : (n) =  1 + 2 + 3 + ..... + n
def addSum(n) :
    if n == 1 :
        return 1
    else :
        result = n + addSum(n-1)
        print('n','debug - ', n,result)
        return result
print('n-2 - ', addSum(2))
print('n-100 - ', addSum(100))

# 익명의 함수(lambda 식) 만드는 방법
# 람다식(가독성 향상, 코드 간결, 메모리 절약 - 즉시 실행되는 함수이기 때문)
def multiFunc(x,y) :
    return x * y

print(multiFunc(10,50))

# syntax : lambda arg : body
lambdaVar = lambda x, y : x * y
print(lambdaVar(10,50))

def lambdaFunc(x, y ,func) :
    print('lambdaFunc - ', x * y * func(100,100))
lambdaFunc(10,20,lambda x, y : x * y)
lambdaFunc(10,20,lambdaVar)
lambdaFunc(10,20,multiFunc)

# hint
def totalFunc(word : str, num : int) :
    return len(word) * num
print('hint - ',totalFunc('eun', 20))


