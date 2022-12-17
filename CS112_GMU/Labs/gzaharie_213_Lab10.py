def reformDate(date):
	lst = date.split(" ")
	months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
	try:
		if int(lst[0][0:2]) < 1 or int(lst[0][0:2]) > 31:
			raise ValueError
			
		if lst[1] not in months.keys():
			raise ValueError
		
		if len(lst[2]) != 4:
			raise ValueError
				
	except ValueError:
		return "The input is invalid "
	else:
		res = "Data is: "  + str(lst[2])+ "-"+ months[lst[1]] + "-"+ lst[0][0:2]
		return res
	