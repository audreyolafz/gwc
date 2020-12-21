dog_breeds = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
    print(breed)

favorite_foods = ['chocolate', 'matcha', 'ramen', 'pumpkin pie'
                  'crackers', 'kiwi berries', 'cookies', ]
for food in favorite_foods:
    print(food)

for i in range(3):
    print("Warning!")

# infinite loop!!
# my_favorite_numbers = [4, 8, 15, 16, 42]
# for number in my_favorite_numbers:
#     my_favorite_numbers.append(1)
#     break

dog_breeds_available_for_adoption = [
    'french bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'poodle'
for dog in dog_breeds_available_for_adoption:
    print(dog)
    if dog == dog_breed_I_want:
        print("They have the dog I want!")
        break

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for i in big_number_list:
    if i < 0:
        continue
    print(i)

dog_breeds = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
index = 0
while index < len(dog_breeds):
    print(dog_breeds[index])
    index += 1

all_students = ['Alex', 'Briana', 'Cheri', 'Daniele',
                'Dora', 'Minerva', 'Alexa', 'Obie', 'Arius', 'Loki']
students_in_poetry = []
while len(students_in_poetry) < 6:
    students_in_poetry.append(all_students.pop())
print(students_in_poetry)


project_teams = [['Ava', 'Samantha', 'James'],
                 ['Lucille', 'Zed'], ['Edgar', 'Gabriel']]
for team in project_teams:
    for student in team:
        print(student)

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for shop in sales_data:
    for ice_cream in shop:
        scoops_sold += ice_cream
print(scoops_sold)

words = ['@coolguy35', '#nofilter', '@kewldawg54',
         'reply', 'timestamp', '@matchmom', 'follow', '#updog']
usernames = [word for word in words if word[0] == '@']
print(usernames)
messages = [user + "please follow me!" for user in usernames]
print(messages)

my_upvotes = [192, 34, 22, 175, 75, 101, 97]
updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]
print(updated_upvotes)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)
