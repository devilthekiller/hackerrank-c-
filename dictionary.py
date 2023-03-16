# a={
#     1:33,
#     2:32
# }
# print(a[1])

# a={
#     (1,2,3):30
# }
# print(a[(1,2,3)])

# a={
#     2:20,
#     1:1,
#     3:30,
#     2:91
# }
# print(a)

'''
party = {
    "Vivek" : "Pizza",
    "Ayush" : 23,
    "Jay" : ["Soup", "Main Course", "Gulab Jamun"],
    "Rishi" : ("Dosa", "Pepsi"),
    "Alakh" : {"Dosa", "Pepsi"},
    "Dhiraj" : frozenset({"Rotlo", "Gud", "Buttermilk"}),
    "Marlin" : {"BF" : "Sandwich", "Lunch" : "Punjabi", "Dinner" : "Pau Bhaji"}
}
per=input("Enter the name").capitalize()
# print(party[per])
a=party[per]
# print(type(a))
if type(a)==list or type(a)==tuple or type(a)==frozenset or type(a)==set :
    for obj in a:
        print(obj)
elif type(a)==dict:
    key=input("enter your meal")
    print(a[key])

else:
    print(a)
'''
#subsidy
consumers = ["Darshan", "Nishkal", "Vidhi", "Devanshi", "Harsh"]
subsidy={}
for obj in consumers:
    subsidy[obj]=1000
print(subsidy)