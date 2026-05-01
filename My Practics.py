# This is Print Function
'''
a = 5
b = 5
total = a+b
print("the sum is ", total)

print("Hi \"PYTHON\"")

print("""Your Learning Path:
    -python basics 
    -data enginering 
    -AI""")

# Function
Villa_1 = 140.000
Villa_2 = 150.000

Villa_1_Area = 220
Villa_2_Area = 220

Villa_1_Price = 900
Villa_2_Price = 1050

subtotal = Villa_1_Area*Villa_1_Price + Villa_2_Area*Villa_2_Price
print("subtotal is", subtotal)

discount = subtotal * 0.10
print("Discount is ", discount)

total = subtotal-discount
print(total)


# Variables
x = 2
y = x + 3
print(y)

name = "Dawan"
language = "Python"
print(" My name is", name, "\n",  # "\n" To New Line
      name, "Wants to learning", language, "\n",
      name, "learning", language, "expert")  # Don't Reapit it, Name it

# Not Space Like https://
name = "@DawanData"
website = ".com"

print(f"info{name}{website}""\n"
      f"support{name}{website}""\n"
      f"www.{name}{website}")

# Input ()
name = input("Enter Your Name: ")   # Dynamic value
password = input("Input Your Password: ")
country = "Kurdistan"    # Hard-coded (static) value
print(f"Name is {name}", "\n"
      f"Password is {password}", "\n"
      f"He is from {country}")


# Collection (Variables & Input & Print) functions
x = 5
y = int(input("Enter your number:"))
z = x + y
print(z)


# Data Type
# 1- no value (none)

# 2- single value
# a = 10 (int),
# b = 3.14 (float),
# c = "hello" (str),
# d = True (bool),
# e = date and time(date, time, datetime)

# 3- multi-value
# a = list [1,2,3] - you can change, add and remove info
# b = set {1,2,3} - not replace the duplicates info
# c = tuple (1,2,3) - like list but not change it,
# after you create it you can't change it
# d = dict {'a':1, 'b':2} - stores data in key:value using specific key
# e = array ('i', [10,20]) - unlike lists all elements to be of the same data type

name = "dawan"
number = 10
print(type(name))  # class (the type of)
print(type(number))

name = "dawan"
number = 10
print(name.upper())  # upper (capital) - just for str
print(len(name))  # len - just for str
print(number.bit_length())  # return the length of binary 01 - not for str
'''

# Challenge - crate 5 variable is whith diffrent data types
# 1- your age
# 2- your hight
# 3- your name
# 4- are you a student?
# 5- somthing with no value yet

age = 27
hight = 181.4
name = "Dawan"
is_student = True
something = None

my_profile = {"age":age,
              "hight":hight,
              "name":name,
              "is student":is_student,
              "somtheng":something}
              
for key, value in my_profile.items():
    print(f"{key}:{value}")