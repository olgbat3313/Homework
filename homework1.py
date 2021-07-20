n = int(input('enter time '))
h = n // 3600
x = n % 3600
m = x // 60
s = x % 60
print(f'{h} {m} {s}')