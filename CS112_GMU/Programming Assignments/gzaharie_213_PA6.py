#-------------------------------------------------------------------------------
#Name: Georgi Zahariev
#Assignment: PA 6
#Due Date: 10/29/2022
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
#using default arguments when creating the function 
def shift_elems(elems, rt_shift = 1, filler = "X"):
	#j is how many times will the numbers be shifter
	for j in range(rt_shift):
		for i in range(len(elems) - 1,-1, -1):
			#shifting every number staring from the last
			if i == 0:
				#putting filler where as a value for the first element
				elems[i]=filler
			else:
				elems[i]=elems[i-1]
	return elems

#2
def find_mode(value_list):
	mode_list = []
	mode_dict = {}
	
	#Using dictionary to see how many times every element occurs
	for i in value_list:
		if i not in mode_dict:
			# if not exists
			mode_dict[i] = 1
		else:
			#if exists increase by 1
			mode_dict[i] = mode_dict[i] + 1
	
	max_times = 0
	#finding the highest value in the dictionary
	for value in mode_dict.values():
		if value > max_times:
			max_times = value
	#appending the keys that are seen the most in a list		
	for key,value in mode_dict.items():
		if value == max_times:
			mode_list.append(key)
	
	return mode_list
		
#3
def find_median(value_list):
	if len(value_list)==0:
		return None
	#if odd numbers, the median is the number in the middle
	elif len(value_list) % 2 == 1:
		return value_list[len(value_list)//2]
	else:
		#if even number when need to take the average of 2 numbers
		# that are closest to the middle
		lower_num = value_list[len(value_list)//2 - 1]
		upper_num = value_list[len(value_list)//2]
		median = (lower_num + upper_num)/2
		return median

#4
def averages(values_list):
	#using find_mode
	mode = find_mode(values_list)
	
	#sorting my list with nested loop
	#comparing every element with the elements after it
	#if there is an element that is smaller than it
	#they are switching places
	for elem in range(len(mode)):
		for other in range(elem + 1,len(mode),1):
			if mode[elem] > mode[other]:
				#switching places of two elements
				temp = modet[elem]
				mode[elem]=mode[other]
				mode[other]=temp
	
	#using find_median
	median = find_median(values_list)
	sum_num = 0
	#finding sum of the elements
	for elem in values_list:
		sum_num += elem
	
	if len(values_list)==0:
		mean = None
	else:
		#finding mean (average)
		mean = round((sum_num/len(values_list)),2)
		
	
	return {'mode':mode, 'median':median, 'mean':mean}

#5
#recursion	
def add_chars(some_list, some_str):
	#creating the base
	new_list = []
	#when to stop
	if len(some_list) == 0:
		return new_list
	else:
		#in all other cases
		new_list.append(some_list[0])
		if len(some_str)>0:
			#steps 
			#append letter if there are letters from the word left
			new_list.append(some_str[0])
			some_list.remove(some_list[0])
			# add to the list called function by recursion
			#calling the function with new elements
			#removed element from the list, and sliced word
			new_list += add_chars(some_list, some_str[1:])
		else:
			#When there is no word left,
			#we are calling the function with empty string
			#and don't add letter to our word
			some_list.remove(some_list[0])
			new_list += add_chars(some_list, "")
	
	return new_list
	
