#Lists can store multiple items
#Lists also do not limit what type of data is stored
groceries = ['apple', 'banana', 5, 6, 'oranges']

#We can view what data are in each position using their index
groceries[0] #First spot, results in 'apple'

#If we want to split up a string by a specific delimiter
#We can use the .split() command and store into a list

string_example = 'This-is-an-example-string'
string_example.split('-') #results in a printed list of 5 separate words
#We can store these results by defining it as another variable

string_list = string_example.split('-')
print(string_list)

#We can add to the list by using the .append method
numbers = [1,2,3,4,5]
numbers.append(6) #Will add the number 6 to the end of the list

#If you wanted to add a set # of items into the list, you can use a for loop
numberlist=[]
for i in range(100):
	numberlist.append(i)

#To see what a potential range will generate, you can use the following
print (list(range(10)))
#Which will show [0,1,2,3,4,5,6,7,8,9]
#So if you wanted a specific range of numbers to be added such as 6 to 30...
for i in range(6,31): #Since the range will begin at the 6 and end before 31
	numbers.append(i)