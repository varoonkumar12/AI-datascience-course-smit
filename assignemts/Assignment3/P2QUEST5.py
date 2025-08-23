Numbers =[32,54,66,11,77,10.90]
#partA
for n in Numbers[:]:
    if n<20:
        Numbers.remove(n)
print("after removing",Numbers)

#partB
Numbers.sort()
print("Ascending",Numbers)

#partC
average= sum(Numbers)/len(Numbers)
print("average",average)             
    

