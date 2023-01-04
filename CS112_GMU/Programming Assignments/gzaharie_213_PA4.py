#-------------------------------------------------------------------------------
#Name: Georgi Zahariev
#Assignment: PA 4
#Due Date: 10/09/2022
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
def indices(some_list, another_list):
	#empty list to record the indexes
	result = []
	
	for num in range(len(some_list)):
		#checking if elements with the same indexes are equal
		if some_list[num] == another_list[num]:
			result.append(num)
	return result

#2
def compute(lst1, lst2, lst3): 
	result = [] 
	#all list are same length
	for num in range(len(lst1)):
		#List 3 is showing what to do +/-
		# if true + , if false -
		if lst3[num]==True:
			result.append(lst1[num]+lst2[num])
		else:
			result.append(lst1[num]-lst2[num])
	return result

#3
def replace_elems(lst1, lst2, n):
	result = [] 
	temp =[]
	#making list 1 always the smaller one for easier work
	if len(lst1)>len(lst2) :
		temp = lst1
		lst1 = lst2
		lst2 = temp
	
	for num in range(len(lst1)):
		#finding the elements that need to be changed
		if (num+1) % n ==0 :
			lst1[num]=lst2[num]
	
	result = lst1
	
	return result

#4
def extra_copies(some_list):
	result = 0   
	#empty list for unique values from the list 
	unique_list = []
	# all values in the given list
	for num in some_list:
		#checking if the value has already been seen in the list
		#if not we are adding it to the unique list
		if num not in unique_list:
			unique_list.append(num)
		#if yes increasing the copies number by 1
		else:
			result+=1
	
	return result
