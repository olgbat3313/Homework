class Windows:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def square(self):
        return print('Square = ', self.width * self.height)
    
class Room:

    def __init__(self, w, h, d):
        self.width = w
        self.height = h
        self.deep = d
        self.windows = []


    def wall_square(self):
        p = (self.width + self.deep) * 2
        area = p * self.height 
        
        for window in self.windows:
            area -=window.square
        return area

    def add_window(self, w, h):
        self.windows.append(Windows(w,h))

class Oboi:

    def __init__(self, w, h):
        self.width = w
        self.height = h
        area1 = Room
        self.area_room = area1.wall_square


    def square_oboi(self):
        area = self.width * self.height
        return area

    def number_oboi(self):
        number = area1.wall_square / self.square_oboi  
        return number

r = Room(10, 20, 30)
print(r.wall_square())
r.add_window(1, 2)
print(r.wall_square)
o = Oboi(2, 3)
print(o.square_oboi())
print(o.number_oboi()) 