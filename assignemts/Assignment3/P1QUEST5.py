def Age(age):
    if age <= 18:
        return " you are minor ."
    elif age >=18 and age <=60:
         return"you are adult."
    else:
        return" you are senior citezen."    

user_age=int(input("Enter your age:"))
message=Age(user_age)
print(message)
                   

        
