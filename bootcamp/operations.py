import sys

#work in prgress need error handling

def calculus():
  if len(sys.argv) == 3:
    if sys.argv[1].isnumeric and sys.argv[2].isnumeric:
      n1 = int(sys.argv[1])
      n2 = int(sys.argv[2])
      sum = n1 + n2
      print("Sum:         {}".format(sum))
      diff = n1 - n2
      print("Difference:  {}".format(diff))
      prod = n1 * n2
      print("Product:     {}".format(prod))
      try:
        print("Quotient:    {}".format(n1 / n2))
      except:
        print("err")
      try:
        print("Remainder:   {}".format(n1 % n2))
      except:
        print("err")
    else:
      print("InputError")

if __name__ == '__main__':
  calculus()
