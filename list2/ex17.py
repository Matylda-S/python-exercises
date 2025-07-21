def sortbyname(users):
  '''
     Sort the given dictionary in which each user is assigned their address by user name and return the result as a list

            Parameters:
                    users (dict): A dictionary where keys are user names (str) and values are their addresses (str)

            Returns:
                    result (list): A list of tuples sorted by user name
    '''
  sort=lambda x: sorted(x.items())
  result = sort(users)
  return result

def sortbyadress(users):
  '''
     Sort the given dictionary in which each user is assigned their address by user adress and return the result as a list

            Parameters:
                    users (dict): A dictionary where keys are user names (str) and values are their addresses (str)

            Returns:
                    result (list): A list of tuples sorted by user adress 
    '''
  sort=lambda x: sorted(x.items(),key=lambda x: x[1])
  result = sort(users)
  return result

def main(): 

  users = {
          "Harry": "Main Street",
          "Alex": "Garden Street",
          "James": "Knockturn Alley",
          "Suzan": "Diagon Alley",
          "Lily": "Great Peter Street"
  }

  print(sortbyname(users))
  print(sortbyadress(users))

if __name__ == "__main__":
    main() 