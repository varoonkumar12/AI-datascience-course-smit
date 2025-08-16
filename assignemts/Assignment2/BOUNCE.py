

a, b = 0, 1

print("First 10 Fibonacci numbers:")

# Print first two numbers
print(a, b, end=" ")

# Loop from 3rd to 10th term
for i in range(2, 10):
    c = a + b
    print(c, end=" ")
    a, b = b, c
