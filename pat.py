'''
123456789
 2345678
  34567
   456
    5
   456
  34567
 2345678
123456789
'''
for i in range(1,6):
    for j in range(1,10):
        if j>=i and j<=10-i :
            print(j,end='')
        else:
            print(" ",end='')
    print()

for i in range(4,0,-1):
    for j in range(1,10):
        if j>=i and j<=10-i :
            print(j,end='')
        else:
            print(" ",end='')
    print()



