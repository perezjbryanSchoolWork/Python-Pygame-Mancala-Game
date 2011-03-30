#Bryan Perez
#email: perezjbryan@gmail.com
# This file contains the main game loop for the mancala game and functions for the UI

import pygame, sys, os, MancalaController# ,MyRNG
from pygame import K_1,K_2, K_3, K_4,K_5,K_6,K_7,K_8,K_9,K_0,K_MINUS,K_EQUALS,K_h

##########################################
##Intializes various items for the game
##########################################
pygame.init()
clock = pygame.time.Clock()
width = 745
height = 430
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mancala!')
running = 1
#rand = MyRNG.MyRNG() 
LEFT = 1
bgcolor = ( 0, 0, 0)
game = MancalaController.MancalaController()
helpflag = False

##############################################

##########################################
## Loads Images for the games
##########################################
#board and holes images
board_path = os.path.join("images","board.jpg") 
board = pygame.image.load(board_path)
he_path = os.path.join("images","e.jpg") 
he = pygame.image.load(he_path).convert()
h1_path = os.path.join("images","1.jpg") 
h1 = pygame.image.load(h1_path).convert()
h2_path = os.path.join("images","2.jpg") 
h2 = pygame.image.load(h2_path).convert()
h3_path = os.path.join("images","3.jpg") 
h3 = pygame.image.load(h3_path).convert()
h4_path = os.path.join("images","4.jpg") 
h4 = pygame.image.load(h4_path).convert()
h5_path = os.path.join("images","5.jpg") 
h5 = pygame.image.load(h5_path).convert()
hm_path = os.path.join("images","m.jpg") 
hm = pygame.image.load(hm_path).convert()
'''
#alternative holes images
h1a_path = os.path.join("images","1a.jpg") 
h1a = pygame.image.load(h1a_path).convert()
h2a_path = os.path.join("images","2a.jpg") 
h2a = pygame.image.load(h2a_path).convert()
h3a_path = os.path.join("images","3a.jpg") 
h3a = pygame.image.load(h3a_path).convert()
h4a_path = os.path.join("images","4a.jpg") 
h4a = pygame.image.load(h4a_path).convert()
h5a_path = os.path.join("images","5a.jpg") 
h5a = pygame.image.load(h5a_path).convert()
hma_path = os.path.join("images","ma.jpg") 
hma = pygame.image.load(hma_path).convert()
'''
#stores
se_path = os.path.join("images","se.jpg") 
se = pygame.image.load(se_path).convert()

s1_path = os.path.join("images","s1.jpg") 
s1 = pygame.image.load(s1_path).convert()
s2_path = os.path.join("images","s2.jpg") 
s2 = pygame.image.load(s2_path).convert()
s3_path = os.path.join("images","s3.jpg") 
s3 = pygame.image.load(s3_path).convert()
s4_path = os.path.join("images","s4.jpg") 
s4 = pygame.image.load(s4_path).convert()
s5_path = os.path.join("images","s5.jpg") 
s5 = pygame.image.load(s5_path).convert()
sm_path = os.path.join("images","sm.jpg") 
sm = pygame.image.load(sm_path).convert()

'''
s1a_path = os.path.join("images","s1a.jpg") 
s1a = pygame.image.load(s1a_path).convert()
s2a_path = os.path.join("images","s2a.jpg") 
s2a = pygame.image.load(s2a_path).convert()
s3a_path = os.path.join("images","s3a.jpg") 
s3a = pygame.image.load(s3a_path).convert()
s4a_path = os.path.join("images","s4a.jpg") 
s4a = pygame.image.load(s4a_path).convert()
s5a_path = os.path.join("images","s5a.jpg") 
s5a = pygame.image.load(s5a_path).convert()
sma_path = os.path.join("images","sma.jpg") 
sma = pygame.image.load(sma_path).convert()
'''

