import sys

def main():
  if len(sys.argv) < 2:
    return
  if len(sys.argv) > 2 or sys.argv[1].isnumeric() is False:
    print("ERROR")
    return
  num = int(sys.argv[1])
  if num == 0:
    print("I'm Zero.")
  elif num % 2 == 0:
    print("I'm Even.")
  else:
    print("I'm Odd")

if __name__ == '__main__':
  main()
