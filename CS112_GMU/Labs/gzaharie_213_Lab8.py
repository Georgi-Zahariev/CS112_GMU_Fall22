#don't modify this function
def fibonacci(n):
    """
    This is a recursive function provided to you.
    Given the value of n,
    it will return the nth Fibonacci number.
    """
    
    #base cases:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #recursive case:
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        #notice how in the recursive case the function calls itself! 
        #this is called recursion, thus this is a recursive function

#don't modify this function
def print_matrix(arr):
    """
    This is a helper function provided to you.
    You can use this to print a
    2D list (matrix) in a nice format.
    """
    for row in arr:
        for item in row:
            print(item, end="\t")
        print()

#************************#
#DEFINE/MODIFY THIS FUNCTION, this is the lab 8 task to complete
def fill_matrix(arr):
	for i in range(len(arr)):
		for j in range(len(arr[i])):
				if i==0 or j==0:
					arr[i][j]="-"
				elif i > j:
					arr[i][j]= round(fibonacci(i) / fibonacci(j), 1)
				elif i < j:
					arr[i][j]= round(fibonacci(j) / fibonacci(i), 1)
				else:
					arr[i][j] = "*"
		   		
	return arr
#************************#


'''Don't change the below code, it is used to test your function
simply running the code in this file after defining fill_matrix(arr) 
should reveal to you whether you pass the below test or not'''
if __name__ == "__main__":
    width = 7
    height = 7
    #creating a 7x7 2D list filled with 0.0 in each row and column
    arr = [[0.0 for _ in range(width)] for _ in range(height)]
    #passing the 7x7 2D list to your function 
    #and storing the function return value in arr
    arr = fill_matrix(arr)

	#if your function fill_matrix() is defined correctly
	#the below is the expected output for a 7x7 2D list 
    expected_arr = [
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "*", 1.0, 2.0, 3.0, 5.0, 8.0],
        ["-", 1.0, "*", 2.0, 3.0, 5.0, 8.0],
        ["-", 2.0, 2.0, "*", 1.5, 2.5, 4.0],
        ["-", 3.0, 3.0, 1.5, "*", 1.7, 2.7],
        ["-", 5.0, 5.0, 2.5, 1.7, "*", 1.6],
        ["-", 8.0, 8.0, 4.0, 2.7, 1.6, "*"],
    ]

	#if your function returns the same 7x7 list as above expected_arr
	#you pass the test case
    if arr == expected_arr:
        print("Test case passed!")
        print("Output : \n")
    #if your function does not match the above expected 7x7 list
    #you are notified via some print statements
    else:
        print("Incorrect!")
        print("Expected output : \n")
        print_matrix(expected_arr)
        print("Your output : \n")

    print_matrix(arr) #prints the 7x7 list YOUR function produced
