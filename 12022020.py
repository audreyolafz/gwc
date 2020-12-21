favorite_song = 'SmOoTH'
favorite_song_lowercase = favorite_song.lower()
print(favorite_song_lowercase)

poem_title = "spring storm"
poem_title_fixed = poem_title.title()
print(poem_title_fixed)

poem_author = "William Carlos Williams"
poem_author_fixed = poem_author.upper()
print(poem_author_fixed)

epic_string = "Once upon a time"
epic_list = epic_string.split()
print(epic_list)

greatest_guitarist = "santana"
greatest_list = greatest_guitarist.split('n')
print(greatest_list)

authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer"
author_names = authors.split(',')
author_last_names = []

for name in author_names:
    author_last_names.append(name.split()[-1])
print(author_last_names)

smooth_chorus = \
    """And if you said,
    "This life ain't good enough."""
smooth_chorus.split("\n")
print(smooth_chorus)

my_munequita = ['My', 'Spanish', 'Harlem']
munequita = ' '.join(my_munequita)
print(munequita)

reapers_line_one_words = ["Black", "reapers", "with",
                          "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = ' '.join(reapers_line_one_words)
print(reapers_line_one)

featuring = "                                    rob thomas        "
print(featuring.strip(''))

love_maybe_lines = ['Always     ', '     in the middle of our bloodiest battles    ', 'you lay down your arms',
                    '               like flowering mines       ', '\n', '           to conquer me home.           ']
love_maybe_lines_stripped = []
for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip())
love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)

with_spaces = "You got the kind of loving that can be so smooth"
with_underscores = with_spaces.replace(' ', '_')
print(with_underscores)

print('smooth'.find('t'))
print('smooth'.find('oo'))

god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find('disown')
print(disown_placement)


def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)


print(favorite_song_statement("Long Live", "Taylor Swift"))


def poem_title_card(poet, title):
    return "The poem \"{}\" is written by {}.".format(title, poet)


print(poem_title_card("Walt Whitman", "I Hear America Singing"))
