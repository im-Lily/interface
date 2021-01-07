# python control statement for looping
# for ~ in range()
# for ~ in list, dict
# for ~ in enumerate(list)

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

# 단어의 빈도수 구하기
wordVec = ['love', 'word', 'cat','love', 'word', 'cat']
print(len(wordVec)) # list의 개수 = 요소의 개수

# get() : 해당 key의 value값 호출함수
wordCnt = {}
for word in wordVec :
    wordCnt[word] = wordCnt.get(word, 0) + 1
print(wordCnt)

# 엥
wordCnt02 = {}
for word in wordVec :
    if word in wordCnt02 :
        wordCnt[word] += 1
    else :
        wordCnt02[word] = 1
print(wordCnt02)

# 1 ~ 1000 합 구하기
rangeSum = 0
for value in range(1,1001) :
    rangeSum += value
print('1 ~ 1000 합 %d 이다.' %(rangeSum))

# 2000 ~ 2050년까지 올림픽 개최년도 출력하기
# 단, 한 줄에 5개 년도 출력하고 개행
cnt = 0
for year in range(2000,2051,4) :
    cnt += 1
    print(year,end='\t')
    if cnt % 5 == 0 :
        print()

# 아래 리스트에서 세 글자 이상의 단어만 출력
wordList = ['I', 'am', 'study', 'python', 'language']
for word01 in wordList :
    if len(word01) >= 3 :
        print(word01, end = '\t')

# list comprehension
word001 = [word01 for word01 in wordList if len(word01) >=3]
print(word001)

wordList = ['I', 'am', 'study', 'PYTHON', 'language','IF','for']
for word02 in wordList :
    if word02.isupper() :
        print(word02)

wordList02 = ['dog','cat','pig','carrot', 'horse']
for word03 in wordList02 :
    print(word03.capitalize())

# 해당 파일의 확장자를 제거하고 파일 이름만 출력
# split : 문자열에서 사용, return 형식은 list
fileList = ['gretting.py','bool.py','intro.hwp', 'ai.doc']
for file in fileList :
    print(file,file.split('.')[0])

# 문자열은 문자로 토큰이 가능한 시퀀스타입
# 문자 1글자씩 출력가능
# looping 가능
word04 = 'HandSome Boy'
for w in word04 :
    if w.isupper() :
    print(w, end=',')

# 주어진 문장에서 모든 문자를 대문자로 출력
dumySen = 'FasdfAlsjdlkjfowDjoskjfdlkjsdvndkDkjsld'
print(dumySen.upper())

# 소문자 -> 대문자로 변환하여 전체문장을 대문자로 출력
for w in dumySen :
    if w.islower() :
        print(w.upper(), end = '')
    else :
        print(w, end = '')

# [::-1] 마지막 부분은 step을 의미하는데 -1 step으로 가져오겠다는 뜻
wordList03 = ['가', '나', '다', '라']
for word05 in wordList03[::-1] :
    print(word05)

# break, continue
# search =17
search = 17
numbers = [14,3,4,7,10,24,17,2,33,34,36,38]
for num in numbers :
    if num == search :
        continue
        print('Found - ', num)
       # break
    else :
        print('Not Found - ', num)

# for ~ else : 전체 구문을 돌면서 조건을 충족하지 못할 경우 else 구문 실행
# 조건을 충족하여 break문 실행한다면 else 구문 실행x
search = 5
numbers = [14,3,4,7,10,24,17,2,33,34,36,38]
for num in numbers :
    if num == search :
        print('Found - ', num)
        break
else :
    print('Not Found - ', search)

for i in range(1,6) :
    for j in range(1,4) :
        print('i - {}, j - {}'.format(i,j))

for i in range(2, 10) :
    for j in range(1, 10) :
        print('{} * {} = {}'.format(i,j,(i*j)),end='\t')
    print()
    if i == 5 :
        break

# 리스트에 요소 추가함수
# append() : 마지막 인덱스에 추가,
# insert(), extend() : 특정 위체에 요소 추가

string = '''나는 지금 파이썬 강의를 듣고있다
하루빨리 대면강의를 하고싶다
소문으로 밥이 맛있다고 들었다
동기들도 보고싶다~,,'''

sentences = []
words = []

for s in string.split('\n') :
    sentences.append(s)
    for w in s.split() :
        words.append(w)
print(sentences, len(sentences))
print(words, len(words))

# 분류정확도
answer = [1,0,2,1,0]
predict = [1,0,2,0,0]
acc = 0
for idx in range(len(answer)) :
    fit = answer[idx] == predict[idx]
   # print(int(fit), end = '\t')
    acc += int(fit) * 20
print('classification accuracy - ', acc)

'''
enumerate : 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때
인덱스 번호와 컬렉션 요소를 확인가능
'''

bookList = ['SQL','R', 'TEXT-MINING', 'NLP','DATA-MINING','DJANGO']
for idx, book in enumerate(bookList) :
    print('index - {}, value - {}'.format(idx,book))

'''
for와 다르게 while 구문안에 증감식이 있어야함
while <expression> :
    statement
    증감식 -> 존재하지 않으면 무한루프 발생
'''

cnt = 5
while cnt > 0 :
    print(cnt)
    cnt -= 1
    print('cnt - ', cnt)

# list - pop()
whileList = ['foo','bar','baz']
while whileList : # 비어있지않은 list -> True
    print(whileList.pop())
    print('whileList - ', whileList)
print('while - end')

# 난수를 발생시켜 횟수내에 맞추는 게임
import random # 모듈

ran = random.random() # 0 ~ 1 사이의 실수형 난수발생
print(ran)

ran = random.randint(0,2) # 정수형 난수발생
print(ran)

'''
숫자 범위 : 1 ~ 10
내가 입력한 숫자 > 난수 : 더 작은 수 입력
내가 입력한 숫자 < 난수 : 더 큰 수 입력
'''

randNum = random.randint(1,10)
while True :
    userNum = int(input('숫자를 입력하세요(1 ~ 10) : '))
    if randNum == userNum :
        print('success')
        break
    elif randNum > userNum :
        print('더 큰 수를 입력하세요 : ')
    else :
        print('더 작은 수를 입력하세요 : ')

'''
1 ~ 100 사이의 난수발생
도전횟수는 20회로 제한
출력 결과는 (정답 시도횟수, 정답) 
'''

from random import randint
randNum02 = random.randint(1,100)
tries = 1
while tries <= 20 :
    userNum02 = int(input('숫자를 입력하세요 : '))
    if randNum02 == userNum02 :
        print('정답')
        break
    elif randNum02 > userNum02 :
        print('더 큰 수를 입력하세요 : ')
    else :
        print('더 작은 수를 입력하세요 : ')
    i += 1
if randNum02 == userNum02 :
    print('시도 횟수 {}, 정답 {}'.format(i,userNum02))
else :
    print('정답 {}'.format(randNum02))

# random choice()
dataset = list(range(1, 10001))
print(dataset)

# 모집단 dataset에서 k개의 데이터 샘플링
train = random.choices(dataset, k = 10)
print('sample dataset - ', train)




