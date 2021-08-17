# - 每行代码，或每个方法要求添加注释（基础不好的同学）
#
# 题目内容：
#
# 1. ⼀个回合制游戏，有两个英雄，分别以两个类进⾏定义。分别是Timo和Jinx。每个英雄都有 hp 属性和 power属性，hp 代表⾎量，power 代表攻击⼒
# 2. 每个英雄都有⼀个 fight ⽅法， fight ⽅法需要传⼊“enemy_hp”（敌⼈的⾎量），“enemy_power”（敌⼈的攻击⼒）两个参数。需要计算对打一轮过后双方的最终血量，
# 英雄最终的⾎量 = 英雄hp属性-敌⼈的攻击⼒enemy_power
# 敌⼈最终的⾎量 = 敌⼈的⾎量enemy_hp-英雄的power属性
# 量和敌⼈最终的⾎量，⾎量剩余多的⼈获胜。如果英雄赢了打印 “英雄获胜”，如果敌⼈赢了，打印“敌⼈获胜”
#
# 4. 使用继承、简单工厂方法等各种方式优化你的代码

# 继承方式
import random

#创建一个英雄类
class Hero:
    Hero_name="Hero"
    Hero_hp = 0
    Hero_power = 0

    def fight(self, name,enemy_hp, enemy_power):
        '''

        :param name: 英雄名
        :param enemy_hp: 敌人血量
        :param enemy_power: 敌人攻击力
        :return:
        '''
        #敌人战斗后血量
        enemy_end_hp = enemy_hp - self.Hero_power
        #英雄战斗后血量
        hero_end_hp = self.Hero_hp - enemy_power
        #当英雄血量大于敌人血量时
        if hero_end_hp > enemy_end_hp:
            print(f"{name}胜利")
        #当血量相等时
        elif hero_end_hp == enemy_end_hp:
            print("平局")
        #当血量低于敌人血量
        else:
            print(f"{name}败北")

#创建一个英雄提莫,继承主类
class timo(Hero):
    Hero_name = "提莫"
    Hero_hp = random.randint(1000, 1300)
    Hero_power = random.randint(100, 150)
    pass

#创建一个英雄金克斯
class Jinx(Hero):
    Hero_name = "金克斯"
    Hero_hp = random.randint(1000, 1300)
    Hero_power = random.randint(100, 150)
    pass



