def sum_list(lst):
	amount = 0
	for num in range(len(lst)-1):
		amount += lst[num]
	return amount

def ones_digit(number):
	return number % 10
	
def check_correctness(*numbers):
	number_sum = sum_list(numbers)
	last_digit = ones_digit(number_sum)
	
	if last_digit == numbers[-1]:
		return "correct"
	else:
		return "error"
	
	
	
		
	
	

	
	
