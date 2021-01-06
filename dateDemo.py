# python date type

from datetime import date, datetime, timedelta


today = date.today()
print('date - ', type(today), today, today.year, today.month, today.day)
print('년도 {}, 월 {}, 일 {}'.format(today.year, today.month, today.day))

# 시간
todayDateTime = datetime.today()
print('datetime - ', todayDateTime)
print('시 {}, 분 {}, 초 {}'.format(todayDateTime.hour,todayDateTime.minute,todayDateTime.second))

# install dateutil
from dateutil.relativedelta import relativedelta

# 날짜 형식에 대하여 연산불가능 -> dateutil 사용하면 연산가능
today = date.today()
days = timedelta(days = -1)
print(' 어제 - {}'.format(today+days))

# year, month 관련된 옵션을 필요로 한다면 relativedelta 이용
days = relativedelta(months=-2)
print(' 2달 전 오늘 - {}'.format(today+days))

days = relativedelta(years=-2)
print(' 2년 전 오늘 - {}'.format(today+days))

from dateutil.parser import parse

# parse 함수이용
# 문자열 -> 날짜형식으로 변환
userDate = parse('2021-06-04')
print('parser date - ', userDate,type(userDate))

userDate = datetime(2021,12,25)
print('dattime date - ', userDate,type(userDate))

# 날짜 객체의 출력형식 원하는대로 변경
today = datetime.tdoay()
# 날짜 -> 문자열로 변환 strftime()
print("{}".format(today.strftime('%m-%d-%y')))
print("{}".format(today.strftime('%m-%d-%Y')))

# 문자 -> 날짜 strptime()
strDate = '2021,01,06-11:12:40'
userDate = datetime.strptime(strDate,'%Y,%m,%d-%H:%M:%S')
print(type(userDate),userDate)

