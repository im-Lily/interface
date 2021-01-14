'''
binary 형식의 입출력
- 객체직렬화(Seriallizable) -> 파일저장
- pickle
'''
# 텍스트 형식
scores = {'kor' : 90, 'eng' : 95, 'math' : 70, 'scien' : 82}
print(type(scores))

def pickleWriter() :
    with open ('scoresPickle.txt', 'w', encoding='utf-8') as file :
        for (key, value) in scores.items() :
            file.write('{} : {}\n'.format(key, value))

pickleWriter()

# 바이너리 형식
import pickle

def pickleWriter() :
    with open (file = 'scoresPickle.txt', mode = 'wb') as file :
        pickle.dump(scores, file)
    print('객체 직렬화를 통한 파일저장')

pickleWriter()


def pickleReader():
    with open(file = 'scoresPickle.txt', mode = 'rb') as file:
        dictScores = pickle.load(file)
        print('파일로딩 - ', dictScores,type(dictScores))
    print('객체 직렬화를 통한 파일저장')

pickleReader()

''' 
1. 단어가 줄 단위로 저장된 cnt_words.txt 파일에서 
10자 이하인 단어의 개수를 카운트하는 함수 구현 및 호출
'''

def wordsReader() :
    wordList = []
    with open(file = './word/cnt_words.txt', mode = 'r', encoding='utf-8') as file :
        for word in file.readlines() :
            word = word.strip('\n')
            if len(word) <= 10 :
                wordList.append(word)
        print('10자 이하의 단어개수 {}'.format(len(wordList)))

wordsReader()

'''
special_words.txt 파일에서 문자가 'c'가 포함된 단어 출력
주의) 단어 출력 시 등장한 순서대로 출력 / ,.은 출력하지 않음
'''

def specialReader() :
    with open(file='./word/special_words.txt', mode='r', encoding='utf-8') as file :
        words = file.read().split()
        # print(type(words))
        for word in words :
            if 'c' in word :
                print(word.strip(',.'))
specialReader()

'''
zipcode.txt
input() 으로 동 이름을 입력받아 해당하는 동의 주소 출력하는 함수 정의 및 호출
입력예시) 개포 -> 개포동의 주소 출력
'''

def searchAddrFunc() :
    dong = input('동을 입력하세요 : ')
    with open(file = './word/zipcode.txt', mode = 'r',encoding='utf-8') as file :
        line = file.readline()
        while line :
            address = line.split()
            if address[3].startswith(dong) and address[3].endswith('동'):
                print(address)
            line = file.readline()

searchAddrFunc()

'''
csv, execel 파일 -> pandas lib 사용
- pip install pandas
- conda install pandas
- service_bmi.csv
- DataFrame
'''
import pandas as pd

bmiDataset= pd.read_csv('./word/service_bmi.csv', encoding='utf-8')
print(bmiDataset.info())
print(bmiDataset.head())
print(bmiDataset.tail())
# feature에 대한 접근 -> type : Series
print(bmiDataset.height,type(bmiDataset.height))
print(bmiDataset['weight'])

# 키, 몸무게 평균
# print('키 avg {}, 몸무게 avg {}'.format(sum(bmiDataset.height)/len(bmiDataset.height),
#                                     sum(bmiDataset.weight)/len(bmiDataset.weight)))

# 키, 몸무게 최대
print('max height - ', max(bmiDataset.height))
print('max weight - ', max(bmiDataset.weight))

# label 빈도수
labelCnt = {}
for label in bmiDataset.label :
    labelCnt[label] = labelCnt.get(label,0) + 1
print(labelCnt)

'''
spam_data.csv
'''
spamDataset = pd.read_csv('./word/spam_data.csv',header=None,encoding='ms949')
print(spamDataset)
print(spamDataset.info())
print(spamDataset.head())
target = spamDataset[0]
print(target)
text = spamDataset[1]
print(text, type(text))

# spam = 1, ham = 0 새로운 타겟을 만들고 싶다면?
target = [1 if t == 'spam' else 0  for t in target]
print(target)

# 코드클린 - 문자열에 대한 정규표현식을 이용하여 문자 제거
# 정규표현식 -> import re
'''
1. 메타문자
. ^ $ * + ? {} [] \ | ()
. -> 무엇이든 한 글자를 의미
^ -> 시작문자 지정
* -> 0 or more
+ -> 1 or more
? -> 0 or 1
ex)
[abc] -> a,b,c 중 한 문자와 매치
[^0-5] -> 0~5와 매치되지 않는 것
^[0-5] -> 반드시 0~5로 시작
문자클래스
\d -> 숫자의 자릿수
\D -> 숫자가 아닌 문자매칭의 자릿수
\w -> 문자+숫자
\W -> not 문자+숫자가 아닌 문자매치
\s -> 공백
010-0000-0000
^\d{3}-\d{4}-\d{4} -> 반드시 숫자로 시작

- sub()
- match()
- search()
- findall()
- finditer()
'''

# 텍스트 전처리 - (특수문자, 숫자, 공백, 영문제거) -> 한글 단어만 추출
import re
text = spamDataset[1]
print(text)

def cleanText() :
    for str in text :
        str = re.sub('[,.?!:;]',' ', str) # 문장부호 제거
        str = re.sub('[0-9a-zA-Z]',' ',str) # 숫자, 영문자 제거
        str = ' '.join(str.split()) # 한 칸 공백
        print(str)

cleanText()

def cleanText(str) :
    for str in text :
        str = re.sub('[,.?!:;]',' ', str) # 문장부호 제거
        str = re.sub('[0-9a-zA-Z]',' ',str) # 숫자, 영문자 제거
        str = ' '.join(str.split()) # 한 칸 공백
        return str
cleanData = [cleanText(t) for t in text]
print(cleanData)

# xls, xlsx 파일
kospiDataset = pd.ExcelFile('./word/sam_kospi.xlsx')
kospi = kospiDataset.parse('sam_kospi')
print(kospi.info())

from statistics import *
print('high mean - ', mean(kospi.High))

# json 파일 입출력 (dict과 비슷하다고 생각해~)
'''
json file : 네트워크 상에서 표준으로 사용되는 파일형식
구성 : {key : value , key : value}
encoding : python(dict, list) -> json 문자열(json file) : dumps()
decoding : json 문자열 -> python 객체 : loads()
import json
'''

# encoding : python -> json
import json
user = {'id' : 1234, 'name' : 'eun'}
print(type(user))

jsonStr = json.dumps(user) # object -> json str
print(jsonStr, type(jsonStr))

# decoding : json -> python
pyObj = json.loads(jsonStr)
print(pyObj, type(pyObj))
print(pyObj['id'])

'''
usagov_bitly.txt
'''

with open(file = './word/usagov_bitly.txt', mode = 'r', encoding='utf-8') as file :
    lines = file.readlines()
    # print(type(lines), len(lines))
    # print(lines[:5])
    rows = [json.loads(line) for line in lines]
    # print(type(rows))
    # print(type(rows[0]))
    # for row in rows :
    #     for key, value in row.items() :
    #         print('key - {}, value - {}'.format(key,value))
    # rows -> pd.DataFrame(행렬)
    rowsDF = pd.DataFrame(rows)

print(rowsDF.head)