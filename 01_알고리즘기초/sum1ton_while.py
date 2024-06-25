# sum 1 to n of integer (using while)

print('Find the sum of 1 to n integers: ')
n = int(input('Enter n: '))

sum = 0
i = 1

while i <= n:
  sum += i
  i += 1


print(f'1 to {n}, the sum is {sum}')
print(f'the value of i is  {i}')
