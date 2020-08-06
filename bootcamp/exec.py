import sys

def inv_case(letter):
  if letter.isupper():
    return letter.lower()
  else:
    return letter.upper()

def rev(str):
  i = 0
  j = 0
  tmp = ''
  new_str = ''
  for letter in str:
    tmp += inv_case(letter)
    i += 1
  i -= 1
  while i >= 0:
    new_str += tmp[i]
    i -= 1
  print(new_str)
  
def main():
  size = len(sys.argv)
  if size > 1:
    i = 1
    str = ''
    while i < size:
      str += sys.argv[i]
      i += 1
      if i != size:
        str += ' '
    rev(str)
 
if __name__ == '__main__':
  main()
