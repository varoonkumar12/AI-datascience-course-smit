Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]
#partA
strings=[]
numbers=[]
for item in Gadgets:
    if isinstance(item,str):
        strings.append(item)
    else:
        numbers.append(item)

print("strings=",strings)
print("numbers=",numbers)

#partB
strings.sort()
print("in ascending form=",strings)

strings.sort(reverse=True)
print("in deascending form=",strings)

#partC
strings.sort(key=len)
print("string length=",strings)

#partD
numbers.sort()
print("number in ascending form=",numbers)

numbers.sort(reverse=True)
print (" numbers in deascending form=",numbers)
    
    
