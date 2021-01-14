### composition은 상속과 다른 개념 / 클래스의 일부 기능만을 사용하고 싶을 때!

class Calc01 :
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    def add(self) :
        return self.x + self.y
    def substract(self):
        return self.x - self.y

class Calc02 :
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def multiply(self):
        return self.x * self.y

class UserCalc :
    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.cal01 = Calc01(x, y)
    def add(self):
        return self.x + self.y
    def substract(self):
        return self.cal01.substract()

clac = UserCalc(3,4)
clac.multiply()
clac.substract()

### Exception

def userKeyIn() :
    try :
        age = int(input('나이를 입력하세요 :'))
    except Exception :
        print('문자열이 아닌 정수를 입력하세요!')
    else :
        print('나이 %d' %age)
    finally:
        pass

userKeyIn()

try :
    x = int(input('나눌 숫자 :'))
except Exception :
    print('예외발생')
else :
    y = 10 / x
    print(y)
finally :
    pass

try :
    x = int(input('3의 배수를 입력하세요 : '))
    if x % 3 != 0 :
        raise Exception('3의 배수가 아님')
    print(x)
except Exception as e :
    print('예외발생', e)

def threeMultiple() :
    x = int(input('3의 배수 입력 : '))
    if x % 3 != 0 :
        raise Exception('3의 배수가 아님')
    print(x)

try :
    threeMultiple()
except Exception as e:
    print('예외발생', e)

nameList = ['kim','jeong','park','lee']
try :
    name = 'cho'
    if name not in nameList :
        raise Exception
except Exception :
    print('{} not found it'. format(name))
else :
    print('{} found it'.format(name))
finally :
    pass
print('프로그램 종료')

class Account :
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate
    def withDraw(self, amount):
        try :
            if self.balance < amount :
                raise Exception
        except Exception :
            print('잔액부족')
        else :
            self.balance -= amount

account = Account('100', 100000, 1.1)
account.withDraw(200000)

class InsufficientError(Exception) :
    def __init__(self):
        super().__init__()

class Account :
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate
    def withDraw(self, amount):
        try :
            if self.balance < amount :
                raise InsufficientError
        except Exception :
            print('잔액부족')
        else :
            self.balance -= amount

account = Account('100', 100000, 1.1)
account.withDraw(200000)

### collecionts.namedtuple

import collections

Person = collections.namedtuple('Person', ['name', 'age'])
person = Person('eun',25)
print(person,type(person))

print(person[0])
print(person.name)
name, age = person
print(name, age)

Emp = collections.namedtuple('Emp', ['name', 'age', 'dept'])
emp = Emp('eun', 30, 'edu')
print(emp, type(emp))
print(emp[1])
print(emp.dept)
name, age, dept = emp
print(name, age, dept)

### 파일 입출력
# 기존 파일 존재 시 내용 삭제 후 입력
file = open(file = 'hello.txt', mode = 'w')
line = ['I am studying\n', 'How about you?\n']
file.writelines(line)
file.close()

with open(file = 'hello.txt', mode = 'w') as file:
    line = ['I am studying\n', 'How about you?\n']
    file.writelines(line)

with open('hello.txt', 'r') as file :
    line = None # 변수 초기화
        while line != '' :
            line = file.readline()
            print(line.strip('\n'))

def fileStream(fileName, mode) :
    with open(fileName,mode) as file :
        try :
            if mode == 'w' :
                line = ['I am studying\n', 'How about you?\n']
                file.writelines(line)
            elif mode == 'r' :
                line = file.read()
                print(line)
            elif mode == 'a' :
                file.write('\nappend')
            else :
                raise Exception('모드 확인')
        except Exception :
            print('모드 확인')
        finally :
            pass

# binary 형식 입출력
scores = {'kor' : 90, 'eng' : 95, 'math' : 70, 'scien' : 92}
print(type(scores))

def scoresWriter() :
    with open(file='scores.txt', mode = 'w') as file :
        for key, value in scores.items() :
            file.write('{} : {}\n'.format(key, value))

scoresWriter()

import pickle

def pickleWriter() :
    with open('scores.txt','wb') as file:
        pickle.dump(scores,file)

pickleWriter()

def pickleReader() :
    with open('scores.txt','rb') as file :
        print(pickle.load(file))

pickleReader()

def wordsReader() :
    wordList = []
    with open(file = './word/cnt_words.txt', mode = 'r', encoding='utf-8') as file :
        for word in file.readlines() :
            word = word.strip('\n')
            if len(word) <= 10 :
                wordList.append(word)
        print('10자 이하의 단어개수 {}'.format(len(wordList)))

wordsReader()

def specialReader() :
    with open('./word/special_words.txt','r',encoding='utf-8') as file :
        word = file.readline().split()
        # print(word, type(word))
        for w in word :
            if 'c' in w :
                print(w.strip(',.'))

specialReader()

### 왜 안될까
def searchFunc() :
    with open('./word/zipcode.txt', 'r', encoding='utf-8') as file:
        try :
            dong = input('동을 입력하세요 : ')
            line = file.readline()
        except Exception :
            print('문자를 입력하세요 : ')
        else :
            while line :
                address = line.split()
                # print(address,type(address))
                if address[3].startswith(dong) and address[3].endswith('동') :
                    print(address)
                line = file.readline()

searchFunc()
