def encode(s,d):
  '''
    Encode a given string using the Caesar cipher with a given
shift parameter d

            Parameters:
                    s (str): The given string.
                    d (int): The shift parameter

            Returns:
                    encoded_string (str): The encoded string
    '''
  if d>26:
    d=d-26  
  encoded_string=""
  for item in s:
    if item.isalpha():
      shifted_letter=ord(item)+d
      if item.islower():
          if(shifted_letter>122):
              shift=shifted_letter-122
              shifted_letter=96+shift
      elif(shifted_letter>90):
              shift=shifted_letter-90
              shifted_letter=64+shift   
      a=item.maketrans(item,chr(shifted_letter))
      encoded_string+=item.translate(a)
    else: encoded_string+=item
  return encoded_string 

def decode(s,d):
  '''
    Decode a given string using the Caesar cipher with a given
shift parameter d

            Parameters:
                    s (str): The given string.
                    d (int): The shift parameter

            Returns:
                    decoded_string (str): The decoded string
    '''
  if d>26:
    d=d-26
  decoded_string=""
  for item in s:
    if item.isalpha():
      shifted_letter=ord(item)-d
      if item.islower():
          if(shifted_letter<97):
              shift=97-shifted_letter
              shifted_letter=123-shift
      elif(shifted_letter<65):
              shift=65-shifted_letter
              shifted_letter=91-shift 
      a=item.maketrans(item,chr(shifted_letter))
      decoded_string+=item.translate(a)
    else: decoded_string+=item  
  return decoded_string 


def main():
  s = input("Enter the string to encode/decode: ")
  d_1 = input("Enter the shift: ")
  if not d_1.isdigit():
        print("Shift has to be an intiger")
        return
  d=int(d_1)
  choice=(input("Enter 'e' if you want to encode and 'd' if you want to decode: "))
  if choice=='e':
      print("Result:", encode(s, d))
  elif choice == 'd':
        print("Result:", decode(s, d))
  else:
        print("Invalid input. Enter 'e' or 'd' ")


if __name__ == "__main__":
    main()