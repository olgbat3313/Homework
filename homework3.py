#1 case
p = input('enter a product ')
#if p == 'milk':
#   print('milk cost 2')
#elif p == 'butter':
#    print('butter cost 5')
#elif p == 'flour':
#    print('flour cost 7')
#else:
#    print(-1)

#2 case
a = {'milk':2, 'butter':5, 'flour':7}
print(a.get(p, -1))
