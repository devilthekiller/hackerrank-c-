a=int(input("enter a no."))
flag=0
i=2
while i<a:
    if a%i==0 :
        flag=1
    #     break
    # else:                      #these only work togetherx
    #     flag=0
    i+=1

print("not prime") if flag==1 else print("prime")