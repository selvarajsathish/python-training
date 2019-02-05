def frequency_of_characters(string):
    """function to count the number of times of each character and prints the output.
      Args:
         string(str): The first parameter.

      Returns:
          Dict: The return value, dictionary with key - character and value - count of character.

      Example:
        string='Example' |  [('E', 1), ('x', 1), ('a', 1), ('m', 1), ('p', 1), ('l', 1), ('e', 1)]
      """ 
    char_cnt = 0
    str_dict = {}
    string = string.replace(' ','')
    for char in string:
      char_cnt = string.count(char)
      str_dict[char] = char_cnt
    return str_dict
  


if __name__ == '__main__':
    """main function to get user input and call frequency_of_characters function to print output.
      """
    string = input("enter a string..:")
    if string.isspace():
      print 'enter a valid string'
    else:
      print frequency_of_characters(string)