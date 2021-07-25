a = input('enter number from 001 to 999 ')
y = 0
b = len(a)
if b == 3 and a.isdigit()==True:
    for x in a:
        x = int(x)
        y = y+x
    print(y)     
else:
    print('your number is wrong ') 
if a.isdigit()==True:
    for x in a:
        x = int(x)
        y = y+x
    print(y)       
else:
    print('your number is wrong')    