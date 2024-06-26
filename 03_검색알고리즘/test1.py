# for i in [[1,2], [10,20], [100,200]]:
#   print(i)



# 단어_사전 = {
#     '하나' : 'one',
#     '둘' : 'two',
#     '셋' : 'three',
# }

# for key,value in 단어_사전.items():
#   print(f'{key}: {value}')



def my_sum(numbers):
  total = 0
  for i in numbers:
    total += i

  return total


print(my_sum([1,2,3,4,5]))


