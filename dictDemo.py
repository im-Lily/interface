# python mapping type - dict
# dictionary -> key : value
# Hash or Associative Array와 유사한 구조
# dict{}
# 순서와 키 중복 불가능 / 수정, 삭제 가능

temp = {}
print(type(temp))

dict01 = {
    'name' : 'eun',
    'age' : 25,
    'address' : 'incheon',
    'birth' : 970327,
    'gender' : 'f'
}
print(dict01,type(dict01))

# dict에 요소 추가하는 방법
dict01['marriage'] = False
print(dict01,type(dict01))

# 키 유무 판단
print('marriage' in dict01)

# dict의 value 출력
print('address - ', dict01['address'])
# 데이터 확인
print(dict01.get('name'))
print(len(dict01))

# dict함수를 이용하여 여러 개의 튜플() 이용하여 리스트[] 타입으로 만들었음
dict02 = dict([('name','eun'),('age',49),('adress','incheon')])
print(dict02, type(dict02))

# dict_keys, dict_values, dict_items
# 리스트처럼 보이지만 리스트가 아님!
# 조작하기 위해서는 casting함수 이용
print('dict_keys - ', dict01.keys(),type(dict01.keys()),type(list(dict01.keys())))
print('dict_values - ', dict01.values(),type(dict01.values()),type(list(dict01.values())))
print('dict_items - ', dict01.items(),type(dict01.items()),type(list(dict01.items())))

# looping
for key in dict01.keys() :
    print('key : {} , value : {}'.format(key,dict01.get(key)))
   #print('key : {} , value : {}'.format(key,dict01[key]))

for value in dict01.values():
    print('value : {}'.format(value))

for (key, value) in dict01.items() :
    print('key : {} , value : {}'.format(key, value))

# 삭제 pop(), del
del dict01['gender']
print(type(dict01),dict01)
print(dict01.pop('birth'),dict01)

# 전체요소 삭제
dict01.clear()
print(dict01)
