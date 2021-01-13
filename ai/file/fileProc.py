'''
텍스트파일 입출력
open(file = '파일경로/파일명', mode = 'r|w|a|wb')
'''

# file = open(file = 'hello.txt', mode = 'w')
# file.write('Hi, Jeong')
# file.close()

# file = open(file = 'hello.txt', mode = 'r')
# print(file.read())
# file.close()

# with open() as file -> 자동으로 close해줌
with open(file='hello.txt', mode='r') as file :
    print(file.read())

def fileStream(fileName, mode) :
    file = open(file=fileName, mode=mode)
    try :
        if mode == 'w' :
            # file = open(file=fileName, mode=mode)
            file.write('sample txt')
        elif mode == 'r' :
            # file = open(file=fileName, mode=mode)
            line = file.read()
            print('result read - ', line)
        elif mode == 'a' :
            # file = open(file=fileName, mode=mode)
            file.write('\nappend')
        else :
            raise Exception('모드를 확인하세요')
    except Exception as e :
        print(e)
    finally:
        if file != None :
            file.close()

def withMultiWriter(fileName) :
    with open(fileName, 'w', encoding='utf-8') as file :
        for idx in range(3) :
            print('idx - ', idx)
            text = input('문자열을 입력하세요: ')
            file.write('{} - {}\n'.format(idx,text))

def withListFileWriter(fileName, dataset) :
    with open(fileName, 'w', encoding='utf-8') as file :
        for idx in range(len(dataset)) :
            print('idx - ', idx)
            file.write('{} - {}\n'.format(idx,dataset[idx]))

def withListFileRead(fileName, mode) :
    with open(fileName, mode , encoding='utf-8') as file :
        # line = None
        # while line != ''
        #     line = file.readline()
        #     print(line.strip('\n')) # 개행제거

        # for line in file.readlines() :
        #     print(line.strip('\n'))

        # print(file,type(file))

        for line in file :
            print(line.strip('\n'))