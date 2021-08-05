x = int(input('enter number '))
#import pdb; pdb.set_trace()
for i in range(0, x):
    if i % 2 == 0:
        print('number is EVEN', i)
    else:
        print('number is ODD', i)

a = [1,5,6,7]
b = [56, 8, 9, 0]
f = list(map(lambda a, b: (a * 2 + b), a,b))
print(f)