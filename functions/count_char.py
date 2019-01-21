def count_char(string,char):
	"""function to count the given character from given string.

    Args:
       string(str): The first parameter.
       char(char): The second parameter.

    Returns:
        -1: The return value, when entered charecter is not present in string.
        count: Number of count given charater in given string.

    Example:
    	string='hello selva',char='a'     | return count | 1
    	string='hello selva',char='x'     | return -1
    	
    """	
	if char not in string:
		return -1

	count=0
	for character in string:
		if character==char:
			count+=1
	return count

if __name__ == '__main__':
	"""main function to get user input and call count_char function.
    """
	string=input("enter a string..:")
	char=input("enter a characer to find in string..:")
	ret=count_char(string,char)
	if ret== -1:
		print "given character not present in given string"
	else:
		print ret