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
