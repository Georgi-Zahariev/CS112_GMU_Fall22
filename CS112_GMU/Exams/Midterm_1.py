def weight_on_neptune(earth_weight):
	new_weight = earth_weight * 1.125
	return new_weight

def travel_cost(miles):
	if miles <= 50:
		return 3
	elif miles <= 100:
		return 6
	elif miles < 500:
		return 8
	elif miles <= 1000:
		return 10
	else:
		return 12


def fact_evens(n):
	result = 1
	if n < 2:
		return result
	else:
		for nums in range(2,n+1,2):
			result = result * nums
		return result