#help board & winings & turns & Mancala
boardhelp_path = os.path.join("images","boardhelp.jpg") 
boardhelp = pygame.image.load(boardhelp_path).convert()
player1_path = os.path.join("images","player1.jpg") 
player1 = pygame.image.load(player1_path).convert()
player2_path = os.path.join("images","player2.jpg") 
player2 = pygame.image.load(player2_path).convert()
player1wins_path = os.path.join("images","player1wins.jpg") 
player1wins = pygame.image.load(player1wins_path).convert()
player2wins_path = os.path.join("images","player2wins.jpg") 
player2wins = pygame.image.load(player2wins_path).convert()
mancala_path = os.path.join("images","mancala.jpg") 
mancala = pygame.image.load(mancala_path).convert()
tie_path = os.path.join("images","tie.jpg") 
tie = pygame.image.load(tie_path).convert()
# score images
n0_path = os.path.join("images","n0.jpg") 
n0 = pygame.image.load(n0_path).convert()
n1_path = os.path.join("images","n1.jpg") 
n1 = pygame.image.load(n1_path).convert()
n2_path = os.path.join("images","n2.jpg") 
n2 = pygame.image.load(n2_path).convert()
n3_path = os.path.join("images","n3.jpg") 
n3 = pygame.image.load(n3_path).convert()
n4_path = os.path.join("images","n4.jpg") 
n4 = pygame.image.load(n4_path).convert()
n5_path = os.path.join("images","n5.jpg") 
n5 = pygame.image.load(n5_path).convert()
n6_path = os.path.join("images","n6.jpg") 
n6 = pygame.image.load(n6_path).convert()
n7_path = os.path.join("images","n7.jpg") 
n7 = pygame.image.load(n7_path).convert()
n8_path = os.path.join("images","n8.jpg") 
n8 = pygame.image.load(n8_path).convert()
n9_path = os.path.join("images","n9.jpg") 
n9 = pygame.image.load(n9_path).convert()
n10_path = os.path.join("images","n10.jpg") 
n10 = pygame.image.load(n10_path).convert()
n11_path = os.path.join("images","n11.jpg") 
n11 = pygame.image.load(n11_path).convert()
n12_path = os.path.join("images","n12.jpg") 
n12 = pygame.image.load(n12_path).convert()
n13_path = os.path.join("images","n13.jpg") 
n13 = pygame.image.load(n13_path).convert()
n14_path = os.path.join("images","n14.jpg") 
n14 = pygame.image.load(n14_path).convert()
n15_path = os.path.join("images","n15.jpg") 
n15 = pygame.image.load(n15_path).convert()
n16_path = os.path.join("images","n16.jpg") 
n16 = pygame.image.load(n16_path).convert()
n17_path = os.path.join("images","n17.jpg") 
n17 = pygame.image.load(n17_path).convert()
n18_path = os.path.join("images","n18.jpg") 
n18 = pygame.image.load(n18_path).convert()
n19_path = os.path.join("images","n19.jpg") 
n19 = pygame.image.load(n19_path).convert()
n20_path = os.path.join("images","n20.jpg") 
n20 = pygame.image.load(n20_path).convert()
n21_path = os.path.join("images","n21.jpg") 
n21 = pygame.image.load(n21_path).convert()
n22_path = os.path.join("images","n22.jpg") 
n22 = pygame.image.load(n22_path).convert()
n23_path = os.path.join("images","n23.jpg") 
n23 = pygame.image.load(n23_path).convert()
n24_path = os.path.join("images","n24.jpg") 
n24 = pygame.image.load(n24_path).convert()
n25_path = os.path.join("images","n25.jpg") 
n25 = pygame.image.load(n25_path).convert()
n26_path = os.path.join("images","n26.jpg") 
n26 = pygame.image.load(n26_path).convert()
n27_path = os.path.join("images","n27.jpg") 
n27 = pygame.image.load(n27_path).convert()
n28_path = os.path.join("images","n28.jpg") 
n28 = pygame.image.load(n28_path).convert()
n29_path = os.path.join("images","n29.jpg") 
n29 = pygame.image.load(n29_path).convert()
n30_path = os.path.join("images","n30.jpg") 
n30 = pygame.image.load(n30_path).convert()
n_path = os.path.join("images","n+.jpg") 
n = pygame.image.load(n_path).convert()
############################################


##########################################
## Various functions for the UI
##########################################
'''
def randomNum():
	randNum = rand.next() # Gets the random number from MyRNG
	randNum = 1 + randNum%100 # puts number in the range 1 -10
	return randNum
'''
def ReturnStoneImage(value):
	if value == 0:
		return he 
	elif value == 1:
		return h1 
	elif value == 2:
		return h2
	elif value == 3:
		return h3
	elif value == 4:
		return h4
	elif value == 5:
		return h5
	elif value > 5:
		return hm
	
