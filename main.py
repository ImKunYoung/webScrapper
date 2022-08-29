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