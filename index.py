from math import *
#Variables
length = 7
width = 5
area = width * length
print(f'If the length of a rectangle is {length}, and the width is {width}, then the area is {area}')

#Lists
favorite_animals = ["Dog", "Cat", "Monkey", "Rabbit"]
favorite_animals[3] = "Snake"
favorite_animals.remove("Cat")
favorite_animals.append("Owl")
print(favorite_animals)

#Functions
def cube(number):
    result = number ** 3
    return print(result)

cube(5)

def by_three(number1):
    if number1 % 3 == 0:
        return cube(number1)
    else:
        return print("False")  

by_three(4)
by_three(6)

#Functions Extra
cost = 0
discount_value = 0
def padel_court_cost(hours, court_type):
    if court_type == "Indoors" and hours >= 3:
       cost = 30 * hours
       discount_value = (cost / 100) * 20
       cost = cost - discount_value
    elif court_type == "Outdoors" and hours >= 3:
        cost = 20 * hours
        discount_value = (cost / 100) * 20
        cost = cost - discount_value
    elif court_type == "Indoors":
        cost = 30 * hours
    elif court_type == "Outdoors":
        cost = 20 * hours     

    return print(cost)

padel_court_cost(4, "Outdoors")
padel_court_cost(2, "Indoors")
        
#Functions and Loops
def printer(Elements):
    for element in Elements:
        print(f"{element}C°")

printer([24, 35, 5, 46, 13])

def to_celcius(temperatures):
    c_list = []
    for temp in temperatures:
        t_converted = (temp - 32) * (5 / 9)
        c_list.append(t_converted)

    return print(c_list)

to_celcius([112, 80, 76])

#Functions Advanced
def sec_min(seconds):
    minutes = seconds / 60
    return print(f"{seconds} seconds is {minutes} minutes")
sec_min(120)
sec_min(435)  

def is_odd(number2):
    if number2 % 2 == 0:
        return print(True)
    else:
        return print(False)

is_odd(25)
is_odd(24)

my_list = [12, 32, 2, 22, 55, 8]
print((lambda x: x[0] + x[-1])(my_list))

def is_array_length_even(my_list1):
    list_len = len(my_list1)
    if list_len % 2 == 0:
        return print(True)
    else:
        return print(False) 

is_array_length_even([420, 69, 80, 0])
is_array_length_even([21, 69, 7])

def highest_score(grades):
    highest_grade = None
    for grade in grades:
        if highest_grade is None or highest_grade < grade:
            highest_grade = grade
    return print(highest_grade)        

highest_score([21, 12, 30, 55, 18, 40])
#Another very silly way to solve the above problem
def highest_score2(grades2):
    grades2.sort()
    return print(grades2[-1])
highest_score2([24, 15, 34, 50, 18, 40])

def missing_num(num_list):
    expected = range(min(num_list), max(num_list)+1)
    return print(set(expected) - set(num_list))           
missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10])