def ReturnImageForScore(score):
	if score == 0:
		image = n0
	elif score == 1:
		image =n1
	elif score == 2:
		image = n2
	elif score == 3:
		image =n3
	elif score == 4:
		image = n4
	elif score == 5:
		image =n5
	elif score == 6:
		image =n6
	elif score == 7:
		image =n7
	elif score == 8:
		image =n8
	elif score == 9:
		image =n9
	elif score == 10:
		image =n10
	elif score == 11:
		image =n11
	elif score == 12:
		image = n12
	elif score == 13:
		image =n13
	elif score == 14:
		image = n14
	elif score == 15:
		image =n15
	elif score == 16:
		image =n16
	elif score == 17:
		image =n17
	elif score == 18:
		image =n18
	elif score == 19:
		image =n19
	elif score == 20:
		image =n20	
	elif score == 21:
		image =n21
	elif score == 22:
		image = n22
	elif score == 23:
		image =n23
	elif score == 24:
		image = n24
	elif score == 25:
		image =n25
	elif score == 26:
		image =n26
	elif score == 27:
		image =n27
	elif score == 28:
		image =n28
	elif score == 29:
		image =n29
	elif score == 30:
		image =n30
	elif score > 30:
		image =n
	return image

	
def ReturnScoreImages(scores):
	player1 = ReturnImageForScore(scores[0])
	player2 = ReturnImageForScore(scores[1])
	scores=(player1, player2)
	return scores
	
def ReturnStoreImage(value):
	if value == 0:
		return se 
	elif value == 1:
		return s1
	elif value == 2:
		return s2
	elif value == 3:
		return s3
	elif value == 4:
		return s4
	elif value == 5:
		return s5
	elif value > 5:
		return sm



def UpdateScreen():
			#----------------------------------------------------
			# Hole Counts
			
			count12 = ReturnImageForScore(game.ReturnHoleValue(12))
			count11 = ReturnImageForScore(game.ReturnHoleValue(11))
			count10 = ReturnImageForScore(game.ReturnHoleValue(10))
			count9 = ReturnImageForScore(game.ReturnHoleValue(9))
			count8 = ReturnImageForScore(game.ReturnHoleValue(8))
			count7 = ReturnImageForScore(game.ReturnHoleValue(7))
			count6 = ReturnImageForScore(game.ReturnHoleValue(6))
			count5 = ReturnImageForScore(game.ReturnHoleValue(5))
			count4 = ReturnImageForScore(game.ReturnHoleValue(4))
			count3 = ReturnImageForScore(game.ReturnHoleValue(3))
			count2 = ReturnImageForScore(game.ReturnHoleValue(2))
			count1 = ReturnImageForScore(game.ReturnHoleValue(1))
			
			#top row 12-7
			screen.blit(count12, (180,275)) # 237x167
			screen.blit(count11, (237,275)) # 294x167
			screen.blit(count10, (294,275)) # 351x167
			screen.blit(count9, (398,275)) # 455x167
			screen.blit(count8, (455,275)) # 512x167
			screen.blit(count7, (512,275)) # 569x167
			# bottom row 1-6
			screen.blit(count1, (180,342)) #237x234
			screen.blit(count2, (237,342)) #294x234
			screen.blit(count3, (294,342)) #351x234
			screen.blit(count4, (398,342)) #455x234
			screen.blit(count5, (455,342)) #521x234
			screen.blit(count6, (512,342)) #569x234
			
			#----------------------------------------------------
			# Help board, player scores, Mancala images
			if helpflag:
				screen.blit(boardhelp, (100,265))
				
			screen.blit(mancala, (80,40))
			screen.blit(currentPlayerImage, (355,40))
			
			scores = game.ReturnPlayerScores()
			scores = ReturnScoreImages(scores)
			
			#images scores
			screen.blit(scores[0], (664,130)) 
			screen.blit(scores[1], (28,130)) 
			
			#----------------------------------------------------
			# Stones on the board
			hole12 = ReturnStoneImage(game.ReturnHoleValue(12))
			hole11 = ReturnStoneImage(game.ReturnHoleValue(11))
			hole10 = ReturnStoneImage(game.ReturnHoleValue(10))
			hole9 = ReturnStoneImage(game.ReturnHoleValue(9))
			hole8 = ReturnStoneImage(game.ReturnHoleValue(8))
			hole7 = ReturnStoneImage(game.ReturnHoleValue(7))
			hole6 = ReturnStoneImage(game.ReturnHoleValue(6))
			hole5 = ReturnStoneImage(game.ReturnHoleValue(5))
			hole4 = ReturnStoneImage(game.ReturnHoleValue(4))
			hole3 = ReturnStoneImage(game.ReturnHoleValue(3))
			hole2 = ReturnStoneImage(game.ReturnHoleValue(2))
			hole1 = ReturnStoneImage(game.ReturnHoleValue(1))
			
			#top row 12-7
			screen.blit(hole12, (180,110)) # 237x167
			screen.blit(hole11, (237,110)) # 294x167
			screen.blit(hole10, (294,110)) # 351x167
			screen.blit(hole9, (398,110)) # 455x167
			screen.blit(hole8, (455,110)) # 512x167
			screen.blit(hole7, (512,110)) # 569x167
			# bottom row 1-6
			screen.blit(hole1, (180,177)) #237x234
			screen.blit(hole2, (237,177)) #294x234
			screen.blit(hole3, (294,177)) #351x234
			screen.blit(hole4, (398,177)) #455x234
			screen.blit(hole5, (455,177)) #521x234
			screen.blit(hole6, (512,177)) #569x234
			
			#store
			stores = game.ReturnStoresValue()
			store1 = ReturnStoreImage(stores[0])
			store2 = ReturnStoreImage(stores[1])
		
			screen.blit(store2, (118,110)) #173x232
			screen.blit(store1, (574,110)) #629x232
			#----------------------------------------------------
			
			#updates the screen with the new data
			pygame.display.flip()
			
