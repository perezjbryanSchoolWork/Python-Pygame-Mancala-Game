#Bryan Perez
#email: perezjbryan@gmail.com
# This file contains the player model


class PlayerModel:
	
	# constructor:
	# initializes player's Name, score, last stone postions variables
	def __init__(self, playerName):
		self.playerName = playerName
		self.score = 0
		self.Last_stone_position = 0
	
	#Function: playerName(self)
	#returns player name
	def PlayerName(self):
		return self.playerName
		
	#Function: score(self)
	#returns player's score
	def Score(self):
		return self.score
		
	#Function: setScore(self)
	# sets players score
	def SetScore(self, score):
		self.score = score
