# print
print("Hi")

# variable
a = 2
b = 3
c = a + b
print(c)

# camelCase
myAge = 23

# snake_case
my_Age = 23

# Data Type
my_name = "KunYoung"
print(my_name)

a = True
print(a)

# review
print("..........review..........")
my_name = "KunYoung"
age = 12
dead = False
live = True

print(my_name)
print(age)
print(dead)
print(live)

print("Hi I'm", my_name)
print("and I'm", age, "years old")

# function
print("..........function..........")
print(True)
print(12)


def say_hello():
    print("how r u?")


say_hello()

# Indentation (들여쓰기)
print("..........Indentation..........")


def say_bye():
    print("bye bye")
    say_hello()


def say_bye():
    print("bye bye")


say_hello()

# Parameters
print("..........Parameters..........")


def say_hello(name):
    print(name)


say_hello("hello")


def say_age(age):
    print("and I'm", age, "years old")


say_age(23)

# Multiple Parameters
print("..........Multiple Parameters..........")


def say_multi(name, age):
    print("and I'm", name, "years old", "and I'm", age, "years old")


say_multi("KunYoung", 23)

# review
print("..........review..........")


def tax_calculator(income, tax):
    print(income * tax)


income = 150000000
tax = 0.2
tax_calculator(income, tax)

# Default Parameters
print("..........Default Parameters..........")


def say_hello2(user_name="anonymous"):
    print("hello", user_name)


say_hello2("KunYoung")
say_hello2()


def plus(a=0, b=0):
    print(a + b)


def square(a=0, b=0):
    print(a ** b)


def divide(a=0, b=1):
    print(a / b)


def minus(a=0, b=0):
    print(a - b)


def multiply(a=0, b=0):
    print(a * b)


print("..........plus..........")
plus(2, 4)
plus(2)
plus()

print("..........minus..........")
minus(2, 4)
minus(2)
minus()

print("..........multiply..........")
multiply(2, 4)
multiply(2)
multiply()


print("..........divide..........")
divide(2, 4)
divide(2)
divide()


print("..........square..........")
square(2, 4)
square(2)
square()
# - * / **


# Return Values
print("..........Return Values..........")
def tax_calc(money):
    return money * 0.35

def pay_tax(tax):
    print("thank you for paying", tax)

to_pay = tax_calc(15000000)

pay_tax(to_pay)
pay_tax(tax_calc(15000000))

# Return Recap
print("..........Return Recap..........")
my_name = "kunyoung"
my_age = 22
my_color_eyes = "brown"

print("Hello I'm" + my_name + ", I have {my_age} years in the earth, {my_color_eyes} is my eye color")

# 위에걸 직관적으로 표현
print(f"Hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color")
print("Hello I'm {my_name}, I have {my_age} years in the earth, {my_color_eyes} is my eye color")


def make_juice(fruit):
    return f"{fruit}+🎆"

def add_ice(juice):
    return f"{juice}+😊"

def add_sugar(iced_juice):
    return f"{iced_juice}+🐒"

juice = make_juice("🍔")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)