class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    def show(self):
        print(f'({self.x}, {self.y})')

    def set(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return self.x, self.y

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)
    
    def show(self):
        print(f'좌측 상단 꼭지점이 {self.lt.get()}이고', end = ' ')
        print(f'우측 하단 꼭지점이 {self.rb.get()}인 사각형입니다.', end = '')

    def getWidth(self):
        return self.rb.get()[0] - self.lt.get()[0]

    def getHeight(self):
        return self.rb.get()[1] - self.lt.get()[1]

    def getArea(self):
        return self.getHeight() * self.getWidth()

    def getPerimeter(self):
        return (self.getHeight() + self.getWidth()) * 2
    
r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()

r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')
