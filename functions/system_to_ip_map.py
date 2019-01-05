def system_to_ip_map(sys_names,ips):
	"""function to map system with ip address and return as dictionary.
    Args:
       sys(tuple): The first parameter -system names
       ips(tuple): The second parameter -ip address of system

    Returns:
        Dict: The return value, ordered dictionary with key - system name and value - ip address.

    Example:
    	sys_names='system1','system2'
    	ips='192.168.1.2','192.168.1.3'

    	[('system1', '192.168.1.2'), ('system2', '192.168.1.3')]
    """	
	ip_mapped_dict=zip(sys_names,ips)
	return ip_mapped_dict

if __name__ == '__main__':
	"""main function to get user input and call system_to_ip_map function.
    """
	sys_names=(input('enter a system names in tuple format : '))
	ips=(input('enter a system ips in tuple format : '))
	if sys_names==' ' or ips==' ':
		print "atleast one systen name and ip should be entered"
	else:
		print system_to_ip_map(sys_names,ips)
