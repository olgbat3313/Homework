# не решена
a = int(input('enter number  '))
b = int(input('enter number  '))
c = abs(a-b)
if c==0:
    print('nod= ',a)
elif a<b:
    b = c
    c = abs(a-b)
else:
    a = c
    c = abs(a-b)
