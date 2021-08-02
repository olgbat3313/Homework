def flower(rose):
    def color():
        print('green ')
        rose()
        print('blue')
    return color

@flower
def rose():
    return print('rose ')

a = rose()




