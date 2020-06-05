

import random ##generate the random number##



Player1Tiebreaker = 0
Player2Tiebreaker = 0
Winner_Points = 0
player1Roll=0
player2Roll=0
score=0
scorep2=0
winner_user=0

dicegame= input("welcome to my dice game.\npress enter to continue")

#### authintication start ####
logged_in1 = True
logged_in2 = True
while logged_in1 == True: ### user1 login##
    username = input('What is your username? ') 
    password = input('What is your password? ')
    if username == 'user1' or username == 'user2': 
        if password == 'password':
            print('Welcome, ',username,' you have been successfully logged in.')
            logged_in1 = False
            user1 = username
        else:
            print('Incorrect password, try again')  
    else:
        print('Incorrect username, try again')

while logged_in2 == True: ### user2 login###
    username = input('What is your username? ')
    password = input('What is your password? ')
    if username == 'user1' or username == 'user2':
        if password == 'password':
            
            print('Welcome, ',username,' you have been successfully logged in.')
            logged_in2 = False
            user2 = username
        else:
            print('Incorrect password, try again')  
    else:
        print('Incorrect username, try again')
        
#### authintication ends###


##dice roll##

###player1 dice game####
for i in range(1,6): ### 5 round game###
  print("\n")  
  player1Roll = input(user1 + " would you like to roll your dice? Y/N: ") ## asking the 1st player ###
  print("\n")
        
  if player1Roll ==("Y") or  player1Roll ==("y"):

         print ("You rolled a:")
         dice1 = random.randint(1,6) ### dice1 random number generates ###
         print(dice1)

   
         print ("You rolled a:")
         dice2 = random.randint(1,6) ### dice2 random nnumber generates ###
         print(dice2)


  diceTotalp1 = dice1 + dice2 ### total dice for player1 ###

  score = diceTotalp1 +score


  if  diceTotalp1 % 2==0: ### if the number is divided by 2 and reminder is 0 then it's even number ###
         print("You rolled an even number + 10 points!")
         score= score + 10 ### score will added to the player1 score variable ####
         print(score)

  else:
      print("you got odd number-5") ### if the dicetotalp1 is not divided by 2 then it's a odd number ###
      score= score-5 ### score will be substract to the player1 variable ###
      print(score)


  if dice1 == dice2: ### if dice1 and dice2 and the same number then it will run the code below ####
      print("\n")
      print("double score\nyou will have a bonus roll")
      print("\n")

      print("you have rolled a: ")
      dice1_2 =random.randint(1,6) ### dice1_2 will generates random number ####
      print(dice1_2) ### this will print the number that has been generated ####


      print("you have rolled a: ")
      dice2_2= random.randint(1,6)### dice2_2 will generates random number ####
      print(dice2_2) ### this will print the number that has been generated ####

      extradice = dice1_2 + dice2_2 ### dice1_2 and dice2_2 will add together to find out wheather the total extradice is even or odd number ###

      score= extradice + score ### the extradice number will add to the players score ###

      if extradice %2 ==0: ### if extradice is divided by 2 and the reminder is 0 then its an even number ####
          print("you have rolled an even number +10 points") #### it will output to show the user that they got a even number ###
          score= score + 10 ### 10 points will add to the players score ####
          print(score) ### it will output the players score ####

      else:
          print("you have odd number") ### if the extradice is not divided by 2 and the reminder is not 0 then its a odd number ####
          score= score - 5 ### 5 points will taken from the score ###
          print(score) ### this will output the players score ###
          

 #### player1 dice games ends #####

      


