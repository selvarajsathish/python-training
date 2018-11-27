
def sum_of_inputs(a,b):           # To calculate the sume of given value.
		c=a+b
		return c

def find_type_arg(input1,input2): # To find the type of arguments given.
	x,y=type(input1),type(input2)
	if (x!= y):
		return -1

if __name__ == '__main__':
	a,b=input("enter a two values to be sum :")		
	ret=find_type_arg(a,b)        # called function to find type of arguments given by user.
	if ret == -1:
		print 'Two inputs should be either integer or string.'
	else:
		print sum_of_inputs(a,b)  # called the fucntion to calculate the sume of given value.
	
