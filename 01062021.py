class CoolClass:
  pass

class Musician:
  title = "Rockstar"
drummer = Musician()
print(drummer.title)

class Dog:
  dog_time_dilation = 7
  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = ()
pipi_pitbull.time_explanation()

class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."
student = Rules()
print(student.washing_brushes())

class DistanceConverter:
  km_in_a_mile = 1.609

calculate area of circle given circumference
class Circle:
  # pi = 3.14
  def __init__(self, diameter):
    print("New circle with diamter: " + str(diameter))
  def area(self, radius):
    pi = 3.14
    radius /= 2
    area = pi * radius ** 2
    return area
circle = Circle()
pizza_area = circle.area(12)
teaching_table_area = circle.area(36)
round_room_area = circle.area(11460)
print(pizza_area, teaching_table_area, round_room_area)

teaching_table = Circle(36)
print(teaching_table)

class Shouter:
  def __init__(self, phrase):
    if type(phrase) == str:
      print(phrase.upper())
shout1 = Shouter("shout")
shout2 = Shouter("shout!!")

class FakeDict:
  pass
fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"
working_string = "{} {}".format
class store:
  pass
alternative_rocks = store()
isabelles_ices = store()
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

print(alternative_rocks.store_name)
print(isabelles_ices.store_name)

class NoCustomAttributes:
  pass
attributesless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")  