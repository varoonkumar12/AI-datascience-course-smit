students = ["Tahir", 44, "AI and Data Science", True]
strings=[]
numbers=[]
booleans=[]

for item in students:
    if isinstance(item,str):
       strings.append(item)
    elif isinstance(item,bool):
        booleans.append(item)
    elif isinstance(item,(int,float)):
        numbers.append(item)
   

print("Strings=",strings)
print("Booleans=",booleans)
print("Numbers=",numbers)

    
