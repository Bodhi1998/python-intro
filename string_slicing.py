string_example = 'hello'

#To get the first letter of a variable
'hello'[0]

#To get multiple
'hello'[0:2]
#Means start at the first and stop before the 3rd index (0,1,2)

#To get the last letter, slice by negative
'hello'[-1]

#To get all letters other than the last, without knowing the length
'hello'[0:-1]

#String slicing has methods built to help with unknown strings
data = 'XBOX 360 | 150 | New'
#For example if variable 'data' has 3 things you'd want separated
#But could be any length, how do you know what to grab
data.index('|') #Will find the first | and determine the index/spot

#We can use this method to create other variables as well to separate the string
product = data[:data.index('|')] #Starts at the beginning til the first |

#This only helps us for the first pipe '|' in the string
#So we have to reset the string to not have the pipe anymore

data = data[data.index('|')+1:].strip()
#This will set the 'data' variable to the data left after the first pipe
#the .strip() method will remove any white space at the beginning of the string
price = data[:data.index('|')] #Finds the next section


condition = data[data.index('|')+1:].strip()



#How to reverse the string
any_string = 'hello'
string_count = any_string.index(any_string[-1])+1
rev_count = string_count-1
reverse = ''

for i in range(string_count):
	reverse = reverse+any_string[rev_count]
	rev_count=rev_count-1

print(reverse)

#How to reverse a string without hurting your head
any_string[::-1] #Steps by 1 starting at the end

#Best way to split up a string separated by a common delimiter
data.split('|') #And can be stored into separate variables
product, price, condition = data.split('|')
#This will split the 'data' variable by the pipe |