from recipe import Recipe
import datetime
import string

class Book:
  def __init__ (self, name, recipes_list):
    for i in name:
      if string.printable is False:
        print("atr \"name\" has to be of type string")
        return
    self.name = name
    self.creation_time = datetime.date.today()
    self.last_update = datetime.date.today()
    self.repices_list.append()
    
  def get_recipe_by_name(self, name):
    print(Recipe.__str__(name))
    return str(name)
#  def get_recipes_by_types(self, recipe_type):
#    pass
#  def add_recipe(self, recipe):
#    pass
  recipe = property(get_recipe_by_name)
ing = ["carotte", "patte", "levure"]
mira = Recipe("tourte", 3, 12, ing, "", "starter")
book = Book("book1", mira)
#print(tourte)
#print(book.creation_time)
x = Book.get_recipe_by_name(book, mira)

