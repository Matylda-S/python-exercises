# -*- coding: utf-8 -*-

from itertools import combinations
import math

def cosine(v1,v2):
  '''
    Computes the cosine of the angle between two n-dimensional vectors v1 and v2.

            Parameters:
                    v1 (array-like): The n-dimensional vector.
                    v2 (array-like): The n-dimensional vector.

            Returns:
                    angle (float): The cosine of the angle between v1 and v2 in degrees.
    '''

  n=len(v1)
  scalar=0
  normV1=0
  normV2=0
  cos_angle=0
  angle=0
  for i in range(n):
    scalar=scalar+v1[i]*v2[i]
    normV1=normV1+v1[i]*v1[i]
    normV2=normV2+v2[i]*v2[i]
  normV1=normV1**0.5
  normV2=normV2**0.5
  if normV1 != 0 and normV2 != 0:
        cos_angle = scalar / (normV1 * normV2)
  else:
        return 0
  angle=math.acos(cos_angle)*360/(2*math.pi)
  return angle


def divisible_in_range(a,b,d):
  """
    Returns the list of all integers from the range {a,...,b} that are divisible by the integer d.

    Parameters:
                  a (int): Start of the range.
                  b (int): End of the range.
                  d (int): Integer by which the numbers should be divisible.

    Returns:
            list (List): List of integers from the range {a,...,b} that are divisible by d.
            If d is zero,return empty list
    """
  list=[]
  if d == 0:
        return []
  for i in range(a,b+1):
    if i%d==0:
      list.append(i)
  return list

def common_elements(x,y):
  """
    Returns the list of elements that are common between lists x and y.

    Parameters:
                x (list): The first given list.
                y (list): The second given list.

    Returns:
            list (list): List of elements that are common between x and y.
    """
  return list(set(x) & set(y))

def exclude(letter, string):
  """
    Removes all occurrences of a given letter from a given string.

    Parameters:
                letter (str): The letter to be removed.
                string (str): The input string from which the given letter is to be removed

    Returns:
            new_string (str): The input string with all occurrences of the given letter removed.
    """
  new_string=string.replace(letter,"")
  return new_string


def letters_and_digits(s):
    """
    Calculates the number of letters and digits in a given string s.

    Parameters:
                s (str): The input string for which the count of letters and digits will be calculated.

    Returns:
            tuple: A tuple containing the count of letters (first element) and digits (second element) found in the given string.
    """
    digit = 0
    letter = 0
    for item in s:
        if item.isalpha():
            letter += 1
        elif item.isdigit():
            digit += 1
    return letter, digit


def subsets(s):
  """
    Lists all subsets of a given set x, including the original set and the empty set.

    Parameters:
                x (set): The given set for which subsets will be generated.

    Returns:
            sets (list): A list containing all subsets of the input set x.
    """
  sets=[]
  max_num=len(s)+1
  for i in range(max_num):
    for a in combinations(s, i):
      sets.append(set(a))
  return sets


def mode(s):
  """
    Returns the letter that occurs most frequently in a given string s.

    Parameters:
                s (str): The given string for which the most frequent letter will be determined.

    Returns:
              letter (str): The most frequently occurring letter in the given string s.
    """
  number=0
  letter=''
  for item in s:
    if(item.isalpha()):
      n=s.count(item)
      if(n>number):
        number=n
        letter=item
  return letter

def dec_to_bin(x):
  """
    Converts a given number x represented as a sequence of decimal digits to its binary representation.

    Parameters:
                x (int): The decimal number to be converted to binary.

    Returns:
            result (str): The binary representation of the input decimal number.
            If the input is not a number or is negative number, returns a message that input is invalid.
    """
  if isinstance(x, int) and x >= 0:
        result = bin(x)[2:]
        return result
  else:
        return "Invalid input"

def non_negative(x):
  """
    Removes all negative numbers from a given list of integers x.

    Parameters:
                x (list): The list of integers from which negative numbers will be removed.

    Returns:
            x (list): A new list including only non-negative integers from the given list x.
    """
  a = list(x)
  for item in a:
    if item < 0:
      x.remove(item)
  return x

def no_longer_than(threshold, x):
  """
    Removes all strings longer than a given threshold from a given list of strings x.

    Parameters:
                threshold (int): The maximum length allowed for strings in the given list.
                x (list): The given list of strings from which longer strings will be removed.

    Returns:
            x (list): A new list including only strings that are not longer than the threshold.
  """
  a = list(x)
  for item in a:
    if len(item)> threshold:
      x.remove(item)
  return x


def max_string(x):
  """
    Returns the string of maximal length from a given list of strings x

    Parameters:
        x (list): The list of strings.

    Returns:
        word (str): String of the maximum length from the input list.
  """
  length=0
  word=''
  for item in x:
    if len(item)> length:
      length=len(item)
      word=item
  return word

def alternate(a, b):
  """
    Constructs a list of alternating elements from two lists a and b.

    Parameters:
                a (list): The first given list.
                b (list): The second given list.

    Returns:
        list_of_ab (list): A list containing alternating elements from lists a and b.
        If the lists a and b are not of equal length, returns a string indicating the mismatch.
    """
  lena=len(a)
  lenb=len(b)
  list_of_ab=[]
  if(lena==lenb):
    for i in range(lena):
      list_of_ab.append(a[i])
      list_of_ab.append(b[i])
    return list_of_ab
  else:
    return "the lists aren't of equal length"

def separate_and_sort(x):
  """
    Separates letters and numbers in the given list x, sorts the given list x in such a way that the resulting list contains
at the beginning all strings sorted in alphabetical order, and then all integers sorted in ascending order

    Parameters:
                x (list): The given list containing both integers and strings.

    Returns:
              x (list): The sorted list containing strings sorted alphabetically and integers sorted in ascending order.
    """
  len_of_list=len(x)
  list_of_numbers=[]
  list_of_letters=[]
  for item in x:
    if isinstance(item, int):
          list_of_numbers.append(item)
    elif isinstance(item, str):
          list_of_letters.append(item)

  list_of_numbers.sort()
  list_of_letters.sort()
  x=list_of_letters+list_of_numbers
  return x