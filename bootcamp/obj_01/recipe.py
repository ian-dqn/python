import string

class Recipe:
  def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
    for i in name:
      if i in string.printable is False:
        print("atr \"name\" has to be of type string")
        return
    self.name = name
    try:
      self.cooking_lvl = int(cooking_lvl)
      if cooking_lvl < 1 or cooking_lvl > 5:
        print("atr \"cooking_lvl\" has to be of type int in rang 1 to 5")
        return
    except ValueError:
      print("atr \"cooking_lvl\" has to be of type int in rang 1 to 5")
      return
    try:
      self.cooking_time = int(cooking_time)
      if cooking_time < 0:
        print("atr \"cooking_time\" has to be a positive number")
        return
    except ValueError:
      print("atr \"cooking_time\" has to be a positive number")
    try:
      for i in ingredients:
        if i in string.printable is False:
          print("atr \"ingredients\" has to be a list of strings")
        if len(i) <= 1:
          print("atr \"ingredients\" has to be a list of strings")
    except ValueError:
      print("atr \"ingredients\" has to be a list of strings")
      return
    self.ingredients = ingredients
    if recipe_type == "starter" or recipe_type == "lunch" or recipe_type == "dessert":
      self.recipe_type = recipe_type
    else:
      print("recipe type has to be a string with value \"starter\", \"lunch\" or \"dessert\"")
      return
    self.description = str(description)
   # print("define obj work")
    
  def __str__(self):
      txt = ""
      txt += "Name:               "
      txt += self.name
      txt += "\nCooking level:      "
      txt += str(self.cooking_lvl)
      txt += "\nCooking time:       "
      txt += str(self.cooking_time)
      txt += "\nIngredients:        "
      for s in self.ingredients:
        txt += s
        txt += ", "
      txt += "\n"
      if len(self.description) > 0:
        txt += "Description:        "
        txt += self.description
        txt += "\n"
      txt += "Recipe Type:        "
      txt += self.recipe_type
      return txt

ing = ["carotte", "patte", "levure"]

tourte = Recipe("tourte", 3, 12, ing, "", "starter")
#to_print = str(tourte)
#print(tourte)
#print(to_print)
