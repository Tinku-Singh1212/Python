# m1=3
# c1=3
# m2=0
# c2=0
# while m1!=0 or c1!=0: 
#   r=int(input("enter the rule "))
#   if r==1:
#     m1-=1    #one missionary go
#     m2+=1   #press   1
#   if r==2:
#     m1-=2    #two missionary go
#     m2+=2    #press 2
#   if r==3:
#     c1-=1    #one cannibal go
#     c2+=1     #press 3
#   if r==4:
#     c1-=2    #two cannibal go
#     c2+=2      #press 4
#   if r==5:
#     c1-=1    # one missionary and one cannibal go
#     c2+=1       #press 5
#     m1-=1
#     m2+=1
#   if r==6:
#     m2-=1      #one missionary come
#     m1+=1       #press 6
#   if r==7:
#     m2-=2      #two missionary come
#     m1+=2      #press 7
#   if r==8:
#     c2-=1      #one cannibal come
#     c1+=1        #press 8
#   if r==9:
#     c2-=2    #two cannibal come
#     c1+=2       #press 9
#   if r==10:
#     m2-=1      # one missionary and one cannibal come
#     m1+=1       #press 10
#     c2-=1
#     c1+=1 
#   if m1<c1 or m2<c2:  
#     print("game over")
#     m1==0
#     c1==0  
#   if r<=5:
#     print("Boat go to Second end")
#   else:
#     print("Boat come to first end")  
#   print("First End of river ","Missionaries= ",m1,"Cannibals= ",c1)
#   print("Second end of river ","Missionaries= ",m2,"Cannibals= ",c2)  
m1 = 3  # missionaries on the first side
c1 = 3  # cannibals on the first side
m2 = 0  # missionaries on the second side
c2 = 0  # cannibals on the second side

while (m1 > 0 or c1 > 0):  # Game ends only when all have crossed
    print("First End of river - Missionaries:", m1, "Cannibals:", c1)
    print("Second End of river - Missionaries:", m2, "Cannibals:", c2)

    r = int(input("Enter the rule (1-10): "))

    if r == 1:
        if m1 >= 1:
            m1 -= 1  # One missionary goes
            m2 += 1
        else:
            print("Invalid move! Not enough missionaries.")
    elif r == 2:
        if m1 >= 2:
            m1 -= 2  # Two missionaries go
            m2 += 2
        else:
            print("Invalid move! Not enough missionaries.")
    elif r == 3:
        if c1 >= 1:
            c1 -= 1  # One cannibal goes
            c2 += 1
        else:
            print("Invalid move! Not enough cannibals.")
    elif r == 4:
        if c1 >= 2:
            c1 -= 2  # Two cannibals go
            c2 += 2
        else:
            print("Invalid move! Not enough cannibals.")
    elif r == 5:
        if m1 >= 1 and c1 >= 1:
            m1 -= 1  # One missionary and one cannibal go
            c1 -= 1
            m2 += 1
            c2 += 1
        else:
            print("Invalid move! Not enough missionaries or cannibals.")
    elif r == 6:
        if m2 >= 1:
            m2 -= 1  # One missionary comes back
            m1 += 1
        else:
            print("Invalid move! Not enough missionaries on the second side.")
    elif r == 7:
        if m2 >= 2:
            m2 -= 2  # Two missionaries come back
            m1 += 2
        else:
            print("Invalid move! Not enough missionaries on the second side.")
    elif r == 8:
        if c2 >= 1:
            c2 -= 1  # One cannibal comes back
            c1 += 1
        else:
            print("Invalid move! Not enough cannibals on the second side.")
    elif r == 9:
        if c2 >= 2:
            c2 -= 2  # Two cannibals come back
            c1 += 2
        else:
            print("Invalid move! Not enough cannibals on the second side.")
    elif r == 10:
        if m2 >= 1 and c2 >= 1:
            m2 -= 1  # One missionary and one cannibal come back
            c2 -= 1
            m1 += 1
            c1 += 1
        else:
            print("Invalid move! Not enough missionaries or cannibals on the second side.")
    else:
        print("Invalid rule! Enter a number between 1 and 10.")

    # Check game over condition
    if (m1 > 0 and c1 > m1) or (m2 > 0 and c2 > m2):
        print("Game over! Cannibals outnumbered the missionaries!")
        break

    if m1 == 0 and c1 == 0:
        print("Congratulations! All missionaries and cannibals have crossed safely.")
        break

    if r <= 5:
        print("Boat goes to the second end.")
    else:
        print("Boat comes to the first end.")
 