# Dictionaries allow you to pair data together using key:value setup
# For example, a phone book would have a name(key):phone number (value)
# dict[key] --> value
# Stored using {}
phone_book1 = {'qazi':'123-456-7890', 'bob':'222-222-2222', 'cat':'333-333-3333'}

# This can be created this way to make the code more readable
# Also makes it easier to add addtional values based on the keys
phone_book = {
	'qazi':['123-456-7890', 'qazi@qazi.com'],
	'bob':['222-222-2222', 'bob@bob.com'],
	'cat':['333-333-3333', 'cat@cat.com']
	}
# Now we have a dictionary that contains three keys (qazi, bob, cat)
# And each key contains a list of elements
# And each list contains two elements

# Now that we've stored a few key:value pairs, we can tap into the values using the keys
print(phone_book1['qazi']) #will print out the value of the key 123-456-7890

print(phone_book['qazi']) #will print out the list of values phone and email

# If we only want a single item in the list of values
print(phone_book['qazi'][1]) #Will index the 2nd value (0, 1) from the list
# resulting in printing his email qazi@qazi.com