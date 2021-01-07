# 매개변수, 리턴값 X
def printCoins() :
    print('bitcoin')

# 매개변수 X, 리턴값 O
def returnFunc() :
    return '호출한 쪽으로 값 전달'

# 매개변수, 리턴값 O
def sayEcho(name):
    return name + '안녕'

def calculator(op01, operator, op02):
    pass

def makeUrl(url) :
    return 'www.' + url + '.com'

# 매개변수 O, 리턴값 X
def badFunc(name) :
    pass

# 가변인자로 튜플을 받을 수 있음
# 매개변수 개수와 상관없이 받을 수 있음
def tupleFunc(*args) :
    result = 0
    for idx in range(len(args)) :
        result += args[idx]
    return result

# 가변인자로 딕셔너리를 받을 수 있음
def dictFunc(**args) :
    for key, value in args.items() :
        print('{} - {}'.format(key,value))

# 범위내에 있는 값의 홀, 짝 합 구하기 -> 2개의 리턴값 필요
# tuple
def cntSum(start, end) :
    odd = even = 0
    for x in range(start, end+1) :
        if x % 2 == 0 :
            even += x
        else :
            odd += x
    return odd, even

# list
def leapYearFunc(year1,year2) :
   yearList = []
   for year in range(year1,year2+1) :
       if (year % 4 ==0 and year % 100 != 0) or (year % 400 == 0) :
           yearList.append(year)
   return yearList

# dict
def rtnDictFunc(x) :
    y01 = x * 10
    y02 = x * 20
    y03 = x * 30
    return {'val01' : y01, 'val02' : y02, 'val03' : y03}





