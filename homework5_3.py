class Point_m:
    def __init__(self, *args):
        for arg in args:
            if type(arg) not in (float, int):
                raise ValueError('Invalid argument')
        self.__point = args

    def get_point(self):
        return self.__point 

    @property
    def shape(self):
        return len(self.__point)

    def get_koords(self):
        return self.__point

    def distance(self, koord):
        if koord.shape != self.shape:
            raise ValueError('Incorrect shape ')
        sum = 0
        for (x1, x2) in zip(koord.get_koords(), self.get_koords()):
            sum += (x1-x2) ** 2
        return print(f"distance = {sum ** 0.5}".format())

    def distance_0(self):
        args = tuple([0] * self.shape)
        m0 = Point_m(*args)
        return self.distance(m0)

class Line_m(Point_m):

    def __init__(self, p1, p2):
        point1 = Point_m(*p1)
        point2 = Point_m(*p2)
        if point1.shape != point2.shape:
            raise ValueError('Incorrect shape')
        self.first_point = point1
        self.second_point = point2

    def distance(self):
        return self.first_point.distance(self.second_point)

    def parallel_move(self):
        for i in range(0, self.first_point.shape):
            self.second_point[i] -= self.first_point[i]
            self.first_point[i] = 0

    def get_line(self):
        return print('Line start {self.first_point} and finish {self.second_point}')

m1 = Point_m(5, 6, 3, 8)
m2 = Point_m(0,0, 9, 1)
print(m1.shape)
print(m2.shape)
m1.distance(m2)
m1.distance_0()
l = Line_m((5,4,8),(5,8,9))