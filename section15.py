#시, 분, 초로 구성된 Watch 클래스를 생성하세요.

# - 사용자로 부터 HH:mm:ss 형식의 시간을 입력받아서, 이름 Watch 클래스의 hour, minute, second 인스턴스 변수에 저장
# - add_hour(n) 메소드를 이용해서 지정된(n) 시간이 지난 시간을 계산하세요.
# - add_minute(n) '' 분
# - add_second(n) '' 초
# - hour 는 0~23 / minute 0~59, second 0~59 값만 가질 수 있습니다.

class Watch:
    def __init__(self, format: str):
        # ['HH', 'mm', 'ss']
        self.hour, self.minute, self.second = map(int, format.split(':'))

    def add_hour(self, n):
        self.hour += n
        if self.hour > 23:
            self.hour -= 24

    def add_minute(self, n):
        self.minute += n
        self.add_hour(self.minute // 60)
        self.minute %= 60

    def add_second(self, n):
        self.second += n
        self.add_minute(self.second // 60)
        self.second %= 60

