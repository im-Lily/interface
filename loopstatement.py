# python control statement for looping
# for ~ in range()
# for ~ in list, dict

userSum = 0
for tmp in range(1, 10) :
    print(tmp, end='\t')

userSum = 0
for tmp in range(1, 11, 2) :
    print(tmp)
    userSum += tmp
print('누적 값은 : {}'.format(userSum))

# userList = [1,2,3,4,5]
# list지만 안에 요소가 tuple이기 때문에 변수를 2개로 지정함
userList = [(1,2), (3,4), (5,6)]
for tmp01, tmp02 in userList :
    print(tmp01, tmp02, end='\t')
    userSum += tmp01 + tmp02
print() # 개행
print('누적 값은 : {}'.format(userSum))

# dict.items() 는 키 값으로 받아줌
userDict = {'name' : 'eun', 'gender' : 'f'}
for (key, value) in userDict.items() :
    print('{} : {}'.format(key,value))

scores = [100, 50, 80, 90, 70, 60]
for idx in range(len(scores)) :
    print(idx) # index 출력

# 값을 출력하고 싶다면?
scores = [100, 50, 80, 90, 70, 60]
for idx in range(len(scores)) :
    print(scores[idx])

scores = [100, 50, 80, 90, 70, 60]
for idx in range(len(scores)) :
    userSum = userSum +scores[idx]

print('scores 합 %d' % userSum)

# List Comprehension -> 여러 줄의 코드를 한 줄로 줄일 수 있음 대박적
'''
[ for 구문을 통한 반복적인 표현식 이용가능 ] 
'''

userList = [1,2,3,4,5,6,7,8,9]
useList02 = [tmp ** 2 for tmp in userList]
print(useList02)
# for 앞쪽에 쓰는 것은 결과, 뒤쪽에 쓰는 것은 조건
userList03 = [tmp ** 2 for tmp in userList if tmp % 2 == 0]
print(userList03)

# dict에서도 적용 가능
userDict = {'test'+str(tmp) : tmp ** 2 for tmp in range(1,10)}
print(userDict)




