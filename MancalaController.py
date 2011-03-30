#Bryan Perez
#email: perezjbryan@gmail.com
# This file contains the mancala game logic

import MancalaBoardModel, PlayerModel




class MancalaController:

	def __init__(self):
		self.board = MancalaBoardModel.MancalaBoardModel()
		self.Current_Player = PlayerModel.PlayerModel("Player 1")
		self.Other_Player = PlayerModel.PlayerModel("Player 2")
	

	

	def ContinueGame(self):
		return self.board.HasStonesLeft(self.Other_Player.PlayerName())
		

	def ReturnHoleValue(self, hole):
		self.board.printb()
		return self.board.ReturnHoleValue(hole)
		
	def ReturnStoresValue(self):
		return self.board.ReturnStores()
		
	def ReturnPlayerScores(self):
		player1 =0 
		player2 =0
		
		if self.Current_Player.PlayerName() == "Player 1":
			player1 = self.Current_Player.Score()
			print "player 1: ", self.Current_Player.Score()
		elif self.Other_Player.PlayerName() == "Player 1":
			player1 = self.Other_Player.Score()
			print "player 1: ", self.Other_Player.Score()
			
		if self.Current_Player.PlayerName() == "Player 2":
			player2 = self.Current_Player.Score()
			print "player2: ", self.Current_Player.Score()
		elif self.Other_Player.PlayerName() == "Player 2":
			player2 = self.Other_Player.Score()
			print "player 2: ", self.Other_Player.Score()
			
		scoreTuple =(player1, player2)
		return scoreTuple
		
	def ReturnPlayerTurn(self,):
		return self.Current_Player.PlayerName()
	
	def PlayerSelectsHole(self, hole):
		self.board.MoveSelected(hole, self.Current_Player.PlayerName())
		# Last stone placed in an empty spot on your side? 
		self.board.LastStoneEmptySpot(self.Current_Player.PlayerName())			
		# Updates Players Score
		Store = self.board.ReturnStores()
		if self.Current_Player.PlayerName() == "Player 1":
			Score = self.Current_Player.Score()
			Score = Store[0]
		elif self.Current_Player.PlayerName() == "Player 2":
			Score = self.Current_Player.Score()
			Score = Store[1]
		self.Current_Player.SetScore(Score)
		# if last stone was placed in the players store another turn is given
		if self.board.Last_stone_position < 14:
			temp = self.Current_Player
			self.Current_Player = self.Other_Player
			self.Other_Player = temp

		

	
	
	def EndofGameLogic(self):
		# Moves Other_Players remaining stones to his store
		self.board.RowToStore(self.Other_Player.PlayerName())
		# Update other players score
		Store = self.board.ReturnStores()
		if self.Other_Player.PlayerName() == "Player 1":
			Score = self.Current_Player.Score()
			Score = Store[0]
		elif self.Other_Player.PlayerName() == "Player 2":
			Score = self.Current_Player.Score()
			Score = Store[1]
		self.Other_Player.SetScore(Score)
	
	def DetermineWinner(self):
		# Player with most stones wins
		if self.Other_Player.Score() == self.Current_Player.Score():
			return "tie"
		elif self.Other_Player.Score() > self.Current_Player.Score():
			return self.Other_Player.PlayerName()
		else:
			return self.Current_Player.PlayerName()
	

'''
#############################################
# Copy of original controller without UI
#############################################

# Funtion main():
# Contains the logic of the game mancala
def main():
	
	board = MancalaBoardModel.MancalaBoardModel()
	Current_Player = PlayerModel.PlayerModel("Player 1")
	Other_Player = PlayerModel.PlayerModel("Player 2")
	

	
	while board.HasStonesLeft(Other_Player.PlayerName()) :
		
		#------------------------------------------------------------------#
		# Display board
		board.printb()
		#------------------------------------------------------------------#
		# Player selects the hole
		print Current_Player.PlayerName(), "Your Turn"
		print " "
		SelectedHole = int(input("Enter choice"))
		#------------------------------------------------------------------#
		# Calculates Players move & sets last stone postion
		board.MoveSelected(SelectedHole, Current_Player.PlayerName())
		#------------------------------------------------------------------#
		# Last stone placed in an empty spot on your side? 
		board.LastStoneEmptySpot(Current_Player.PlayerName())			
		#------------------------------------------------------------------#
		# Updates Players Score
		Store = board.ReturnStores()
		if Current_Player.PlayerName() == "Player 1":
			Score = Current_Player.Score()
			Score = Score + Store[0]
		elif Current_Player.PlayerName() == "Player 2":
			Score = Current_Player.Score()
			Score = Score + Store[1]
		Current_Player.SetScore(Score)
		# Updates Board 
		board.printb()
		#------------------------------------------------------------------#
		# if last stone was placed in the players store another turn is given
		if board.Last_stone_position < 14:
			temp = Current_Player
			Current_Player = Other_Player
			Other_Player = temp
		#------------------------------------------------------------------#
		# Updates Board 
		board.printb()
		
	
	#------------------------------------------------------------------#
	# Moves Other_Players remaining stones to his store
	board.RowToStore(Other_Player.PlayerName())
	#------------------------------------------------------------------#
	# Update other players score
	Store = board.ReturnStores()
	if Other_Player.PlayerName() == "Player 1":
		Score = Current_Player.Score()
		Score = Score + Store[0]
	elif Other_Player.PlayerName() == "Player 2":
		Scores = Current_Player.Score()
		Score = Score + Store[1]
	Other_Player.SetScore(Score)
	#------------------------------------------------------------------#
	# Player with most stones wins
	if Other_Player.Score() > Current_Player.Score():
		print Other_Player.PlayerName(), " Wins"
	else:
		print Current_Player.PlayerName(), " Wins"
	
if __name__ == "__main__":
	main() 
	
'''
	

	
