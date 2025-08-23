fruits=["apple","raspberry","pineapple","cherry"]
#partA
if "aaple" in fruits:
    print("'apple' is present at index of ",fruit.index("apple"))
else:
    print("'apple' is not presentin list")
    
#partB
fruits[1:3]=["orange"]
print("after replacement",fruits)

#partC
fruits.insert(2,"apricot")
print("after inserting",fruits)

#partD
fruits.extend(["car","bike","aeroplane"])
print("final list",fruits)
