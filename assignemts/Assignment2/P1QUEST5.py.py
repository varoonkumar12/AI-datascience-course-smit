Age=int(input("Enter your age:"))
if(Age<=18):
    print("you are minor ",Age)
elif(Age>=18 and Age<=60):
     print("you are adult ",Age)
else:
    print("you are senior citizen")
