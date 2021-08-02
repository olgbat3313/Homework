class Point_m:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    #def dimension_p(self, x, y, z):
     #   
    def distance(self, x, y, z):
        l = ((self.x**2)+(self.y**2)+(self.z**2))**0.5
        return print(f"distance = {l}".format())

#class Line_m(Point_m):
    
    


m=Point_m(5,6,1)
m.distance(5,6,1)

