# name = input("Please enter your name: ")
# age = int(input("Please enter your age: "))
# print(f'Hello  {name}! You are {age} years old')


# x = 5.0
# print(type(x))

# a = 5
# b = 3.0
# print(f'{a+b}')


# s = ['a', 'b', 'c', 'd', 'e', 'f']
# print(s[2:5])


# s = "hello"
# print(s.capitalize())

# print(2 ** 3)

# l = [1,2,3,4,5]
# print(len(l))
# print(l[-1::])


# text = "Python Programming"
# print(len(text))
# print(text[0])
# print(text[-1])

# person = {"name": "John", "age": 30, "city": "New York"}
# print(person["name"])
# print(len(person))


# a = 3
# b = 2
# print(f'sum: {a+b}, subtraction: {a-b}, division: {a/b}, multiplication: {a*b}')



# def hello(name): 
#   print(f'hello {name}')

# name = input("please enter your name: ")
# print(hello(name))



# name = input('enter name: ')
# def hello(name):
#   return f'hello {name}'

# # result = hello(name)
# print(hello(name))


# x = [2, 4, 8, 16, 32, 64, 128]
# print(list(zip(x, x[1:], x[2:])))

# # sum([1, 2], [10, 20], [100, 200]) # error
# sum(sum([[1, 2], [10, 20], [100, 200]])) # 출력: 333



a = 'pithon'
 
def 함수1():
    def 함수2():
        print('love')
 
    print('I') # 1번
    함수2() #2번
    return "python" #3번
 
 
a = 함수1()
print(a)