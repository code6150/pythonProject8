
#Person 클래스 ( 이름, 전체 인구수 )
# 이름 - instance variable
# 전체 인구 - class variable

# man = Person('james')
# woman = Person('emily')

# 객체 생성 시 자동으로
# james is born
# emily is born

#print(f'전체 인구수{Person.get_population()} 명')

# del man

# 삭제 될 시 자동으로
# 이름 is dead. - 메세지 출력

class Person:
    count = 0

    def __init__(self, name):
        Person.count += 1
        self.name = name
        print(f'{name} is born.')

    @classmethod
    def get_population(cls):
        return Person.count

    def __del__(self):
        print(f'{self.name} is dead.')
        Person.count -= 1

# Shop - 가게 매출을 구할 수 있는 클래스
# - 클래스 변수 ( total - 전체 매출액 / menu_list - 메뉴명, 가격 [딕셔너리])
# - total = 0
# - menu_list [{'떡볶이':3000},{'순대',3000},{'튀김',500},{'김밥',2000}]

class Shop:
    total = 0
    menu_list = {'떡볶이':3000, '순대':3000, '튀김':500, '김밥':2000}

    @classmethod
    def sales(cls, name, amount):
        cls.total += cls.menu_list[name] * amount

# Hybrid 를 구현하세요
class Car:
    max_oil = 50
    def __init__(self, oil):
        self.oil = oil

    def add_oil(self,oil):
        if oil <= 0:
            return

        self.oil += oil
        # 20 + 50
        if self.oil == Car.max_oil:
            self.oil = Car.max_oil

    def car_info(self):
        print(f'현재 주유상태: {self.oil}')

#서브 클래스 Hybrid 는 다음과 같은 특징을 들고 있습니다.
# - 최대 배터리 충전량은 30입니다.
# - 배터리를 충전하는 charge() 메소드가 있습니다. 최대 충전량을 초과할 수 없습니다. 0보다 작은 값으로 충전금지
# - 현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() .라는 메소드가 있습니다.

# car = hybrid(0,0)
# car.add_oil(100)
# car.charge(50)
# car.hybrid_info()
# 현재 주유상태: 50
# 현재 주유상태: 30

class Hybrid(Car):
    max_battery = 30
    def __init__(self, battery, oil):
        self.battery = battery
        super.__init__(oil)

    def charge(self, battery):
        if battery <= 0:
            return
        self.battery += battery
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery

    def hybrid_info(self):
        super().car_info()
        print(f'현재 충전상태: {self.battery}')
