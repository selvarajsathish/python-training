def sum_of_inputs(x,y):
	"""function to perform sum, if arguments are int or str.

    Args:
       x (int or str): The first parameter.
       y (int or str): The second parameter.

    Returns:
        -1: The return value, when both arguments types are other than int or str.
        x+y:The return value, when both arguments types are either int or str

    Example:
    	x=1,y=2     | return x+y | 3
    	x='a',y='b' | return x+y | ab
    	x='a',y=2   | return  -1 | 'Two inputs should be either integer or string.'

    """
	if (type(x) != int or type(y) !=int) and (type(x) != str or type(y) != str):
		return -1
	else:
		return x+y		

if __name__ == '__main__':
	"""main function to get user input and call sum_of_inputs fuction to perform sum and return value.

    """
	a,b=input("enter a two values to be sum :")		
	ret=sum_of_inputs(a,b)
	if ret == -1:
		print 'Two inputs should be either integer or string.'
	else:
		print ret
