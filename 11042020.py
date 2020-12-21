favorite_word = "compassionate"
print(favorite_word)

favorite_fruit = "blackberry"
print(favorite_fruit[0])
print(favorite_fruit[3:8])

first_name = "Rodrigo"
last_name = "Villanueva"
# new_account = last_name[:5]


def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]


new_account = account_generator(first_name, last_name)
print(new_account)

fruit_prefix = "blue"
fruit_suffix = "berries"
fav_fruit = fruit_prefix + fruit_suffix
fruit_sentence = "My favorite fruit is " + fav_fruit
print(fruit_sentence)

length = len(favorite_fruit)
print(favorite_fruit[length-4:])
print(favorite_fruit[-1:])
print(favorite_fruit[-3:])

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]
print(second_to_last)
print(final_word)

# error!
first_name = "Bob"
last_name = "Daily"
# first_name[0] = "R"
fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)


favorite_fruit_conversation = "He said, \"bluberries are my favorite!\""
print(favorite_fruit_conversation)

password = "theycallme\"crazy\"91"


def print_each_letter(word):
    for letter in word:
        print(letter)


favorite_color = "blue"
print_each_letter(favorite_color)


def get_length(string):
    str_len = 0
    for s in string:
        str_len += 1
    return str_len


print(get_length("Hello"))

counter = 0
for char in favorite_fruit:
    if char == "b":
        counter += 1
print(counter)


def letter_check(word, letter):
    for w in word:
        if w == letter:
            return True
            break
    return False


print(letter_check("strawberry", "o"))
print(letter_check("strawberry", "e"))
print(letter_check("strawberry", "a"))
print(letter_check("blueberry", "blue"))
print(letter_check("strawberry", "straw"))


def contains(big_string, little_string):
    return little_string in big_string


print(contains("watermelon", "melon"))
print(contains("watermelon", "berry"))


def common_letters(string_one, string_two):
    letter_string = []
    for char in string_one:
        if (char in string_two) and (char not in letter_string):
            letter_string.append(char)
    return letter_string


print(common_letters("banana", "cream"))
