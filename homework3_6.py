# не решена
a = int(input('enter number  '))
b = int(input('enter number  '))
if a!=0 or b!=0 or a!=b:
    if a>b:
        while a>b:
            c = a-b
            a = c     
        print(a)
    else:
        while b>a:
            c = b-a
            b = c       
        print(b)
else:
    print(a)