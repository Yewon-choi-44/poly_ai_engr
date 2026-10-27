class Cat:
    #생성자 혹은 초기화 메소드라 한다.
    def __init__(self, name, color="흰색"):
        self.name=name
        self.color=color
    #고양이의 정보를 출력하는 메소드
    def meow(self):
        print("내 이름은 {}, 색깔은 {}, 야옹 야옹~~".format(self.name, self.color))


nabi = Cat('나비', '검정색')
nero = Cat('네로')
mimi = Cat('미미', '갈색')

nabi.meow()
nero.meow()
mimi.meow()
