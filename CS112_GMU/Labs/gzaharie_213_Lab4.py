def print_triangle(height):
	triangleString=''
	multiple = 1
	for i in range(height):
		if i < height - 1:
			triangleString = triangleString + multiple * '*' + '\n'
		else:
			triangleString = triangleString + multiple * '*'
			
		multiple = multiple + 2
				
	return triangleString
	