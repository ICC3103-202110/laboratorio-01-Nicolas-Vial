# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:54:01 2021

@author: nicol
"""
#import libraries
import random

#function for printing the dashboard on diferent cases
def dashboard(array, participant, x1,y1,x2,y2):
    
    print("Player N°"+str(participant))
    #printing header
    if len(array)>1:
        print("   0  1  2  3  4  5  6  7  8  9")
        print("   ____________________________")
    else:
        counter=0
        print("   ", end='')
        while counter <= len(array[0])-1:
            print(counter, end=' ')
            counter+=1
        print("")
        print("   ", end='')
        print("__"*len(array[0]))
    
    counter1=0
    while counter1<=len(array)-1:
        print(str(counter1)+" |", end='')
        counter2=0
        while counter2 <= len(array[counter1])-1:
            if counter1==y1 and counter2==x1:
                if array[counter1][counter2]<=9:
                    print(array[counter1][counter2], end=' ')
                else:
                    print(array[counter1][counter2], end=' ')
            elif counter1==y2 and counter2==x2:
                if array[counter1][counter2]<=9:
                    print(array[counter1][counter2], end=' ')
                else:
                    print(array[counter1][counter2], end=' ')
            elif array[counter1][counter2]=="":
                    print(array[counter1][counter2], end='  ')   
            elif array[counter1][counter2]=="":
                    print(array[counter1][counter2], end='  ')
            else:
                print("* ", end='')
            counter2+=1
        print("")
        counter1+=1

#function for checking ig two cards are equal
def check(array,x1,y1,x2,y2):
    return array[y1][x1]==array[y2][x2]
    

#Ask main parameters
print("\nWELCOME TO MEMORIZE!! \n")
N_players=int(input("Set the number of players: "))
N_cards=int(input("Set the number of cards: "))
points=[]
counter=0
while counter<N_players:
    points.append(0)
    counter+=1

#Build primary array of numbers
cards_array=[]
counter=1
while counter<=N_cards:
    cards_array.append(counter)
    cards_array.append(counter)
    counter+=1
cards_array=random.sample(cards_array, len(cards_array))


#Build list of lists for coordenateswith cards
vertical=[]
horizontal=[]
value=0
while value <len(cards_array):
    if len(horizontal)<=9:
        horizontal.append(cards_array[value])
        value+=1
        if len(horizontal)==10:
            vertical.append(horizontal)
        
    else:
        vertical.append(horizontal)
        horizontal=[cards_array[value]]
        value+=1
if len(horizontal)<10:
    vertical.append(horizontal)


#gaming
solved_cards=[]
player=1
play=1
while len(solved_cards)-N_cards!=0:
    print("\n####### MEMORIZE #######\n")
    print("Play N°"+str(play)+"\n")
    dashboard(vertical, player,-1,-1,-1,-1)
    hor1=int(input("Type the horizontal coordenate of the first card you want to see :"))
    ver1=int(input("Type the vertical coordenate of the first card you want to see :"))
    dashboard(vertical, player,hor1,ver1,-1,-1)
    hor2=int(input("Type the horizontal coordenate of the second card you want to see :"))
    ver2=int(input("Type the vertical coordenate of the second card you want to see :"))
    dashboard(vertical, player,hor1,ver1,hor2,ver2)
    
    
    if check(vertical, hor1,ver1,hor2,ver2) == False:
    	if player== N_players:
    		player=1
    	else:
    		player+=1
    else:
        
    	solved_cards.append(vertical[ver1][hor1])
    	vertical[ver1][hor1]=""
    	vertical[ver2][hor2]=""
  
    if check(vertical, hor1,ver1,hor2,ver2) == True:
        points[player-1]=points[player-1]+1   
       
    play+=1
dashboard(vertical,player,-1,-1,-1,-1)    
    
print("\n\nGAME OVER\n\nThe scores are the following:\n\n")
value=0
while value <len(points):
    print("Player N° "+str(value+1)+": "+str(points[value])+"\n")
    value+=1
print("\n\nCONGRATULATIONS PLAYER N°"+str(points.index(max(points))+1))
































