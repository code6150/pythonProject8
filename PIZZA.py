#pizza 를 만들 때마다 몇개인지 세는 클래스

class Pizza:
    count = 0

    def __init__(self):
        Pizza.count += 1

Pizza()
Pizza()
p = Pizza
p.count = 22
Pizza()
Pizza()
print(p.count)