##player 2 dice game starts###
  print("\n")    
  player2Roll = input(user2 + " would you like to roll your dice? Y/N: ") ### asking player 2 if they wanna play the games ###
  print("\n")
  if player2Roll ==("Y") or player2Roll ==("y"):
      
          print ("You rolled a:")
          dice1 =random.randint(1,6) ### dice1 random number generetes ###
          print(dice1)


    
          print ("You rolled a:")
          dice2 =random.randint(1,6) ### dice2 random number generetes ###
          print(dice2)

  dicetotalp2= dice1 + dice2 ### total number of dice1 and dice2 ####


  scorep2 = dicetotalp2 + scorep2

  if dicetotalp2 % 2==0:  ### if the total dicetotalp2 is divided by 2 and the reminder is 0 then it's a even number ###
          print("You rolled an even number + 10 points!")
          scorep2= scorep2 + 10 ### score will added on the scorep2 variable ###
          print(scorep2)
          
  else: 
      print("you got the odd number -5") ### if the dicetotalp2 score is not divided by 2 then it's a odd number ###
      scorep2= scorep2 -5 ### score will substract from the scorep2 variable ###
      print(scorep2)


  if dice1 == dice2: ### if dice1 and dice2 are the same number it will run the code below for extra roll ###
      print("\n")
      print("double score\nyou will have a bonus roll")
      print("\n")

      print("you have rolled a: ") 
      dice1_2=random.randint(1,6) ### dice1_2 generates random integer number ####
      print(dice1_2) ### this will output the dice1_2 ###


      print("you have rolled a: ")
      dice2_2= random.randint(1,6) ### dice2_2 generates random integer number ###
      print(dice2_2) ### this will output the dice2_2 ####

      extradicep2 = dice1_2 + dice2_2 ### dice1_2 and dice2_2 will add together to make the number even or odd ###

      scorep2= extradicep2 + scorep2 ### the extradicep2 score will add to the players main score ####

      if extradicep2 %2 ==0: ### if the extrascorep2 is divided by 2 and reminder is 0 then its a even number ####
          print("you have rolled an even number +10 points") #### it will output to show the user that they got a even number ###
          score= scorep2 + 10   ### 10 points will add to the players score ###
          print(scorep2)   ### this will then print the total score that the player has ###


      else:
          print("you have odd number") #d## if its not divided by 2 and the reminder is not 0 then its odd number ###
          scorep2= scorep2 - 5 ### 5 points will taken from the score ###
          print(scorep2) #### this will print the score that the player has ###
              
#### player2 dice game ends ####        

         
###dice roll end###

###if player1 point and player2 point are same ####
      
if score == scorep2: ### if the user1 score and user2 score are the same it will generate another number ####
    while Player1Tiebreaker == Player2Tiebreaker: ### another variable for tie braker ####


        Player1Tiebreaker = random.randint(1,6) ### player1 tiebraker generates a number ####
        Player2Tiebreaker = random.randint(1,6) ### player2 tiebraker generetes a number ####

    if Player1Tiebreaker > Player2Tiebreaker: ### if player1tiebraker is greater than player2tiebraker then 10 points will add to score variable ###
        score = 0 + 10
    elif Player2Tiebreaker > Player1Tiebreaker: #### if player2tiebraker is grater than player2tiebraker then 10 points will added to the scorep2 variable ###
        scorep2 = 0 + 10


if score>scorep2: ### if player1 score is greater than player2 score then the winner will be player1 ####
    Winner_Points = score
    winner_User = user1
    winner = (Winner_Points, user1)
    
elif scorep2>score: #### if player2 score is greater than player1 score than the winner will be player2 ###
    Winner_Points = scorep2
    winner = (Winner_Points, user2)
    winner_User = user2

print('Well done ' ,winner_User, ' you won with ',Winner_Points,' Points') ### output the winner ###


winner = ('congrats ',winner_User, ' you got ' ,Winner_Points, ' points') ### vabiable for winner ###
f = open('Winner.txt', 'a') ### save the file externally in txt. format ###
f.write(str(winner)) ## write the file ###
f.write('\n') ### for 2nd paragraph ###
f.close() ## file close ###



f = open('winner.txt', 'r') ###  leaderboard saves the file externally in txt. format ###
leaderboard = [line.replace('\n','') for line in f.readlines()] ### line separation for the leaderboard ####
f.close() ### file close ###

for idx, item in enumerate(leaderboard): ### loop over leaderboard and have an automatic counter ####
    if item.split(', ')[1] == winner[1] and int(item.split(', ')[0]) < int(winner[0]): 
            leaderboard[idx] = '{}, {}'.format(winner[0], winner[1])
    else:
        pass

leaderboard.sort(reverse=True) #### layer sort out ###

with open('leaderboard.txt', 'w') as f: ### save the leaderboard to txt. format ###
    for item in leaderboard:
        f.write("%s\n" % item) ### write the leaderboard ###
        






