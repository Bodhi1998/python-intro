

bob_hours_worked = 40

if bob_hours_worked > 39: #if bob worked more than 39 hours then execute following
	print('he worked overtime')


johnny_homework = True
johnny_throw_out_garbage = True

if johnny_homework and johnny_throw_out_garbage:
	print('Johnny can play XBOX-ONE')

not(johnny_homework or not(johnny_throw_out_garbage)) #False

#rock paper scissors
human = 'rock'
computer = 'scissors'

if human == 'rock' and computer == 'scissors': #Checks first statment for True
	human_score = 1
elif human == 'bananas' or computer == 'bananas': #Checked if first statement was False
	human_score = 0
	computer_score = 0
	print("You must pick rock, paper, or scissors")
else: #If all previous statements result in False
	print("No winner")