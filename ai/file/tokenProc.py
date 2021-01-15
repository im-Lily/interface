'''
palindrom(회문) : 단어를 거꾸로 읽어도 제대로 읽는 것과 같은 단어 또는 문장
level, sos, rotator, 'nurse run'
기준필요(중앙을 기준으로 첫 글자와 마지막 글자 비교) -> 반복문
// : 몫
'''
str = 'eun1234'
idx = len(str) // 2
print(idx,str[idx])

def isPalindrom() :
    isFlag = True
    word = input('문자열을 입력하세요 : ')
    for idx in range(len(word) // 2) :
        if word[idx] != word[-1 - idx] :
            isFlag = False
            break
    return isFlag

isPalindrom()

def reversedPailndrom() :
    word = input('문자열을 입력하세요 : ')
    print(word == word[::-1])
    print(type(reversed(word)), reversed(word))
    print(list(word), list(reversed(word)))
    print(list(word) == list(reversed(word)))

# palindrom_words.txt 에서 회문인 단어만 출력
def palindromFile() :
    with open('./word/palindrome_words.txt','r', encoding='utf-8') as file:
        for line in file :
            line = line.strip('\n')
            if line == line[::-1] :
                print(line)

palindromFile()

# 문자열에서 n - gram의 연속된 요소 추출
# 자연어처리

text = 'hello'
for idx in range(len(text) - 1) :
    print(text[idx], text[idx + 1], sep='')

text = 'this is python script'
textList = text.split()
print(type(textList))
for idx in range(len(textList) - 1) :
    print(textList[idx], textList[idx + 1])

# zip()
num = [1,2,3,4]
name = ['hong', 'gil', 'dong', 'guy']

dic = {}
for key, value in zip(num, name) :
    dic[key] = value
print(dic)

'''
input 함수를 이용해서 문자열을 입력받고
ex) python is a programming language that lets your work quickly
input 함수를 이용해서 gram 할 숫자를 입력받고
ex) 2
입력된 숫자에 해당하는 단어 N-gram 형식으로 출력
주의) 입력된 문자열의 단어개수가 입력된 정수 미만이라면 예외발생
'''

def zipNgram() :
    sentences = input('sentences : ')
    gram = int(input('gram : '))
    words = sentences.split()
    # for idx in range(len(words)-gram+1) :
    #     print(words[idx:idx+gram])
    ngram = zip( * [words[idx: ]for idx in range(gram)])
    # print(list(ngram))
    for idx in ngram :
        print(idx)
zipNgram()