# python sequence type - list
# 자료구조에서 중요해!
# 파이썬에서는 배열이 존재하지않음
# 리스트는 1차원 자료구조임 / R에서는 vector
# 순서(index 부여 0부터 시작), 중복 존재, 수정, 삭제 가능
# [] 이용하여 변수선언 가능

a = list()
a = []

a = [1,2,3]
print(a,type(a))
print(a[0])
a[0] = 5
print(a[0])

# 요소 추가하는 함수 : append(), insert()
a.append(4)
print(a)

# insert : 특정 위치에 요소 추가
a.insert(0,6)
print(a)
a.sort()
print(a)
a.reverse()
print(a)

# pop() : 기존 리스트에서 요소를 가져오고 삭제 - 조심해!
# 마지막에 위치한 요소를 제거하고 출력해줌
print("a - pop() : ", a.pop())
print("a - print : ", a)

# extend() / append() 차이 구분하기!
ex = [4,3]
a.append(ex)
print('a - applend : ', a) # 리스트형태로 추가됨

ex = [4,3]
a.extend(ex)
print('a - applend : ', a) # 값으로 추가됨

movieRank = ['원더우먼', '해리포터', '겨울왕국2', '가타카', '국제수사', '반도']

# 1. 해당리스트에 '배트맨  추가
movieRank.append('배트맨')
print(movieRank)
''' 
# extend는 요소들을 추가하기 때문에 append와 출력결과가 상이함
movieRank.extend('배트맨')
print(movieRank)
'''

# 2. 원더우먼과 해피포터 사이에 '씽' 추가
movieRank.insert(1,'씽')
print(movieRank)

# 3. '반도' 삭제
'''
# pop은 마지막 요소에서부터 차례대로 삭제, 인덱스 부여해서 삭제가능
movieRank.pop()
print(movieRank)
'''
movieRank.remove('반도')
print(movieRank)

# 최댓값, 최솟값, 총합, 평균
scoreData = [1,2,3,4,5,6,7]
print("max" , max(scoreData))
print("min" , min(scoreData))
print("sum", int(sum(scoreData)))
print("mean", int(sum(scoreData)) / len(scoreData))










