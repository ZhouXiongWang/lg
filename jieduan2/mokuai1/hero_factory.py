from HomeWork2.Hero_jc import Jinx

from HomeWork2.Hero_jc import timo

#工厂模式
#创建英雄工厂类
class Hero_Factory:
    #创造英雄方法
    def create_hero(hero):
        if hero == 'Jinx':
            return Jinx
        elif hero == 'timo':
            return Timo
        else:
            raise Exception("没有这个英雄")

#提莫实例化
Timo = timo()
#金克斯实例化
jinx = Jinx()
#调用方法得出战斗结果
jinx.fight(Jinx.Hero_name, Timo.Hero_hp, Timo.Hero_power)
