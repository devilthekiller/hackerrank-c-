par = int(input("Enter PAR"))
s = int(input("Enter STROKES"))

print("score is :")
if (s == 1):
        print("HOLE IN ONE!!!!!!!!!!!!!!")

elif (s == par):
        print("PAR")

elif (par <= 0 or s <= 0):
        print("Invalid!!!!!!!!!!!! ")

elif (s == par - 1 or s == par - 2):
        print("BIRDIE")

elif (s == par - 3 or s == par - 4):
        print("EAGLE")

elif (s == par + 1 or s == par + 2):
        print("BOGEY")

elif (s == par + 3):
        print("DOUBLE BOGEY")

else:
        print("GO HOME YOU FOOL!!!!!!!!!!!")
