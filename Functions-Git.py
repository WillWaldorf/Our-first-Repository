#4.13.3: Greeting
# Will Waldorf
#2.6.19
"""
name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print ("It's nice to meet you ! ")

greeting()
"""
'''

# 4.13.4: Functions and Variables
# Will Waldorf
# 2.14.19

x = 11                  q

def print_something():
    x = 13
    print(x)
'''

print_something()
print(x)


# 4.13.5: Functions & Variable - Part 2
# Will Waldorf
# 2.15.19
my_variable = 3.6745

def something():
    print(my_variable + 10)

something()


# 4.13.6: Functions and Variables, Part 3
# Will Waldorf
# 2.18.19

def print_number(x):
    print(str(x))


print_number(90)
print_number('\n'+"Hello World ")q


# 4.14.4: Name and Age
# Will Waldorf
# 2.18.19# 4.14.7: Print mutiple times
# Will Waldorf
# 2.19.19

def print_mutiple_times(string, times):
    for i in range(times):
        print(string)

print_mutiple_times('Hey good looking', 7)

def name_and_age(name, age):
    print('\n' 'Hi, my name is', name + ' and I am ', str(age), 'years old. ')


name_and_age('Willy', 99)
name_and_age('Greg', 1)
name_and_age('Mr Beast', 25)

# 4.14.5: Default Parameter Values
# 2.19.19
# Will Waldorf

def print_two_numbers_(x, y = 20):
    print('First num# 4.14.7: Print mutiple times
# Will Waldorf
# 2.19.19
# 4.14.7: Print mutiple times
# Will Waldorf
# 2.19.19

def print_mutiple_times(string, times):
    for i in range(times):
        print(string)

print_mutiple_times('Hey good looking', 7)

def print_mutiple_times(string, times):
    for i in range(times):
        print(string)

print_mutiple_times('Hey good looking', 7)
ber: ', x)
    print('Second number: ', y)

print_two_numbers_(5, 88)
print_two_numbers_(23)


# 4.14.7: Print mutiple times
# Will Waldorf
# 2.19.19

def print_mutiple_times(string, times):
    for i in range(times):
        print(string)

print_mutiple_times('Hey good looking', 7)

<<<<<<< HEAD
#something different
#more different
=======
>>>>>>> Enter-Name-and-Age

# 4.16.3: Enter a number
# Will Waldorf
# 2.20.19


try:
    my_number = int(input('Enter an integer: '))
    print('Your number: ', str(my_number))

except ValueError:
    print('That was not an integer')

<<<<<<< HEAD
# 4.14.4: Name and Age
# Will Waldorf
# 2.18.19# 4.14.7: Print mutiple times
# Will Waldorf
# 2.19.19
=======
<<<<<<< HEAD
>>>>>>> test-master

def print_mutiple_times(string, times):
    for i in range(times):
        print(string)

print_mutiple_times('Hey good looking', 7)

def name_and_age(name, age):
    print('\n' 'Hi, my name is', name + ' and I am ', str(age), 'years old. ')


name_and_age('Willy', 99)
name_and_age('Greg', 1)
name_and_age('Mr Beast', 25)

# 4.16.7: Enter a positive number
# Will Waldorf
# 2.21.19

<<<<<<< HEAD
def retrieve_postive_number():
    while True:
        try:
            number = int(input('Enter a positive number: '))
            if number >= 0:
                return number
            else:
                print('That number was not positive')

        except ValueError:
            print('That was not a number, silly.')

retrieve_postive_number()
=======
except ValueError:
    print('You must enter a float')
=======
# 4.16.4: Enter Name and Age
# William Waldorf
# 2.20.19

name = input('What is your name: ')

age = -1

try:
    age = int(input('Enter your age: '))
except ValueError:
    print('That was not a valid age')

print('\n''Name: ', name)
print('Age: ', age)
>>>>>>> Enter-Name-and-Age
>>>>>>> test-master
