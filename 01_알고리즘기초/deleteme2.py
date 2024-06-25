name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
adult = True

next_year_age = age + 1
name_length = len(name)

if age < 18:
  adult = False
else:
  adult = True

print(f'Hello {name}, you are {age} next year. ')
print( )
       {'grownup' if adult else 'notgrownup'} ' )