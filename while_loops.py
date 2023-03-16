# IMP Homework:
# Write a Python program that takes name of a fruit from user & prints whether it is in the following list or not:
'''
fruits = ["apple", "kiwi", "banana", "cherry", "grapes", "orange"]
a = input("Enter a fruit name")
i = 0
flag = 0
while i < len(fruits):
    if fruits[i] == a:
        flag = 1
    i += 1

if flag == 1:
    print("yes it is in the list")
else:
    print("no it is not in the list")
'''

# better method using (((((while else)))))------------------- 
'''
fruits = ["apple", "kiwi", "banana", "cherry", "grapes", "orange"]
a = input("Enter a fruit name")
i = 0
while i < len(fruits):
    if fruits[i] == a:
        print("yes it is in the list")
        break
    i += 1
else:
    print("no it is not in the list")
'''



# 1. Write a Python code that takes an integer from user and prints number of digits in that integer.
'''
a=int(input("enter a no."))
if a<0:
    a=a*(-1)

print(len(str(a)))
'''

# 2. Write down a Python code that creates a user defined list
'''
n=int(input("Enter total no of values in list"))
mylist=[]
i=0
while i<n:
    mylist.append(input("Enter new element of list"))    
    i+=1
print(mylist)
'''

# 3. Write a Python code to print each of the elements of a given list in a new line
'''fruits = ["apple", "kiwi", "banana", "cherry", "grapes", "orange"]
a=len(fruits)
i=0
while i<a:
    print(fruits[i])
    i+=1'''

# 4. Write a Python program that prints whether the number given is a prime number or not.
'''
a=int(input("Enter a number"))
flag=True
i=0
for i in range (2,a):
    flag=a%i
    if(flag==False):
        break
if(flag==True):
    print("prime")
else:
    print("not prime")

'''
'''      #perfect square
a=int(input("Enter a number"))
i=0
flag=False
for i in range (1,a):
    n=i*i
    if n==a:
        flag=True
        break
if flag==True:
    print("Perfect square")
else :
    print("Not Perfect square")
'''
# 5. Write a Python program that prints whether the number given is a perfect number or not.
# perfect no. => sum of divisors excluding itself ----------------6=1+2+3
'''a=int(input("enter a value"))
sum=0
for i in range(1,a):
    if a%i==0:
        sum=sum+i
        # print(i)
# print(sum)        
if sum==a:
    print("it is perfect number")
else:
    print("it is not perfect number")'''
#  Ask user for a 3-digit integer & print whether it's an Armstrong number or not. A 3-digit integer is an Armstrong number if sum of cubes of all of its digits equals to the number itself.
#     eg, 153:
#     (1^3) + (5^3) + (3^3) = 153
# a=int(input("Enter a number"))
# sum =0
# for i in range(1,4):
#     temp=a
#     temp=temp%10
#     a=a//10
#     sum=sum+(temp**3)
# if sum==a:
#     print("Armstrong")
# else:
#     print("not Armstrong")



# 6. Write a Python program that prints whether the number given is an Armstrong number or not.



# 7. Write a Python program that prints all the prime numbers between two integers given by user.
# p=int(input("Enter a number"))
# q=int(input("Enter a number"))
# flag=True
# i=0
# for a in range (p,q+1):
#     for i in range (2,1+ int(a**0.5)):
#         flag=a%i
#         if(flag==False):
#             break
#     if(flag==True):    
#             print(a)



# 8. Write a Python program that prints all the perfect numbers between two integers given by user.
# 9. Write a Python program that prints all the Armstrong numbers between two integers given by user
# a=int(input("Enter a number"))
# b=a
# pow=int(len(str(a)))
# sum=0
# for i in range(1,pow+1):
#     temp=a
#     temp=temp%10
#     a=a//10
#     sum=sum+(temp**pow)
# if sum==b:
#     print("Armstrong")
# else:
#     print("not Armstrong")






# fruits = ["apple", "kiwi", "banana", "cherry", "grapes", "orange"]
# i = 0
# while i < len(fruits):
#     if fruits[i] == 'cherry':
#         # break
#         continue
#     print(fruits[i])
#     i += 1
