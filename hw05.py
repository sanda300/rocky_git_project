

# 핸드폰 클래스에서 제조사, 출고년도, 색상을 출력하는 info()메소드를 추가하세요.

class Phone:
    name = '핸드폰'
    
    def prt(self):
        print('휴대폰 생성')

    def __init__(self, manuf, year, color):
        self.manuf = manuf
        self.year = year
        self.color = color
        
    def info(self):
        print("제조사 : ", self.manuf)
        print("출고년도 : ", self.year)
        print("색상 : ", self.color)

my_phone = Phone('삼성', '2024년', '검정')
my_phone.info()   
