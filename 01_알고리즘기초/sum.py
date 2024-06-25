# find the sum of integer from a to b (use for)

print('a to be , find the sum of integer numbers.')
a = int(input("enter integer a: "))
b = int(input("enter integer b: "))

if a > b:
  a,b = b,a # sort a, b by ascending order, swapping two

sum = 0
for i in range(a, b+1):
  sum += i # add i to sum

print(f'From {a} to {b} sum is {sum}')