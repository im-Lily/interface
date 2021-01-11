'''
Unit (Marine, Medic, DropShip)
Marine - 4명
Medic - 2명
DropShip - 6명을 태워서 특정 지점 공격
상속 실습
'''

class Unit(object):
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__
        self.damage = damage
        self.life = life
    def unitInfo(self):
        print('타입 {}'.format(self.utype))
        print('공격력 {}'.format(self.damage))
        print('생명력 {}'.format(self.life))
    def attack(self):
        pass

class Marine(Unit) :
    def __init__(self, damage, life, offense, defense):
        super().__init__(damage, life)
        self.offense = offense
        self.defense = defense
    def unitInfo(self):
        super().unitInfo()
        print('공격력 업그레이드 {}'.format(self.offense))
        print('방어력 업그레이드 {}'.format(self.defense))
    def attack(self):
        print('마린공격')
    def stimpack(self):
        if self.life > 50 :
            self.damage *= 1.5
            self.life -= 10
        else :
            print('체력이 낮아 stimpack 사용불가')

class Medic(Unit) :
    def __init__(self, damage, life, defense):
        super().__init__(damage, life)
        self.defense = defense
    def unitInfo(self):
        super().unitInfo()
        print('방어력 업그레이드 {}'.format(self.defense))
    def attack(self):
        print('마린치료')

class DropShip(Unit) :
    def __init(self, damage, life, defense):
        super().__init__(damage, life)
        self.defense = defense
    def unitInfo(self):
        super().unitInfo()
        print('방어력 업그레이드 {}'.format(self.defense))
    def attack(self):
        print('목표지점으로 이동')
    def board(self, unitType):
        self.unitType = unitType
        print('부대원 승차')
    def drop(self):
        print('모든 부대원(unit) 하차')
        return self.unitType
