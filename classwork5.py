class Table:
    def __init__(self, w, h, l):
        self.height = h
        self.widht = w
        self.lenght =l

class KitchenTable(Table):
    def set_places(self, p):
        self.places = p
