Num=int(input("Enter your number:"))
if Num%2==0 and Num%3==0:
    print("Number is divisible By both")
elif Num%2==0:
    print(f"{Num}Number is divisible by 2")
elif Num%3==0:
    print(f"{Num} Number is divisible by 3")

else:
    print("Number is not divisible")
