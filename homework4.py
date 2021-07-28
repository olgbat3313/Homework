def fibbon(n):
    if n>1:
        n = fibbon(n-2)+fibbon(n-1)
    else:
        n=1
    return n
a = print(fibbon(9))


n=9
a1 = 1
a2 = 1
for i in range(1, n):
    sum = a1+a2
    a1 = a2
    a2 = sum
print(a2)    
