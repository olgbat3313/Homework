deposit = int(input('enter sum of your deposit '))
years = int(input('enter years '))
proc = 0.1
while years>0:
    years = years-1
    deposit = deposit + deposit*proc  
print('our sum = ', deposit)    