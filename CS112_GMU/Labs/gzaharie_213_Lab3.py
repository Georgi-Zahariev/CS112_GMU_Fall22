def calculate_price(a_type, month, base_price): 
	if month!='october' and month!='november' and month!='december' and month!='january' :
		return "entered month is incorrect"
		
	if a_type!='fish':
		return "entered animal is incorrect"
	
	if month=='october' :
		base_price = (base_price * 1.08) * 1.04
	elif month=='november' :
		base_price = (base_price * 1.1) * 1.05
	elif month=='december' :
		base_price = (base_price * 1.12) * 1.065
	elif month=='january' :
		base_price = (base_price * 1.18) * 1.067
		
	return f'Final price is: ${base_price}'
		
	
	