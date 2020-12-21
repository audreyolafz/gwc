statement_one = (2+2+2 >= 6) and (-1 * -1 < 0)
statement_two = (4*2 <= 8) and (7-1 == 6)
print(statement_one)
print(statement_two)

statement_one = (2-1 > 3) or (-5*2 == -10)
statement_two = (9+5 <= 15) or (7 != 4+3)
print(statement_one)
print(statement_two)

statement_one = not(4+5 <= 9)
statement_two = not(8*2) != 20-4
print(statement_one)
print(statement_two)

names = ['Jenny', 'Alexus']
dogs_names = ['Carter', 'Ralph']
names_and_dogs_names = zip(names, dogs_names)
print(names_and_dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

orders = ['daisies', 'periwinkle']
print(orders)
orders.append('tulips')
orders.append('roses')
print(orders)

items_sold = ['cake', 'cookie', 'bread']
items_sold_new = items_sold + ['biscuit', 'tart']
print(items_sold_new)

broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)


list1 = range(9)
list2 = range(2, 8)
print(list(list1))
print(list(list2))

my_range_2 = range(2, 9, 2)
print(list(my_range_2))

employees = ['Michael', 'Dwight']
print(employees[1])

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pjs', 'books']
beginning = suitcase[2:5]
print(beginning)
start3 = suitcase[:3]
end3 = suitcase[-3:]
after3 = suitcase[3:]
print(start3)
print(end3)
print(after3)

votes = ['Jake', 'Laurie', 'Cassie', 'Jake', 'Jake',
         'Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie']
print(votes.count('Jake'))
