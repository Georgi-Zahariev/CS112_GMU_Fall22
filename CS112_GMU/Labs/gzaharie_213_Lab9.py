def fileIO(fileInputPath):
	file_in = open(fileInputPath, "r")
	results = []
	for line in file_in:
			
		lst = line.split(" ")
		first_num = int(lst[4])
		second_num = int(lst[7])
		third_num = int(lst[9])
		res = first_num
		if lst[5] == "multiplied":
			res = int(res * second_num)
		else:
			res = int(res / second_num)
			
		if lst[8]=="plus":
			res = res + third_num
		else:
			res = res - third_num
		
		result = "Result: " + str(res)
		
		results.append(result)
		
	file_out = open("fileOutput.txt","w")
	
	for i in results:
		file_out.write(str(i) + "\n" )
	file_out.close()
	
		
	
			
		
			
		
	