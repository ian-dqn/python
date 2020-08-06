from typing import List

def test(cooking_lvl):
    try:
      x = int(cooking_lvl)
      if cooking_lvl < 1 or cooking_lvl > 5:
        raise ValueError
    except ValueError:
      print("atr \"cooking_lvl\" has to be of type int in rang 1 to 5")
    print(x)
test("two")
