# Chapter 4 - logic and oprators
# 2- Contrl flow:
# 2- Boolean Expressions:
# 1- Values (True, False)
# 2- Functions (bool(), any(), all(), isinstance(), etc.)
# 3- Comparison operators (==, !=, >, <, >=, <=)
# 4- Logical operators (and, or, not)
# 5- Identity operators (is, is not)
# 6- Membership operators (in, not in)


# 1- Values (True, False)
print(True)
print(False)
print(type(True))
print(bool(0))  # False (0 is considered False)
print(bool())  # False (empty value)
print(bool(""))  # False (empty string)
print(bool(None))  # False (None value)

# 2- Functions (bool(), any(), all(), isinstance(), etc.)
email = ""
phone = "750-123-4567"
username = ""
print(any([email, phone, username]))  # True (phone is not empty)
print(all([email, phone, username]))  # False (email and username are empty)
print(isinstance(email, str))  # True (email is a string)
print(isinstance(123, str))  # False (123 is an integer, not a string)

# 3- Comparison operators (==, !=, >, <, >=, <=)
3 > 2  # True
3 < 2  # False
3 == 3  # True
3 != 2  # True

x = 5
y = 10
print(x < y)  # True
print(x > y)  # False
print(x <= y)  # True
print(x >= y)  # False
print(x == y)  # False
print(x != y)  # True
print(len("hi") == 3)  # False
print("a" < "b")    # True (lexicographical order)
print("a" == "b")   # False
print("a" == "A")   # False (case-sensitive)
print(1 < 4 < 6)  # True (chained comparison)
print(1 < 4 > 6)  # False (chained comparison)

age = 25
print(18 < age < 30)  # True (age is between 18 and 30)
print(age == 25 != 30)  # True (age is 25, not 30)


# 4- Logical operators (and, or, not)
print(3 > 2 and 5 < 2)  # False (first condition is True, second is False)
print(3 > 2 and 5 > 2)    # True (first condition is True, second is True)

print(3 > 2 or 5 < 2)   # True (first condition is True, second is False)
print(3 < 2 or 5 < 2)   # False (both conditions are False)

print(not 3 > 2)  # False (3 > 2 is True, so not True is False)
print(not 3 < 2)  # True (3 < 2 is False, so not False is True)
print(not False)  # True (not False is True)

# Excute control
is_raining = True
is_sunny = False
is_windy = True
# True (is_sunny and not is_windy is False, but is_raining)
print(is_raining or is_sunny and not is_windy)
# False (is_raining or is_sunny is True, but not is_windy is False)
print((is_raining or is_sunny) and not is_windy)

# 5- membership operators (in, not in)
print("o" in "python")  # True (the letter 'o' is in the string "python")
# False (the string "dawan" is in the set {"ali", "dawan", "sara"})
print("dawan" not in {"ali", "dawan", "sara"})

# 6- Identity operators (is, is not)
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True (a and b have the same content)
print(a is b)  # False (a and b are different objects in memory)
c = a
print(a is c)  # True (a and c refer to the same object in memory)
print(a is not b)  # True (a and b are different objects in memory)
