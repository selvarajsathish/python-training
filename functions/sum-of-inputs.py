def sum_of_inputs(x,y):                 # To calculate the sume of given value.	
	if (type(x) != int or type(y) !=int) and (type(x) != str or type(y) != str):
		return -1
	else:
		return x+y		

if __name__ == '__main__':
	a,b=input("enter a two values to be sum :")		
	ret=sum_of_inputs(a,b)              # called function to find type of arguments and perform sum, given by user.
	if ret == -1:
		print 'Two inputs should be either integer or string.'
	else:
		print ret
