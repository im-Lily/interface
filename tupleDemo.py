# python sequence type - tuple
# 순서와 중복이 있음, 수정, 삭제 불가능
# list VS tuple
# 읽기 전용 (immutable)
# tuple()
# indexcing, slicing 가능

myTuple = ('반도', '강철비', '아이언맨')
oneTuple = (1,)

# 사용자의 편의를 위해 괄호없이 튜플선언 가능
myTuple = 1,2,3,4,5
print(type(myTuple))

multiTuple = (100, 1000, 'Ace', 'Base', 'Captine')
# indexing
print(multiTuple[1])
print(multiTuple[2:],type(multiTuple)) # tuple로 return

# casting : tuple <-> list
# 튜플은 수정과 삭제가 안되기 때문에 리스트로 변경 후 해줘야함
multiList = list(multiTuple[2:])
castingMultiTuple = tuple(multiList)

# python sequence type - range
range01 = range(10)
print(range01)

range02 = range(1,11,2)
print(range02)
print(7 in range02)
print(10 in range02)
print(range02.index(7)) # 7의 index 출력
print(range02[2]) # 2th 값 출력
print(range02[2:])
print(range02[-1])

# 시작값 : 2, 끝값 : 100-1=99, step size : 2
# 1 ~ 99까지의 정수 중 짝수만 저장된 튜플 생성
even = tuple(range(2,100,2))
print(even)
# even[0] = 1 -> 수정, 삭제 불가능







