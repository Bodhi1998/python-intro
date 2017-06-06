# Function problems
# Define a function that finds the greater number of two
def bigger_num(num1, num2):
	if num1 > num2:
		return num1
	else:
		return num2

# Define a function that finds the greater of 3 numbers using previous function
def biggest_num(a, b, c):
	return bigger_num(bigger_num(a, b), c)

# How this works is, it will find the bigger number of a and b
# Using the previously defined function, and then use the function
# A 2nd time to find the bigger number between the result of the first
# And the left over value of c