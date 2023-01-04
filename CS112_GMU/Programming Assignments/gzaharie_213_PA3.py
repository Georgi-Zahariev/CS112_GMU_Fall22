#-------------------------------------------------------------------------------
#Name: Georgi Zahariev
#Assignment: PA 3
#Due Date: 09/25/2022
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

# Number 1
def composite_ratio(x):
	count_factors = 0
	#going through all numbers from 1 to the X number
	# if statement shows whether it is a factor
	#count_factors is counting the factors
	for elements in range(x):
		if x % (elements+1) == 0:
			count_factors+=1
	
	compo_ratio = x/count_factors	
	return compo_ratio
    
# Number 2
def vowels_count(letters):
	#counters 
	count_a = 0
	count_e = 0
	count_i = 0
	count_o = 0
	count_u = 0
	
	#Go through all elements in the list to count every vowel
	for let in letters:
		if let=='a' or let=='A' :
			count_a+=1
		elif let=='e' or let=='E' :
			count_e+=1
		elif let=='i' or let=='I' :
			count_i+=1
		elif let=='o' or let=='O' :
			count_o+=1
		elif let=='u' or let=='U' :
			count_u+=1
	
	#Find out the highest count
	result_str = ''
	if count_a>count_e and count_a>count_i and count_a>count_o and count_a>count_u :
		result_str = f'Most Frequent: \'a\' Count: {count_a}'
	elif count_e>count_a and count_e>count_i and count_e>count_o and count_e>count_u :
		result_str = f'Most Frequent: \'e\' Count: {count_e}'
	elif count_i>count_a and count_i>count_e and count_i>count_o and count_i>count_u :
		result_str = f'Most Frequent: \'i\' Count: {count_i}'
	elif count_o>count_a and count_o>count_i and count_o>count_e and count_o>count_u :
		result_str = f'Most Frequent: \'e\' Count: {count_e}'
	else :
		result_str = f'Most Frequent: \'u\' Count: {count_u}'
	
	return result_str

# Number 3
def wacky_factors(f_list, big_list):
	# Checking if the elements in the first list
	# are factors of the elements in the longest list
	# num_facs counts the factors
	num_facs = 0
	for number in big_list:
		for num in f_list:
			if number % num == 0:
				num_facs+=1

	return num_facs
                
# Number 4
def add_em_up(bottom, top):
	counter = 0
	num_plus = 1
	
	#Adding the num_plus to the bottom number while it is lower than the top
	# counter is counting how many times the program is adding
	while bottom < top :
		bottom = bottom + num_plus
		counter += 1
		num_plus +=1
	
	#if it is different than 0 
	if counter!=0:
		counter -= 1
		
	return counter 
	