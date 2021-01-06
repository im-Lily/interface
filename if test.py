# no.1
num = int(input('값을 입력하세요(0 ~ 255) : '))
if num < 0 :
    print(0)
elif num > 255 :
    print(255)
else :
    print(num)

# no.2
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
userHour =

# no.3
fruit_list = ['사과','포도','홍시']
fruit = input('과일을 입력하세요 : ')
if fruit in fruit_list :
    print('정답')
else :
    print('오답')

# no.4
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
investment = input('투자 종목을 입력하세요 : ')
if investment in warn_investment_list :
    print('투자 경고 종목임')
else :
    print('투자 경고 종목아님')

# no.5
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season = input('계절을 입력하세요 : ')
if season in fruit :
    print('정답')
else :
    print('오답')

# no.6
alpha = input('문자 한 개를 입력하세요 : ')
if alpha.islower() :
    print(alpha.upper())
else :
    print(alpha.lower())

# no.7
score = int(input('학점을 입력하세요 : '))

