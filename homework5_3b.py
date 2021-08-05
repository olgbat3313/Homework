class Line_m:

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

    def __repr__(self):
        return f'Line start {self.first_point} and finish {self.second_point}'

l = Line_m((1,2,5), (5, 8, 9))