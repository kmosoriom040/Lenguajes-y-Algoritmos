
print("Hello In SOS Game")
playerX = input("Enter Name of First Player : \t")
playerY = input("Enter Name of Second Player : \t")
playerX_score = playerY_score = loop_no = counter  = previous_playerX = previous_playerY = 0
toggle = 1
running = True
position=0
grid=value=""
game = []
available=[]
num = [3,7,11,15]
for i in range(0,16):
 game.append(i+1)
 available.append(i+1)


def display() :
    global grid
    grid=""
    for i in range (0,16) :
      if  i in num :
        if ((game[i] == "S" or game[i] == "O") and i >=9):
         grid+="  "+str(game[i])+"  "+" |"+"\n"
        elif ((game[i] == "S" or game[i] == "O") and i <9):
         grid+="  "+str(game[i])+"  "+" |"+"\n"
        else:
           if i >= 9 :
            grid+="  "+str(game[i])+"  "+"|"+"\n"
           else:
            grid+="  "+str(game[i])+"  "+" |"+"\n"

      else :
        if ((game[i] == "S" or game[i] == "O") and i >=9):
         grid+="   "+str(game[i])+"   "+"|"
        elif ((game[i] == "S" or game[i] == "O") and i <9):
         grid+="   "+str(game[i])+"   "+"|"
        else:
           if i >= 9 :
            grid+="  "+str(game[i])+"  "+" |"
           else:
            grid+="   "+str(game[i])+"  "+" |"

    print(grid)
 

      
display()





def inputa() :
    global value
    value = str(input("Enter Value ( S / O) : \n"))
    print("\n")
    global position
    global available
    position = int(input("Enter Numbers between 1 and 16  : ")) 
    if (available[position-1] == 0) :
        print("Warning ! this assigned before")
        inputa()

    





def switch_player() :
    global toggle
    global playerX_score
    global playerY_score
    global previous_playerX
    global previous_playerY
    global loop_no
    if (loop_no == 0) :
     return ">>>>>> First player turn >>>>>>" 
    

    elif (loop_no !=0):
     if ( toggle == 1 ):
      if ( playerX_score > previous_playerX):
       return ">>>>>> First player turn >>>>>>" 
        
      else :
        toggle = 2
        return ">>>>>> Second player turn >>>>>>" 
     elif (toggle == 2) :
      if ( playerY_score > previous_playerY):
       return ">>>>>> Second player turn >>>>>>" 
      else :
       toggle = 1
       return ">>>>>> First player turn >>>>>>" 

        
def write(): 
    global value
    global position
    game[position-1] =value
    display()
    global available
    available[position-1]=0



def judge() :
 global position
 global value
 global playerX_score
 global playerY_score
 global previous_playerX
 global previous_playerY
 global game

 Z = position-1;
 previous_playerY = playerY_score
 previous_playerX = playerX_score
 if (value == "O") :
  look ="S"
  if ( position != 16 and game[Z-1] == game[Z+1]) :
   if(game[Z-1] == look and position%4 !=0):
    if(toggle == 1):
      playerX_score+=1
    else :
      playerY_score+=1

     

  elif(position <= (len(game)-4) and game[Z+4] == game[Z-4]  ):
   if(game[Z-4] == look):
    if(toggle == 1):
     playerX_score+=1
    else:
     playerY_score+=1

  elif(position < (len(game)-4) and position > 5 and game[Z+5] == game[Z-5]) :
    if(game[Z-5]== look and position%4 != 0 ):
      if((position-5)%4 != 0) :
        if(toggle == 1):
          playerX_score+=1
        else :
          playerY_score+=1

  elif(position <12 and game[Z+3] == game[Z-3]):
    if(game[Z-3] == look and position%4 != 0):
      if((position+3)%4 != 0):
        if(toggle == 1):
          playerX_score+=1
        else :
          playerY_score+=1



 elif (value == "S"):
    if ((position) <= (len(game)-2) and game[Z+1] == "O" and game[Z+2] ==  "S" ):
     if((position+1) %4 !=0 and position%4 !=0):
      if(toggle == 1):
       playerX_score+=1
      else:
       playerY_score+=1
    
    

    elif( position >= 3 and game[Z-1] == "O" and game[Z-2] ==  "S"):
     if((position-1) %4 !=0 and (position-2)%4 !=0 ):
      if(toggle == 1):
       playerX_score+=1
      else:
       playerY_score+=1
    
  
    elif(position <= (len(game)-8) and game[Z+4] ==  "O" and game[Z+8] == "S" ):
     if(toggle == 1):
      playerX_score+=1
     else:
      playerY_score+=1
    

    elif((position > (len(game)-8)) and game[Z-4] ==  "O" and game[Z-8] == "S" ):
     if(toggle == 1):
      playerX_score+=1
     else:
      playerY_score+=1
    

    elif(position <= 6 and position and game[Z+5] ==  "O" and game[Z+10] ==  "S" and (position+5)%4 !=0 and position%4 != 0):
     if(toggle == 1):
      playerX_score+=1
     else:
      playerY_score+=1
    
    elif(position > (len(game)-8) and game[Z-5] ==  "O" and game[Z-10] ==  "S" and (position-5)%4 !=0 and (position-10)%4 !=0 ):
     if(toggle == 1):
      playerX_score+=1
     else:
      playerY_score+=1
    
    elif(position <=8 and game[Z+3] ==  "O" and game[Z+6] ==  "S" and (position+3)%4 !=0 and (position+6) %4!=0):
     if(toggle == 1):
      playerX_score+=1
     else:
      playerY_score+=1
    
    elif(position>8 and game[Z-3] ==  "O" and game[Z-6] ==  "S"  and (position-3)%4 !=0):

     if(toggle == 1):
      playerX_score+=1
     else:
      playerY_score+=1
    else:
     playerX_score=playerX_score
     playerY_score=playerY_score
 print(" Score : "+str(playerX_score)+"\n")
 print(" Score : "+str(playerY_score)+"\n")



def check_win():
  global playerX_score
  global playerY_score
  if( playerX_score > playerY_score):
   return "Winner is " +playerX
  elif(playerX_score < playerY_score):
   return  "Winner is " +playerY
  else:

   return "Game ended Draw between " + playerX +" and " + playerY
    
def restart() :
  global game
  global available
  global grid
  game=[]
  available=[]
  grid=""
  for i in range(0,16):
   game.append(i+1)
   available.append(i+1)
  for i in range (0,16) :
   if  i in num :
    if i >= 9 :
     grid+="  "+str(game[i])+"  "+"|"+"\n"
    else:
     grid+="  "+str(game[i])+"  "+" |"+"\n"

   else :
    if i >= 9 :
     grid+="  "+str(game[i])+"  "+" |"
    else:
     grid+="   "+str(game[i])+"  "+" |"

  print(grid)
   



while(True) :
    
    filled = 1
    for z in range(0,16):
     if (available[z] != 0):
      filled = 0
    if ( filled == 1):
     print(check_win())
     exit = input("Do You Want to Close : ( Y / N )")
     if (exit == 'Y'):
      break
     elif (exit == 'N') :
      toggle = 1
      playerX_score = playerY_score = loop_no = counter  = previous_playerX = previous_playerY = 0
      print("\n <<<< Game Restarted  ! <<<< \n")
      restart()




     
    
    print("\n")
    print(switch_player())
    loop_no+=1
    inputa()
    write()
    judge()
