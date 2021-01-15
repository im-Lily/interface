def mpgFunc() :
    with open('./word/mpg.txt', 'r', encoding='utf-8') as file :
        featureLine = file.readline().split(',')
        # print(featureLine, type(featureLine))
        carList = []
        for car in file.readlines():
            car = car.split(',')
            # print(car,type(car))
            dic = {}
            for key, value in zip(featureLine,car) :
                dic[key] = value
            # print(dic)
            carList.append(dic) # [{},{},{}]
    return carList

mpgFunc()

def question01():
    list = mpgFunc()
    cnt4 = 0
    cnt5 = 0
    hwySum4 = 0
    hwySum5 = 0
    for idx in range(0,len(list)) :
        displValue = float(list[idx]['displ'])
        # print(displValue,type(displValue))
        hwyValue = int(list[idx]['hwy'])
        # print(hwyValue,type(hwyValue))
        if displValue <= 4 :
            hwySum4 += hwyValue
            cnt4 +=1
            # print(hwySum4)
        elif displValue >= 5 :
            hwySum5 += hwyValue
            cnt5 +=1
            # print(hwySum5)
    print('배기량 4이하인 자동차의 고속도로 평균연비 : {}'.format(hwySum4/cnt4))
    print('배기량 5이상인 자동차의 고속도로 평균연비 : {}'.format(hwySum5/cnt5))

question01()

def question02() :
    list = mpgFunc()
    ctyAudi = 0
    ctyToyota = 0
    cntAudi = 0
    cntToyota = 0
    for idx in range(0,len(list)) :
        manuList = list[idx]['manufacturer']
        ctyList = int(list[idx]['cty'])
        # print(manuList,type(manuList))
        # print(ctyList,type(ctyList))
        if manuList == 'audi' :
            ctyAudi += ctyList
            cntAudi += 1
            avgAudi = ctyAudi/cntAudi
            # return avgAudi
        elif manuList == 'toyota' :
            ctyToyota += ctyList
            cntToyota += 1
            avgToyota = ctyToyota/cntToyota
    if avgAudi > avgToyota:
        print('cty of audi : {}'.format(round(avgAudi,3)),'아우디 도시연비가 평균적으로 더 높음')
    else:
        print('cty of toyota : {}'.format(round(avgToyota,3)),'토요타 도시연비가 평균적으로 더 높음')

question02()

list = mpgFunc()
def question03(myList,name) :
    list = mpgFunc()
    hwySum = 0
    hwyCnt = 0
    for idx in range(0,len(list)) :
        manuList = list[idx]['manufacturer']
        hwyValue = int(list[idx]['hwy'])
        if manuList == name:
            hwySum +=  hwyValue
            hwyCnt += 1
            return hwySum/hwyCnt

question03(list,'chevrolet')
question03(list,'ford')
question03(list,'honda')

def question04() :
    myList = mpgFunc()
    result = []
    for idx in range(0,len(myList)) :
        manuList = myList[idx]['manufacturer']
        if manuList == 'audi' :
            audiList = myList[idx]['hwy'].split()
            # print(audiList,type(audiList))
            result.extend(audiList)
            audiSort = sorted(result, key = lambda x : x[0], reverse=True)
            # sorted(a, key=lambda x: x[0])
    # print(audiSort[:5])
    return audiSort[:5]

question04()



