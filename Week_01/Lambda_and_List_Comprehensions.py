my_function = lambda a, b, c : a + b
print(my_function(1, 2, 3))

# Let's iterate from 0 to 999 and return the even numbers.
my_list = []
for number in range(0, 1000):
    if number % 2 == 0:
        my_list.append(number)
print(my_list)

# Now the same thing but with list comprehension.
my_list = [number for number in range(0,1000) if number % 2 == 0]
print(my_list)