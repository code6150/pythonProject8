
# 클래스메소드/정적메소드
# classmethod / staticmethod

# self -> instance (생성 된 객체) 접근
# cls -> class 클래스 접근

class Pizza:
    material = '불고기' # 클래스 변수 (self. -> x, cls.->o)

    #instance method
    def set_material(self,material):
        self.material = material

    # 객체 생성을 하지 않아도 실행 가능하다.
    @classmethod
    def set_material_cls(cls,material):
        cls.material = material

    # 클래스 변수, 인스턴스 변수에 접근할 수 없음.
    # 객체 생성을 하지 않아도 실행 가능하다.
    @staticmethod
    def make_pizza():
        pass