class NameCalss:
    def __init__(self, name):
        self.name = name

#self -> 생성된 객체 (자신)
#cls -> 클래스 자체
#super -> 부모 객체

class A(NameCalss):
    # 오버라이딩 - 상속받은 객체의 메소드를 덮어씌운다.
    def __init__(self,name):
        super().__init__(name + 'A')

class B(NameCalss):
    pass


# isinstance(생성된 객체, 클래스명) - True or False -> 생성된 객체가 오른쪽의 클래스와 같으냐?
print(isinstance(A(), NameCalss))

NameCalss('d')