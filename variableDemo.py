# Numeric(숫자, 정수, 실수)
a = 123
b = 3.14
c = 3.14E10

# e = 0o34 -> 8진수
# f =0xAB -> 16진수

# type() : 데이터 형태 파악
print(type(a))
print(type(b))
print(type(c))

div = 3/4
print(div)

result = 3 ** 3
print(result)

# 나머지
result = 10 % 3
print(result)

# 몫
result = 10 // 3
print(result)

# Sequence - list
# 임의의 값을 순서대로 저장하는 집합 자료형(index 부여 및 값 변경 가능한 형식)
# 리스트 생성방법 : 함수 이용 / [] 이용
# range() 함수 이용하여 리스트 생성

a = []
print(type(a))

a = list()
print(type(a))

a = [1, 2, 3]
print(a)

# Indexing
print(a[0])
print(a[1])
print(a[2])
print(a[-1])

# slicing
print('slicing')
print(a[1:2])
print(a[0:2])

a = [1, 2, 'hello', 3.14]
print(a)
a = [1, 2, ['show', 'me', 'the', 'money'], 3.14]
print(a[2])
print(a[2][2:])
print(type(a[2][2:]))

a = [1, 2, 3]
b = [4, 5, 6]
# 데이터 타입 : 리스트임!
print(a + b) # merge
print(a * 3) # 3번 반복

print(a)

a[0] = 5 # 값 변경
print(a)

# tuple () => 중요해

a = ()
print(type(a))

a = tuple()
print(type(a))

# tuple의 요소가 하나일 경우 int로 인식함
a = (1)
print(type(a))

# 따라서 뒤에 ,를 써야함
a = (1,)
print(type(a))

a = (1, 2, 3)
print(type(a))
print(a[0]) # 튜플도 리스트처럼 인덱싱과 슬라이싱이 가능함

a = ()
print(type(a))

# type casting -> tuple을 list로 변경
a = list(a)
print(type(a))