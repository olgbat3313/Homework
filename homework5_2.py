def fibbon(n):
    a1 = 1
    a2 = 1
    for i in range(1, n):
        sum = a1+a2
        yield sum
        a1 = a2
        a2 = sum
        
  
val=fibbon(12)        
#import pdb; pdb.set_trace
for x in val:
    print(x)

