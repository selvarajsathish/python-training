def find_type_arg(value):
	"""function to find type of argument.

    Args:
       value : any type of parameter ie. int,str,float..,.
 
    Returns:
        type of value : The return value.
        
    Example:
    	value  | return 
    	2      | <type 'int'>

    """	
	print type(value)

if __name__ == '__main__':
	"""main function to get user input and call find_type_arg fuction to print type of value.
	
    """
	arg=input("enter a arguement to find its type :")
	find_type_arg(arg)
