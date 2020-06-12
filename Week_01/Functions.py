# 1st example
def add_numbers(x, y):
    return x + y

add_numbers(1, 2)
# Added by Fabio Retorta
print(add_numbers(1, 2))

# 2nd example
def add_numbers2(x,y,z=None):
    if (z==None):
        return x+y
    else:
        return x+y+z

print(add_numbers2(1, 2))
print(add_numbers2(1, 2, 3))

# 3rd example
def add_numbers3(x, y, z=None, flag=False):
    if (flag):
        print('Flag is true!')
    if (z==None):
        return x + y
    else:
        return x + y + z
    
print(add_numbers3(1, 2, flag=True))

# 4th example
def add_numbers4(x,y):
    return x+y

a = add_numbers4
a(1,2)