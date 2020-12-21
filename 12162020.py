# def shopping(groceries):
#     print(groceries)


# grocery_list = "Sugar cookies, apples, chips"
# shopping(grocery_list)

# print_statement = print("hi")
# print(print_statement)

# def create_user(username, is_admin=False):
#     create_email(username)
#     set_permissions(is_admin)
# #error!!
# user2 = create_user('djohansen')

# def log_message(logging_style="shout", message="", font="Times", date=None):
# if logging_style == 'shout':
##       message = message.upper()

# def add_author(author_books, current_books=None):
#     if current_books is None:
#         current_books = []


# def scream_and_whisper(text):
#     scream = text.upper()
#     whisper = text.lower()
#     return scream, whisper


# the_scream, the_whisper = scream_and_whisper("Hi")

# print(the_scream)
# print(the_whisper)

# def truncate_sentences(length, *sentences):
#     for sent in sentences:
#         print(sent[:length])


# truncate_sentences(5, "It is Wednesday", "Happy Holidays!",
#                    "Merry Christmas", "It's almost 2021")

def remove(filename, *args, **kwargs):
    with open(filename) as file_obj:
        text = file_obj.read()
        for arg in args:
            text = k.replace(arg, "")
        for kwarg, replacement in kwargs.items():
            text = text.replace(kwarg, replacement)
        return text
    print(remove("text.txt", "generous", "gallant",
                 fond="amused by", Robin="Mr. Robin"))
