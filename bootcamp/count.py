import sys
import string

def text_analyzer():
  if len(sys.argv) == 1:
    print("What is the text to analyse?")
    arg = input()
  else:
    arg = sys.argv[1]
  upper = 0
  lower = 0
  letter = 0
  punct = 0
  space = 0
  for i in arg:
    if i in string.printable:
      letter += 1
    if i.isupper():
      upper += 1
    elif i.islower():
      lower += 1
    elif i in string.punctuation:
      punct += 1
    elif i in string.whitespace:
      space += 1
  print("The text contains {} characters:\n".format(letter))
  print("-{} upper letters\n".format(upper))
  print("- {} lower letters\n".format(lower))
  print("- {} punctuation marks\n".format(punct))
  print("- {} spaces".format(space))

if __name__ == '__main__':
  text_analyzer()
