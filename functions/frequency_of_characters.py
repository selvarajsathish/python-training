from collections import OrderedDict
def frequency_of_characters(string):
	"""function to count the number of times of each character and return as dictionary.
    Args:
       string(str): The first parameter.

    Returns:
        Dict: The return value, ordered dictionary with key - character and value - count of character.

    Example:
    	string='Example' |  [('E', 1), ('x', 1), ('a', 1), ('m', 1), ('p', 1), ('l', 1), ('e', 1)]
    """	
	count=0
	Dict=OrderedDict()
	string=string.replace(' ','')
	print string
   	for char in string:
   		count=string.count(char)
   		Dict[char]=count
   	#ordict=collections.OrderedDict(Dict)
 	return Dict

if __name__ == '__main__':
	"""main function to get user input and call frequency_of_characters function.
    """
	string=input("enter a string..:")
	if string.isspace():
		print 'enter a valid string'
	else:
		print frequency_of_characters(string)