#-------------------------------------------------------------------------------
#Name: Georgi Zahariev
#Assignment: PA 7
#Due Date: 11/18/2022
#-------------------------------------------------------------------------------
#Honor Code Statement: I received no assistance on this assignment that
#violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
#Comments and Assumptions: A note to the grader as to any problems or
#uncompleted aspects of the assignment, as well as any assumptions about the #
#meaning of the specification. You can write in N/A if you don’t have any
#comments/assumptions.
#-------------------------------------------------------------------------------
#NOTE: width of source code should be <=80 characters to be readable on-screen.
#12345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------


#1
def voterPrecinct(voterFile, voterName):
	string = ""
	try:
		#accessing the file
		file = open(voterFile)
		file.readline()
		#reading all lines as a list
		s_list = file.readlines()
		file.close()
		#closing the file
		if len(s_list)>0:
			for i in range(len(s_list)):
				#check if the voter name is in the list
				if voterName.lower() in s_list[i].strip().lower():
					#if it is, we are creating an output
					lst = s_list[i].split(",")
					string = "Name: "+ lst[0]+ " Precinct: "+lst[3].replace("\n","")
					break
				
	except FileNotFoundError:
		return "File Not Found"
	
	return string

#2
def findPrecinctInfo(precFile, precName):
	string = ""
	try:
		#access the file
		file = open(precFile)
		file.readline()
		s_list = file.readlines()
		#making list of the lines
		file.close()
		#closing the file
		if len(s_list)>0:
			for i in range(len(s_list)):
				lst = s_list[i].split(",")
				element = lst[0]
				#replacing all symbols that are messing our words with " "
				element = element.replace("!","")
				element = element.replace("#","")
				element = element.replace("$","")
				element = element.replace("%","")
				element = element.replace("^","")
				element = element.replace("&","")
				element = element.replace("*","")
				lst[0]=element
				
				if element == precName.lower():
					string = lst[0] + " " + lst[2] + " " + lst[3] +" " + lst[4]
					new_lst = string.split(" ")
					for j in range(len(new_lst)):
						#Making every word to start with an upper case
						new_lst[j] = new_lst[j].replace(new_lst[j][0],new_lst[j][0].upper(),1)
					string = " ".join(new_lst)
					#concatenating all words with capital first letter in a string with " "	
					break
				
	except FileNotFoundError:
		return "File Not Found"
	
	return string

#3	
def pollingPrecincts(precFile):
	try:
		file = open(precFile)
		#opening the file
		file.readline()
		s_list = file.readlines()
		#read all lines as a list
		file.close()
		dct = {}
		#empty dictionary 
		if len(s_list)>0:
		#if not empty
			for i in range(len(s_list)):
				#separating all elements from a row
				info = s_list[i].split(",")
				city = info[4].lower()
				#adding all cities as keys and adding needed values
				if city not in dct:
					dct[city] = [info[0].lower()]
				else:
					dct[city] = dct[city] + [info[0].lower()]
		
			for key in dct:
				#adding to every value the count of the values elements(list elements)
				dct[key] = dct[key] + [len(dct[key])]
			
	except FileNotFoundError:
		return "File Not Found"
	
	return dct

#4
def voter_data(flat_data):
	info = []
	#the list that I will print
	dct = {}
	#dict that I am creating to put as an element in the list
	# as the info is in groups of 3
	for i in range(0,len(flat_data),3):
		dct["Full Name"] = flat_data[i]
		try:
			#checking if the value is between 0 and 1
			if float(flat_data[i+1]) > 0 and float(flat_data[i+1]) < 1 :
				#if yes adding the needed element
				dct["Participation Rate"] = float(flat_data[i+1])
			else:
				#if no raise exception
				raise ValueError()
		except ValueError:
			#making the value of Part. rate 0
			dct["Participation Rate"] = 0
		except IndexError:
			#if not enough elements break
			break
		
		try:
			#checking if the zipcode is between 10000 and 99999
			if int(flat_data[i+2]) > 10000 and int(flat_data[i+2]) < 99999 :
				#if yes add the value
				dct["Zip Code"] = int(flat_data[i+2])
			else:
				#if not, raise exception for incorrect value
				raise ValueError()
		except ValueError:
			#when the value is wrong it is making it 0
			dct["Zip Code"] = 0	
		except IndexError:
			#if not enough elements break
			break
		
		info.append(dct)
		dct = {}
		#making the dict empty, to do the same process again
		
	return info
