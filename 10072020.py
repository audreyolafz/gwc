# relational operators
# ==, !=, >, <, >=, <=

bool_one = 5 != 7
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9


def age_check(age):
    if age >= 13:
        return True
    else:
        return "You must be older than 13."


def grade_calculator(percent_grade):
    if percent_grade >= 90:
        return 'A'
    elif percent_grade >= 80:
        return 'B'
    elif percent_grade >= 70:
        return 'C'
    elif percent_grade >= 60:
        return 'D'
    else:
        return 'F'


# print(grade_calculator(101))
# print(grade_calculator(90))
# print(grade_calculator(80))
# print(grade_calculator(70))
# print(grade_calculator(60))
# print(grade_calculator(59))


def divides(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Can't divide by zero!")


# divides(3, 1)
# divides(9, 8)
# divides(6, 0)

def name_check(name):
    try:
        print(result)
    except NameError:
        print("Can't print name!")


name_check(name="Chicken")
