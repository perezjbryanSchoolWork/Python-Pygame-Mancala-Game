#Bryan Perez
#email: perezjbryan@gmail.com
# This file contains Mancala Board and functions for using it

class MancalaBoardModel:
	
	# constructor:
	# initializes board
	#
	#	[store2]	[12, 11, 10, 9, 8, 7]	store1
	#		[13]    [ 0, 1, 2, 3, 4, 5 ]	[6]
	#
	#						player1					player2
	def __init__(self): #[ 0, 1, 2, 3, 4, 5 ,6    7, 8, 9, 10, 11, 12, 13]
		self.boardgame = [ 4, 4, 4, 4, 4, 4, 0,	  4, 4, 4,  4,  4,  4,  0]
		self.Last_stone_position = 0
		self.tempboardgame = [ 4, 4, 4, 4, 4, 4, 0,	  4, 4, 4,  4,  4,  4,  0]
	
	#Function Boardgame(self)
	#Returns the board game array
	def Boardgame(self):
		return self.boardgame
		
	#Function ReturnHoleValue(self, hole)
	#returns value of specific hole
	def ReturnHoleValue(self, hole):
		if hole < 7:
			return self.boardgame[hole-1]
		if hole >6:
			return self.boardgame[hole]
		
	
	#Function Last_stone_position(self)
	# return the last stone position
	def Last_stone_position(self):
		return self.Last_stone_position
		
	#Function ReturnStores(self)
	# return the 2 stores as a tuple player1's is the first the second is player2's
	def ReturnStores(self):
		storeTuple = (self.boardgame[6], self.boardgame[13])
		return storeTuple
		
	# Function MoveSelected(self, HoleNumber):
	# Moves stones according to selected hole 
	def MoveSelected(self, HoleNumber, playerName):
		if HoleNumber < 7:
			HoleNumber=HoleNumber-1
		
		self.tempboardgame = list(self.boardgame)
		LastPosition = 0
		stones = self.boardgame[HoleNumber]
		self.boardgame[HoleNumber] = 0
		
		if playerName == "Player 1":
			flag = True
		elif playerName == "Player 2":
			flag = False
		
		while  stones != 0:
			
			if flag:
				for index in range(13):
					if index > HoleNumber:
						if stones > 0:
							self.boardgame[index]= self.boardgame[index] + 1
							stones = stones - 1
							LastPosition = index
			
				for index in range(13):
					if stones > 0:
						self.boardgame[index]= self.boardgame[index] + 1
						stones = stones - 1
						LastPosition = index
			
			
			else:
				for index in range(14):
					if index > HoleNumber:
						if stones > 0:
							if index != 6:
								self.boardgame[index]= self.boardgame[index] + 1
								stones = stones - 1
								LastPosition = index
			
				for index in range(14):
					if stones > 0:
						if index != 6:
							self.boardgame[index]= self.boardgame[index] + 1
							stones = stones - 1
							LastPosition = index
		
			
			
			
		#if LastPosition < 6:
		#	self.Last_stone_position =LastPosition+1
		if LastPosition == 6:
			self.Last_stone_position  = 101
		elif LastPosition == 13:
			self.Last_stone_position  = 102
		else:
			self.Last_stone_position = LastPosition
		
		 
		
	
	
	# Function HasStonesLeft(self, Player)
	# Takes in players name checks to see if player has any stones left in his row			
	def HasStonesLeft(self, Player):
		StonesLeft = False;
		total = 0
		
		if Player == "Player 1":
			x=0 
			while x < 6:
				total = total + self.boardgame[x]
				x=x+1
				
			if total > 0:
				StonesLeft = True
		
		if Player == "Player 2":
			x=7 
			while x < 13:
				total = total + self.boardgame[x]
				x=x+1
				
			if total > 0:
				StonesLeft = True
				
		return StonesLeft
	
	#Function LastStoneEmptySpot(self, player)
	#  Last stone placed in an empty spot on your side?  
	#  If so move last stone plus opponents matching hole stones to your store
	def LastStoneEmptySpot(self, player):
		
		if self.Last_stone_position < 101 :
			
			if self.tempboardgame[self.Last_stone_position] == 0:
				
				if player == "Player 1":
					
					if self.Last_stone_position == 0:
						if self.boardgame[12] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[12]
							self.boardgame[12] = 0
							self.boardgame[6] = self.boardgame[6] + 1 + num
					if self.Last_stone_position == 1:
						if self.boardgame[11] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[11]
							self.boardgame[11] = 0
							self.boardgame[6] = self.boardgame[6] + 1 + num
					if self.Last_stone_position == 2:
						if self.boardgame[10] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[10]
							self.boardgame[10] = 0
							self.boardgame[6] = self.boardgame[6] + 1 + num
					if self.Last_stone_position == 3:
						if self.boardgame[9] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[9]
							self.boardgame[9] = 0
							self.boardgame[6] = self.boardgame[6] + 1 + num
					if self.Last_stone_position == 4:
						if self.boardgame[8] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[8]
							self.boardgame[8] = 0
							self.boardgame[6] = self.boardgame[6] + 1 + num
					if self.Last_stone_position == 5:
						if self.boardgame[7] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[7]
							self.boardgame[7] = 0
							self.boardgame[6] = self.boardgame[6] + 1 + num

					
				elif player == "Player 2":
					
					if self.Last_stone_position == 12:
						if self.boardgame[0] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[0]
							self.boardgame[0] = 0
							self.boardgame[13] = self.boardgame[13] + 1 + num
					if self.Last_stone_position == 11:
						if self.boardgame[1] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[1]
							self.boardgame[1] = 0
							self.boardgame[13] = self.boardgame[13] + 1 + num
					if self.Last_stone_position == 10:
						if self.boardgame[2] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[2]
							self.boardgame[2] = 0
							self.boardgame[13] = self.boardgame[13] + 1 + num
					if self.Last_stone_position == 9:
						if self.boardgame[3] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[3]
							self.boardgame[3] = 0
							self.boardgame[13] = self.boardgame[13] + 1 + num
					if self.Last_stone_position == 8:
						if self.boardgame[4] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[4]
							self.boardgame[4] = 0
							self.boardgame[13] = self.boardgame[13] + 1 + num
					if self.Last_stone_position == 7:
						if self.boardgame[5] != 0:
							self.boardgame[self.Last_stone_position]=0
							num = self.boardgame[5]
							self.boardgame[5] = 0
							self.boardgame[13] = self.boardgame[13] + 1 + num

	#Funtion: 	RowToStore(self, player)	
	# Accepts players name and moves all stones in his row to his store
	def RowToStore(self, player):
		if player == "Player 1":
			x=0
			while x < 6:
				self.boardgame[6] = self.boardgame[6] +self.boardgame[x]
				x+=1
		if player == "Player 2":
			x=7
			while x < 13:
				self.boardgame[13] = self.boardgame[13] +self.boardgame[x]
				x+=1				
						
						
	
						
	###################################################################################################################
	#		debug functions
	def printb(self):
		print "[12][11][10][9][8][7]"
		print self.boardgame[12], self.boardgame[11], self.boardgame[10], self.boardgame[9], self.boardgame[8], self.boardgame[7]
		print self.boardgame[0], self.boardgame[1], self.boardgame[2], self.boardgame[3], self.boardgame[4], self.boardgame[5]
		print "[1][2][3][4][5][6]"
		print "player 1 store: ", self.boardgame[6]
		print "player 2 store: ", self.boardgame[13]
		print " "
	
	def printt(self):
		print " PREVIOUS BOARD#################################"
		print self.tempboardgame[12], self.tempboardgame[11], self.tempboardgame[10], self.tempboardgame[9], self.tempboardgame[8], self.tempboardgame[7]
		print self.tempboardgame[0], self.tempboardgame[1], self.tempboardgame[2], self.tempboardgame[3], self.tempboardgame[4], self.tempboardgame[5]
		print "player 1 store: ", self.tempboardgame[6]
		print "player 2 store: ", self.tempboardgame[13]
		print " PREVIOUS BOARD#################################"
		