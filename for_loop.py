# for loops allow us to overcome repetative script
# range(start, stop-1), so range(1, 10) results in 1-9
for i in range(5): # Do something 5 times
	print("Hello") # That something is printing Hello

for num in range (10): # num is just the rolling value
	print(num) #print the current value of num

count = 0 # Value starting at 0


for number in range(1, 4): #1 to 3
	count = count+number

# So to create a function that can take in any size list and return the sum
def sum_list(my_list): #define function sum_list that takes in arguement my_list
	count = 0
	for number in my_list:
		count = count + number

	return count

# assert can be used as error handling
assert sum_list([1,2,3]) == 6 # If function is done correctly, this will not error
assert sum_list([1,2,3,4]) == 10 # If function is done correctly, this will not error