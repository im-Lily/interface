# control statement
# if (조건문), for(반복문), while(반복문)

# input() : 사용자 입력합수 -> return type 문자열

name = input('Enter your name : ')
grade = input('Enter your grade : ')
company = input('Enter your company : ')
print(name, grade, company)

# 홀, 짝 판별 -> if
# if, if ~ else , if ~ elif ~ else, if ~ in
# bool True | False
inputNumber = int(input("Enter your digit(1~100): "))
if inputNumber % 2 == 0 :
    print('짝수')
else :
    print('홀수')

''' 
if 조건문 : 
   pass (아무것도 없을 시 pass 입력해주기)
'''

# 3의 배수인지 5의 배수인지 확인
number = 15
if number % 3 ==0 & number % 5 ==0 :
    print('{}은 3과 5의 배수이다'.format(number))
else :
    print('{}은 3과 5의 배수가 아니다'.format(number))

# if ~ elif
if number % 3 == 0 :
    print('{}은 3의 배수'.format(number))
elif number % 5 == 0 :
    print('{}은 5의 배수'.format(number))
else :
    print('{}은 3과 5의 배수가 아니다'.format(number))

# 윤년의 조건
# 4의 배수 and 100의 배수가 아니거나 or 400의 배수
# if구문을 사용하여 년도와 월을 출력받아 월의 마지막 일 출력

''' 중요함!!
일반적으로 논리연산자는 &&(and), ||(or)가 있음
&, |는 비트연산자로서 값을 이진수로 변환하여 출력해줌
그러나 파이썬에서 &&, ||는 사용할 수 없기 때문에 논리연산자를 사용할 때
꼭 and, or 을 입력해주어야함!!
'''

year = 2020
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('{}는 윤년이다'.format(year))
else :
    print('{}는 윤년이 아니다'.format(year))

# if구문을 사용하여 년도와 월을 입력받아 월의 마지막 일 출력
year = int(input('년도를 입력하세요 :  '))
month = int(input('월을 입력하세요 : '))
if (year % 4 == 0 and year % 100 != 0) | (year % 400 == 0):
    print('{}는 윤년이다'.format(year))
    if (month == 2) :
        print('{}는 29일입니다'.format(month))
    elif (month == 1,3,5,7,8,10,12) :
        print('{}는 31일입니다.'.format(month))
    else :
        print('{}는 30일입니다'.format(month))
else :
    print('{}는 윤년이 아니다'.format(year))
    if (month == 2) :
        print('{}는 28일입니다'.format(month))
    elif (month == 1,3,5,7,8,10,12) :
        print('{}는 31일입니다.'.format(month))
    else :
        print('{}는 30일입니다'.format(month))

# list 를 이용한 if ~ in
area = ['서울', '인천', '대구', '대전', '부산']
region = '수원'
if region in area :
    pass
else :
    print('{} 지역은 포함되지 않음'.format(region))

# dict 를 이용햔 if ~ in
# 딕셔너리는 키를 기준으로 함
areaKeyDict = {'서울' : 100, '광주' : 200}
region = '부산'
if region in areaKeyDict :
    pass
else :
    print('{} 값이 존재하지 않음'.format(region))

# 공백, 비어있는 list, dict일 경우 False로 인식함
city = ""
if city :
    print('true - ', city)
else :
    print('false - ', 'enter your city')

# 삼항 연산자
num = 9
result = 0
result = num * 2 if num > 5 else num + 2
print('삼항 연산자 - ',result)
