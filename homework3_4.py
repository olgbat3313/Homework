
a = input('enter your choice 1-triangle, 2-circle, 3-rectangle ')
if a.isdigit() == True:
    a = int(a)
    if a==2:
        rad = int(input('enter rad '))
        sq = 3.14*rad**2
        print('square = ', sq)  
    elif a==1:
        b = int(input('enter first side '))
        c = int(input('enter second side '))
        d = int(input('enter third side '))
        p = (b+c+d)/2
        sq = (p*(p-b)*(p-c)*(p-d))**0.5
        print('square = ', sq)
    elif a==3:
        b = int(input('enter first side '))
        c = int(input('enter second side '))
        sq = b*c
        print('square = ', sq)
    else:
       print('wrong choice, repeat please ') 
else:
    print('wrong choice, repeat please ')
   
