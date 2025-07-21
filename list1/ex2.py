# -*- coding: utf-8 -*-

from random import *

def main():
  a=0
  b=0
  for i in range(20):
    number=randrange(10,100)
    a=a+number
    if number>b:
      b=number
  mean=a/20
  print(f"maximum value: {b}")
  print(f"mean: {mean}")


if __name__ == "__main__":
    main()