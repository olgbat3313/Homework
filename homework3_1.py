#case1
a = input('enter first number ')
b = input('enter seconod number ')
if a.isdigit() == True and b.isdigit() == True:
    a = int(a)
    b = int(b)
    if 3<=a<=21 and 3<=b<=21:
        print(abs(a-b))  
    else:
        print(a+b)
else:
    print(a+b)
   


       