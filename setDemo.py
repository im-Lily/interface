# python set type - set(집합) -> 연산가능
# 순서와 중복 X, -> 활용빈도 낮음
# 요소에 대한 추가 가능
# {]
# set([]) - list 형태로 set 생성가능

temp = {'jslim','teacher'}
print('set - ', temp, type(temp))

# 중복이 되지않아 5가 한번만 출력됨
temp = set([1,2,3,4,5,5,5,5])
print('set - ', temp, type(temp))

# 순서없음
temp = set([1,3.14,'Pen',False])
print('set - ', temp, type(temp))
casting = tuple(temp)
print('casting - ', casting, type(casting),casting[0:3])

set01 = set([1,2,3,4,5])
set02 = set([3,4,5,6,7])

# 교집합 & == intersection(), 합집합 | == union(), 차집합 - == difference()
# 객체(변수, 함수)
# 객체.변수, 객체.함수()
print('교집합 & - ', set01 & set02)
print('교집합 intersection - ', set01.intersection(set02))
# set은 중복을 허용하지 않기 때문에 합집합 결과 역시 중복허용X
print('합집합 | - ', set01 | set02)
print('합집합 union - ', set01.union(set02))
print('차집합 - - ', set01 - set02)
print('차집합 difference - ', set01.difference(set02))

# 요소 추가
set01.add(7)
print('set add - ', set01)

# 삭제(remove(), discard())
# set01.remove(9) -> keyError
# remove는 존재하지않는 값을 삭제할 때 오류, discard는 무시함
# discard 사용 지양
set01.discard(9)
set01.remove(4)
print('set remove - ', set01)

# 중복을 허용하지 않기 때문에 중복제거용으로 활용가능
gender = ['f','m','f','m','f', 'm']
setGender = set(gender)
print(setGender, type(setGender))
listGender = list(setGender)
print('list casting - ', listGender, type(listGender))
print('list casting - ', listGender, type(listGender),listGender[0])
