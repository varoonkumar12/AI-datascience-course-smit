def Number(num1,num2,num3):
    if num1>num2 and num1>num3:
        print("num1 is largest ;" ,num1)
    elif num2> num1 and num2>num3:
        print("num2 is largest ;",num2)
    else:
        print("num3 is largest ;",num3)

check_num1=int(input("Enter your Num1:"))
check_num2=int(input("Enter your Num2:"))
check_num3=int(input("Enter your Num3:"))
Number(check_num1,check_num2,check_num3)
