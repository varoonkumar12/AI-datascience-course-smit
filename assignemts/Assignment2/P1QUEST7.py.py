Num1=float(input("Enter value of number one:"))
Num2=float(input("Enter value of number two:"))
opt=input("Enter your operator:")
if opt=='+':
    print("Answer",Num1+Num2)
elif opt=='-':
    print("Answer",Num1-Num2)
elif opt=='*':
    print("Answer",Num1*Num2)
elif opt=='/':
     if Num2 !=0:
         print("Answer",Num1/Num2)
     else:
          print("Divisible is not possible")
else:
    print("wrong operator")
          
