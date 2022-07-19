#program for calculating factorial
print("enter the number")
o = int(input())
p = 1

for i in range(1,o+1):
    p = p*i
print("The factorial of",o," is",p)
