# 1. PERCENTAGE
'''
m = int(input("Enter marks of maths"))
s = int(input("Enter marks of science"))
e = int(input("Enter marks of english"))
per = (m+s+e)/3
if per > 75:
    print("grade is A ")
elif per > 65:
    print("grade is B ")
elif per > 55:
    print("grade is C ")
elif per > 45:
    print("grade is D ")
elif per >= 35:
    print("grade is E ")
elif per < 35:
    print("grade is F ")
'''

# 2. Write a Python program to find whether a given year is a leap year or not.
'''a=int(input("Enter a year"))
a=a%4
if a==0:
    print("leap")
else:
    print("not leap")'''

# 3. Write a Python program to find the largest of three numbers.
'''
a=int(input("enter 3 number\n"))
b=int(input())
c=int(input())
if a>=b and a>c:
    print("a is greatest")
elif b>=c and b>a:
    print("b is greatest")
elif c>=a and c>b:
    print("c is greatest")
'''
# 4. Write a Python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies.
# ++>1st
# -+>2nd
# -->3rd
# +->4th
'''
x=int(input("x:"))
y=int(input("y:"))
if x>0 and y>0:
    print("1st Quadrant")
elif x<0 and y>0:
    print("2nd Quadrant")
elif x<0 and y<0:
    print("3rd Quadrant")
elif x>0 and y<0:
    print("4th Quadrant")
elif x==0 and y==0:
    print("on origin")
elif x==0:
    print("on x-axis")
elif y==0:
    print("on y-axis")'''


# 5. Write a Python program to find the eligibility of admission for a professional course based on the following criteria
'''
m = int(input("Enter marks of maths"))
c = int(input("Enter marks of chemistry"))
p = int(input("Enter marks of physics"))
s = m+c+p
mp = m+p
if m > 64 and p > 54 and c > 49 and  s >= 190 and mp >= 140:
    print("ELIGIBLE")

else:
    print("not ELIGIBLE!!!!!!!!!!\nGO HOME!!!!!")
'''
# 6. Take values of length and breadth of a rectangle from user and check if it is square or not.
'''
x=int(input("l:"))
y=int(input("b:"))
if x==y:
    print("Square")
elif x!=y:
    print("Rectangle") 
else :
    print("invalid ")'''

# 7. A shop gives discount of 10% if the cost of purchased quantity is more than Rs.1000.
# Ask user for quantity
# Assume each item costs 100.
# Calculate and print total amount to be paid by user.

'''
n=int(input("Enter no. of items"))
# if n>=10:
#     cost=n*100*.90
# else:
#     cost=n*100   
# --------------or----------------
(cost:=n*100*.90) if n>=10 else (cost:=n*100)
print(cost)
'''

# 8. In above program, ask user for his/her name, mobile number, quantity and price of each item, then decide whether he/she is eligible for discount and based on that print the invoice in the following format:

# case 1- when customer is not eligible for discount:

'''
name=input("Enter your name")
num=input("Enter your number")
print("Enter 0 in price to quit")
while True:
    price=int(input("price:"))
    if price==0:
        break
    quan=int(input("Enter quantity :"))
    total=price*quan
    print(price,"\t",quan,'\t',total)
'''
# ------------------------------------------------------------
'''
name=input("Enter your name")
num=input("Enter your number")
n=int(input("Enter total no of varireties"))

print('Customer Name: ',name)
print('Contact Number ',num)
# ----------------------------------------------
from datetime import date
print(date.today())
# ----------------------------------------------
total=0
gtotal=0
for i in range(0,n):
    print("item",i)
    price=int(input("Enter price"))
    quan=int(input("Enter quantity"))
    total=price*quan
    gtotal=gtotal+total

    print(price,"\t",quan,'\t',total)

print(gtotal)
if gtotal<1000:
    amt=gtotal
else :
    amt = gtotal*.9
print("final amt:",amt)'''

# ----------------------------------------------------
name=input("Enter your name")
num=input("Enter your number")
n=int(input("Enter total no of varireties"))


price=[]
quan=[]
total=[]
gtotal=0
for i in range(0,n):
    price.append(int(input("Enter price")))
    quan.append(int(input("Enter quantity")))
    total.append(price[i]*quan[i])

print('Customer Name: ',name)
print('Contact Number ',num)
# ----------------------------------------------
from datetime import date
print(date.today())
print("Items\tPrice\tQuantity\tTotal")
for i in range(0,n):
    print("Item",i+1,"\t",price[i],"\t",quan[i],"\t",total[i])
    gtotal=gtotal+total[i]
print("\t\tgrand total=",gtotal)
if gtotal<1000:
    amt=gtotal
else :
    amt = gtotal*.9
print("\t\tDiscount:-",gtotal*.1)
print("\t\tfinal amt:",amt)





# n=int(input("Enter total no of values in list"))
# mylist=[]
# i=0
# while i<n: 
#     mylist.append(input("Enter new element of list"))    
#     i+=1
# print(mylist)


