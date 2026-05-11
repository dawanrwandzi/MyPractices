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


# Challenge - crate 5 variable is whith diffrent data types
# 1- your age
# 2- your hight
# 3- your name
# 4- are you a student?
# 5- somthing with no value yet

age = 27
height = 181.4
name = "Dawan"
is_student = True
something = None

my_profile = {"age": age,
              "hight": height,
              "name": name,
              "is student": is_student,
              "sometheng": something}

for key, value in my_profile.items():  # loop
    v_type = type(value).__name__  # the type of data
    # the length of value - just for str
    v_length = len(value) if isinstance(value, str) else "N/A"
    # to get new lines
    print(f"{key}:{value} | type: {v_type} | length: {v_length}")
'''

# string methods
# 1- Types - (type(), str()) - bulit-in function
# 2- Math - (len(), count()) - len is built-in function
# 3- Transformations - (replace(), 'H' + 'i', f{}, split(), 'h' * 2,
# -  Extraction ('cat' [0], 'cat' [1:3])) - count is Method of <str-class>
# 4- Cleaning - Clean whitespaces - (istrip(), rstrip(), strip())
# -  Clean cases - (lower(), upper()) - rstrip is Method of <str-class>
# 5- Search - (startswhith(), endswith(), find(), 'a' in 'cat') - startswhith is Method of <str-class>
# 6- Validation - (isalpha(), isnumeric())

# 1- Type() - built in function
name = "Dawan"
print(type(name))

age = 27
print(type(age))
print("Your Age is: " + str(age))

# 2- Math
password = "123ahd3"
print(len(password))

if (len(password)) < 8:
    print("Your Password is too Short!")
else:
    print("Your Password is Good!")

text = "Python is easy to learn." \
    "Python is powerfull." \
    "Many people love python"

print(text.count("python"))

# 3- Transformations
price = "1234,56"
print(price.replace(",", "."))  # replace

price = "$1,899.99"
print(price.replace("$", "").replace(",", ""))   # double replace none

phone = "750-329-1919"
print(phone.replace("-", " "))  # replece space

phone2 = "+964 (750) 123-4567"
print(phone2.replace("+", "").replace(" ", "")
      .replace("(750)", "750").replace("-", ""))

first_name = "Dawan"
last_name = "Nihmat"
last_name = first_name + " " + last_name
print(last_name)    # join 2 str

# f-string
name = "Soran"
age = 27
is_student = False
print(
    f"My name is {name}, I'm {age} years old and My student status is {is_student}.")

print(f"2 + 3 = {2 + 3}")

# split
date = "6-5-2026 06:54"
print(date.split("-"))

csv_file = "1234,Max,Kurdistan,1-1-2000,M"
print(csv_file.split(","))

# data extraction (indexing & slicing)
text = "python"
print(text[0])  # indexing
print(text[0:3])    # slicing
print(text[0:4:2])  # [start:end:step]

date = "06-05-2026"
print(date[3:5])

# cleaning - whitespace cleanup
text = " Engineering".lstrip()  # left space
print(text)

text = "Engineering ".rstrip()  # right space
print(text)

text = " Engineering ".strip()  # both space
print(text)

text = "Data Engineering".strip()   # not middle space removed
print(text)

text = "##Data##".strip("#")    # remove (#)
print(text)

text = "  Engineering"
print(len(text))
print(len(text.strip()))

nr_of_spaces = len(text) - len(text.strip())
is_clean = len(text) == len(text.strip())
print("Number of spaces:", nr_of_spaces, "\n" "Is my data clean?", is_clean)

# Case conversions
text = "python PROGRAMMING"
print(text.lower())
print(text.upper())

# Example
name = "988-Maria," .strip("988-,").lower()
role = "( Data Engineering );;".strip().strip("();;").lower()
age = 27
print("Name:", name, "| " "Role:", role, "| " "Age:", age)

# Search
phone = "+965-750-12345"
print(phone.startswith("+964"))

email = "dawan@gmail.com"
print(email.endswith("gmail.com"))

print("@" in email)

# fined
phone1 = "+964-740-12345"
phone2 = "964-740-12345"
phone3 = "00964-740-12345"
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])

# Validating
country = "Kurdistan"
print(country.isalpha())

phone = "037-929261984"
print(phone.isnumeric())
