even_sum = 0
odd_sum = 0

for i in range(1,51):
    if i%2==0:
        even_sum+=i
    else:
        odd_sum += i
print("sum of even numbers from 1 to 50 is:",even_sum )
print("sum of odd numbers from 1 to 50 is :",odd_sum)
