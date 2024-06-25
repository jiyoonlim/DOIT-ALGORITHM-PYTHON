# list12 = [None] * 5
# print(list12)

tuple1 = ()
tuple2 = 1,
tuple3=(3,)
tuple4=1,2,3
tuple5 = tuple('ABC')
tuple6 = tuple([1,2,3])
tuple7=tuple({1,2,3})
tuple8=tuple(range(3,17,2))
# print(tuple8)
# print(type(tuple4))


def max_of(a):
  maximum = a[0]
  for i in range(1, len(a)):
    if a[i] > maximum:
      maximum = a[i]