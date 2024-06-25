print('a to b sum of integer')
a = int(input("enter integer a: "))
b = int(input("enter integer b: "))

if a > b:
  a,b = b,a

sum = 0
for i in range(a, b):
  print(f'{i} + ', end='')
  sum += i


print(f'{b} = ', end='')
sum += b

print(sum)
