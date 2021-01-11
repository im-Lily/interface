from ai.oop.oopExec import *

# unit = Unit(10,100)
# unit.unitInfo()
#
# # type check
# if unit.utype == 'Unit' :
#     print(True)
# else :
#     print(False)

# Marin 생성
marin01 = Marine(10, 100, 0, 0)
marin02 = Marine(10, 100, 0, 0)
marin03 = Marine(10, 100, 0, 0)
marin04 = Marine(10, 100, 0, 0)

# Medic 생성
medic01 = Medic(0,100,0)
medic02 = Medic(0,100,0)

# 병력을 list에 담아줌
tropList = [marin01,marin02,marin03,marin04,medic01,medic02]

# 기본정보 출력
for obj in tropList :
    obj.unitInfo()

# DropShip 생성
ship = DropShip(0, 50)

# 부대원을 태운다면?
ship.board(tropList)

# 목표지점으로 이동
ship.attack()

# 부대원 하차
tropAttackList = ship.drop()

# 공격
for unit in tropAttackList :
    if isinstance(unit, Marine) :
        unit.stimpack()
    unit.attack()



