# Boolean is used to determine if something is true or false
# Logic programming is used frequently
# IF statements use this when determining if something should be executed
# For example

if True: # The statement is already True so it will print
	print("True")

if False: # False statement will be skipped
	print("False")

# Comparison operators can be used to check if a condition is true or false
# Equal ==
# Greater Than> 
# Less Than < 
# Less Than or Equal <=
# Greater Than or Equal >=
# Not Equal !=

johnny_hours_worked = 40

if johnny_hours_worked > 40:
	print("Pay him overtime")
# Condition is false since 40 is not greater than 40
# If we set the value to greater than 40
johnny_hours_worked = 42

if johnny_hours_worked > 40:
	print("Pay him overtime")
#Statement is True and prints "Pay him overtime"

# Logic operators
# AND - both conditions are True
# True AND False = False
# True AND True = True

# OR - one or more is True
# False OR False = False
# True OR False = True

# NOT - Negation of condition
# NOT True = False
# NOT False = True
# NOT (True OR False) = False