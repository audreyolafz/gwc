def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)

print("I am " + str(my_age) + "years old and my dad is " +
      str(dads_age) + " years old")


def get_boundaries(target, margin):
    low_limit = target-margin
    high_limit = target+margin
    return low_limit, high_limit


low, high = get_boundaries(100, 20)
print(str(low) + " " + str(high))

header_string = "Our special is "


def create_special_string(special_item):
    return header_string + special_item + "."


# print(create_special_string("grapes"))

# positional argument: parameters in the correct order
# keyword argument: restate value in function call
# default argument: define value in parameter

def product_calculator(x, y, z=2):
    sums = x + y + z  # create sum
    product = x * y * z  # create product
    return sums, product


#12 is positional
#3 is keyword
#2 is default
sums, product = product_calculator(12, y=3)  # holds values sums and product
print(sums)
print(product)
