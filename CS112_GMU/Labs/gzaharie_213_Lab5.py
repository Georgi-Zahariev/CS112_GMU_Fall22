def filter_score (dataset):
	max_grade = 0
	max_id = 0	
	number = 0
		
	for num in range(len(dataset)):
		number = dataset[num][2]
		if max_grade < number:
			max_grade = number
			max_id = num
			
	return dataset[max_id]