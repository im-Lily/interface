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
    with open (file = 'scores.txt', mode = 'wb') as file :
        pickle.dump(scores, file)
    print('객체 직렬화를 통한 파일저장')

pickleWriter()


def pickleReader():
    with open(file = 'scores.txt', mode = 'rb') as file:
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


