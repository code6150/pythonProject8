# 노래제목, 장르 - Song
# 가수, 대표곡 - Singer

# 1. 다음과 같은 형식으로 코드를 작성하세요.
# song = Song()
# song.set_song('취중진담', '발라드')

#singer = Singer()
#singer.set_singer('김동률')
#singer.set_singer(song)

#singer.print_singer()

#최종출력
#가수이름: 김동률
#노래제목: 취중진담(발라드)


class Song:
    def set_sing(self, title, category):
        self.title = title
        self.categaory = category

    def print_song(self):
        print(f'{self.title}({self.categaory})')

class Singer:
    def set_singer(self, singer):
        self.singer = singer

    def set_hit_song(self, song):
        self.song = song

    def print_singer(self):
        print(f'가수이름: {self.singer}')
        print(f'노래제목: ', end = '')
        self.song.print_song()
