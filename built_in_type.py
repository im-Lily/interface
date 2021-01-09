# 변수 정의 및 생성
# 블럭단위 실행 단축키 (shift + alt + e)

intValue = 123
floatValue = 3.14
boolValue = True
strValue = 'jslim'
print()
print(type(intValue),type(floatValue),type(boolValue),type(strValue))

# type casting
numStr = "720"
numNum = 100
print(int(numStr) + numNum) # 정수형의 결합
print(numStr + str(numNum)) # 문자열의 결합

year = "2021"
print(int(year) - 1)

# list
listAry = ['python', 'anaconda']
print(type(listAry))

# dict {} : key-value
dictValue = {
    "neme" : "machine Learning",
    'version' : 2.0
}
print(type(dictValue), dictValue)

# tupel ()
# 요소의 값이 하나일 경우 , 꼭 해주기!!
tupleValue = (3)
print(type(tupleValue))

tupleValue = (3,)
print(type(tupleValue))

# set {} : value -> 중복x, 순서x
setValue = {3,5,7}
print(type(setValue))

# input () : 기본적으로 문자열로 리턴
inputNumber = input('숫자를 입력하세요 : ')
print(type(inputNumber))
print(inputNumber)

''' 오류 : int + str X
inputNumber = input('숫자를 입력하세요 : ')
sum = 100 + inputNumber
print(sum)
'''

inputNumber = tin(input('숫자를 입력하세요 : '))
sum = 100 + inputNumber
print(sum)

# 문자형(str) - Text Sequence 중요해!
str01 = 'I am python'
str02 = "python"

# 개행이 이루어지는 문장
str03 = '''this is a
multiline
sample text'''
str04 = """this is a
multiline
sample text"""

# seqText는 연속되며 인덱싱이 가능하고 슬라이싱이 가능함
seqText = 'Talk is cheap. Show me the code'
print(seqText, type(seqText))
print(seqText[0:4])
print(seqText.split(' '))

# dir() - 사용가능한 내장함수 출력
# iter : 순환반복 내장함수
print(dir(seqText))

# indexing
print(seqText[3])
print(seqText[-1])

# slicing
# 문자열에 대해서도 슬라이싱 가능함
# 인덱싱과 다르게 슬라이싱은 범위를 지정해줘야함
print(seqText[0:4])
print(seqText[-6:])
print(seqText[ : : 2])
print(seqText[ : : -1])

# 아래의 문자열에서 '홀'만 출력하세요
string = "홀짝홀짝홀짝홀짝"
print(string[ : : 2])
print(string[ : : -1])

# 문자열 조작을 위한 많은 내장함수 제공
# 단어의 앞글자 대문자로 변경
string = "python"
print("Capitalize : " , string.capitalize())

# 문자치환 replace(oldchar, newchar)
phoneNumber = '010-1234-5678'
replacePhoneNumber = phoneNumber.replace('-'," ")
print(replacePhoneNumber)

string = 'abcdef2a34a5634a'
print(string.replace('a','A'))

# 문자열 쪼개는 함수 : split()
# 아래 문자열에서 도메인만 출력
url = "http://www.naver.com"
# . 을 기준으로 문자열이 쪼개짐
urlSplit = url.split('.')
# return 형식은 list
print(urlSplit,type(urlSplit))
# list 형식이기 때문에 인덱싱이 가능함
print('domain : ', urlSplit[-1])

# 문자열에서 공백 제거 함수 : strip(), rstrip(), lstrip()
companyName = '    samsung    '
print(companyName, len(companyName))
print(companyName.strip(), len(companyName.strip()))
print(companyName.rstrip(), len(companyName.rstrip()))
print(companyName.lstrip(), len(companyName.lstrip()))

# 대문자, 소문자 변환함수 : upper(), lower()
print(companyName.upper())

# endswith() : 문자열이 특정문자로 끝나는지 확인
# retrun type = bool
fileName = 'reprot.xls'
isExits = fileName.endswith(('xls', 'xlsx', 'csv'))
print(isExits, type(isExits))

# in, not in -> True | False
# 파이썬은 대소문자 구별함
myStr = "This is a sample Text"
print("Sample" in myStr)
print('text' not in myStr)
print("this" in myStr.lower())

# 문자의 빈도 count(), 문자 찾기 find(), 문자의 인덱스 index()
brandName = 'cocacola'
print(len(brandName), brandName.count('c'),brandName.count('a'))


