import random
import math
# Chapter 3 - work with numbers
# 1- Types - (type(), int(), float(), comblex()) - built in function

x = 5
y = 5.7
z = 3 + 2j

print(type(x))
print(type(y))
print(type(z))

# 2- Math operators (3+2, 3-2, 3*2, 3/2, 3//2, 3%2, 3**2) - operators
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 % 2)
print(3 ** 2)

# 3- Rounding numbers
price = 35.542379
print(round(price))
print(round(price, 2))
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))
print(int(price))

# 4- Random
print(random.random())
print(random.randint(1, 10))

# 5- Validation
x = 7.0
print(x.is_integer())

y = 7.1
print(y.is_integer())

x = 70.50
print(isinstance(x, int))
print(isinstance(x, float))

# Challange - generate a random even number between 0 and 100
even_numbers = random.randrange(0, 101, 2)
print(even_numbers)