#####################################################################			
			

##################################################
## the game loop for mancala
#################################################
currentPlayerImage = player1 # player 1 goes first
while running:
			
	for event in pygame.event.get():
		if game.ReturnPlayerTurn() == "Player 1":
			currentPlayerImage = player1
		else:
			currentPlayerImage = player2
		
		if event.type == pygame.QUIT:
				running = 0
		
		if game.ContinueGame():
			
			if event.type == pygame.KEYDOWN:
				if event.key == K_1:
					value = 1
					game.PlayerSelectsHole(value)
				if  event.key == K_2:	
					value = 2
					game.PlayerSelectsHole(value)
				if  event.key == K_3:	
					value = 3
					game.PlayerSelectsHole(value)
				if  event.key == K_4:
					value = 4
					game.PlayerSelectsHole(value)
				if  event.key == K_5:
					value = 5
					game.PlayerSelectsHole(value)
				if  event.key == K_6:	
					value = 6
					game.PlayerSelectsHole(value)

				if  event.key ==  K_7:
					value = 12
					game.PlayerSelectsHole(value)
				if  event.key == K_8:	
					value = 11
					game.PlayerSelectsHole(value)
				if  event.key == K_9:
					value = 10
					game.PlayerSelectsHole(value)
				if  event.key ==  K_0:
					value = 9
					game.PlayerSelectsHole(value)
				if  event.key ==  K_MINUS:
					value = 8
					game.PlayerSelectsHole(value)
				if  event.key ==  K_EQUALS:	
					value = 7
					game.PlayerSelectsHole(value)
				if event.key == K_h:
					if helpflag == True:
						helpflag =False
					else:
						helpflag = True
					
				
			screen.fill(bgcolor)
			screen.blit(board, (100,100))
				
			UpdateScreen()
		
		else: 
			game.EndofGameLogic()
			UpdateScreen()
			winner = game.DetermineWinner()
			if winner == "Player 1":
				screen.blit(player1wins, (355,40))
			elif winner == "Player 2":
				screen.blit(player2wins, (355,40))
			elif winner == "tie":
				screen.blit(tie, (355,40))
				
			pygame.display.flip()
	





	
	
	


'''
#############################
# Extra stuff
############################	
#clock.tick(200)
			
			elif event.type == pygame.MOUSEMOTION:
				print"mouse at(%d, %d)" % event.pos #event.pos returns a pair of values representing the x-position and y-position of the mouse pointer
				x, y = event.pos
			elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
				print "You released the left mouse button at (%d, %d)" % event.pos
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:	
				print "You pressed the left mouse button at (%d, %d)" % event.pos
				if x>180 & x <237 & y > 110 & y <167:#hole12
'''	

