# OT day1
# comment - 주석

'''
변수 : 데이터를 담는 공간
함수 : 행위(업무 로직 및 알고리즘)
클래스
- 변수
- 함수
- 생성자
'''

print('인터페이스 1일차')

'''
변수 : 숫자로 시작x, 특수문자(_,$만 허용)x
변수의 생성 및 삭제
인터프리터 기반의 언어
변수선언 방법
Camel Case : 함수 정의 시 주로 사용
Pascal Case : 클래스 정의 시 주로 사용
Snake Case : 권장하지않음
'''

a=100
print(a)

'''
python data type(Built-in types)
Numeric
Sequence(list, tuple,range)
Text Sequence(str)
Mapping(dict)
Set(set)
Bool(True(T), False(F), not, and, or (논리), &,|,~ (비교))
'''

# 허용하는 변수 선언법
# 예약어는 변수명으로 사용불가
""" 예약어
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass	
"""

year = 2021
month = 1
day = 4

print(year, month, day)

str = 'python start!'
print(type(str))

str = "eun's python"
print(str)

print('p','y','t','h','o', 'n')
print('p','y','t','h','o', 'n',sep="") # 공백제외
print('python', 'google.com',sep='@')
print('naver','kakao','samsung',sep='/')

"""
참고 : Escape 코드
\n : 개행
\t : 탭 
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자
...
"""

# end 옵션(print / println 차이점)
print('Welcome To',end=' ')
print('IT News',end=' ')
print('Web Sites')

# format 사용법(d, s, f)
one = 1
two = 2
print(one,two)
print('%d %d' % (one, two))

one = '1'
two = '2'
print(one,two)
print('%s %s' % (one, two)) # 자릿수 제한할 때 사용

# 여러 개의 변수로 하나의 문장을 만들 때 사용
print('{} {}'.format(one,two)) # type을 지정하지 않아도됨

# format은 자릿수 지정이 가능함
print('%10s' % ('nice',)) # 총 자릿수=10, 오른쪽에서부터 자릿수를 채움
print('%-10s' % ('nice',)) # 총 자릿수=10, 왼쪽에서부터 자릿수를 채움
print('%1.8f' % (3.14159809877)) # 정수 1자리, 실수 8자리
# 0th부터 1.8f형태로 출력
print('{:1.8f}'.format(3.14159809987)) # {}안에는 인덱스가 들어가야함




