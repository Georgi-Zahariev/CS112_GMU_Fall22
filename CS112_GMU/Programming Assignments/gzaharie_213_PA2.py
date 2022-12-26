#-------------------------------------------------------------------------------
#Name: Georgi Zahariev
#Assignment: PA 2
#Due Date: 09/19/2022
#-------------------------------------------------------------------------------
#Honor Code Statement: I received no assistance on this assignment that
#violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
#Comments and Assumptions: A note to the grader as to any problems or
#uncompleted aspects of the assignment, as well as any assumptions about the #
#meaning of the specification. You can write in N/A if you don’t have any
#comments/assumptions.
#-------------------------------------------------------------------------------
#NOTE: width of source code should be <=80 characters to be readable on-screen.
#12345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------


#function 1
def gas_price(prev_price, new_price):
	if new_price/prev_price<=1 : #That means equal or less
		return 'Full Tank'
	elif new_price/prev_price<1.2 : # less than 20% difference
		return '3/4 Tank'
	elif new_price/prev_price<1.8 : #less than 80% difference
		return 'Half Tank'
	elif new_price/prev_price<2 : #less than 100% difference
		return '1/4 Tank'
	else:
		return 'Go Home' # 100% and more difference
		
#function 2
#for every difficulty there are points that you need to level up
def level(num_coins, difficulty):
	if difficulty=='Beginner': #Beginners need 4 points to increase their level
		return int(num_coins/4)
	elif difficulty=='Amateur':	#Amateurs need also 4 
		return int(num_coins/4) 
	elif difficulty=='Intermediate': #Intermediates need 6 per level
		return int(num_coins/6) 
	elif difficulty=='Pro':	#Pros - 6
		return int(num_coins/6)
	elif difficulty=='Expert':	#Experts - 8
		return int(num_coins/8)
	elif difficulty=='Legendary':	#Legendaries - 10
		return int(num_coins/10)


#Function 3

def card_game(player1_card, player2_card, tiebreak_with_card):
	#I am using variables for the number of the card and the suit for each player
	card_num1=0
	card_num2=0
	card_suit1=0
	card_suit2=0
	#Finding number and suit of player 1
	if player1_card<14 :
		card_suit1=1
		card_num1=player1_card
	elif player1_card<27 :
		card_suit1=2
		card_num1=player1_card-13
	elif player1_card<40 :
		card_suit1=3
		card_num1=player1_card-26
	else :
		card_suit1=4
		card_num1=player1_card-39
	
	#Finding number and suit of player 2
	#The same operation as for the player 1
	if player2_card<14 :
		card_suit2=1
		card_num2=player2_card
	elif player2_card<27 :
		card_suit2=2
		card_num2=player2_card-13
	elif player2_card<40 :
		card_suit2=3
		card_num2=player2_card-26
	else :
		card_suit2=4
		card_num2=player2_card-39
	
	#Who is winning
	#There are situations that I am explaining in the code 
	#card1 is bigger and suit1 is lower
	if card_num1>card_num2 and card_suit1<card_suit2: 
		return 'Player 1 Wins'
	elif card_num2>card_num1 and card_suit1>card_suit2:	#card2 is bigger and suit2 is lower
		return 'Player 2 Wins'
	elif tiebreak_with_card == True and card_num1>card_num2:	#Using the card solution 
		return 'Player 1 Wins'
	elif tiebreak_with_card == True and card_num1<card_num2:
		return 'Player 2 Wins'
	elif tiebreak_with_card == False and card_suit1<card_suit2:	#Using the suit solution 
		return 'Player 1 Wins'
	elif tiebreak_with_card == False and card_suit1>card_suit2:
		return 'Player 2 Wins'
	else:
		return 'Tie' # When nothing from the upper things happen the result is tie
	
	

	
	
	

	