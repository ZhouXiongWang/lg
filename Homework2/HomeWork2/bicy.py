class Bicycle():

    def run(self,miles):
        print(f"教材了{miles}公里")

class Ebicycle(Bicycle):
    volume=0
    def fill_charge(self,volume):

        self.volume=self.volume+volume
        print(f'充电之后的电量为{self.volume}')

    def run_e(self,miles):
        #获取可骑行数
        vol_miles=self.volume * 10
        #判断电量是否耗尽
        if miles<=vol_miles:
            print(f'当前电动骑行了{miles}公里')
        else:
            print(f'当前电懂骑行了{vol_miles}')
            self.run(miles-vol_miles)


ASD= Ebicycle()
ASD.fill_charge(50)
ASD.run_e(1000)
