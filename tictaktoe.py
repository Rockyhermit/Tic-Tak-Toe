import random
import os




def board():
    for i in range(1, 10):
        if i <= 6 and i % 3 == 0:
            print("___")
        elif i <= 6:
            print("___|", end="")
        elif i % 3 == 0:
            print("   ")
        else:
            print("   |", end="")

def rboard():
    for i in range(1, 10):
        if i <= 6 and i % 3 == 0:
            print(f" {i} ")
        elif i <= 6:
            print(f" {i} |", end="")
        elif i % 3 == 0:
            print(f" {i} ")
        else:
            print(f" {i} |", end="")

def player(q):
    while True:
        try:
            if q == 1:
                name = input("Enter your name: ")
                k = int(input("Choose any one:\n1.X\n2.O\n"))
                if k!= 1 and k!=2:
                    print("Invalid Option")
                else:
                    return k,name
            else:
                name = input("Enter your name: ")
                return name
        except:
            print("Invalid Option")


def computer(q):
    if q == 1:
         k = random.randint(1,2)
         name = "Computer1"
         return k,name
    else:
        name = "Computer"
        return name


def rules():
    os.system('cls')
    input("******************** RULES ********************\n\n(Press Enter to Continue)")
    board()
    input("1. This is a default board of TIC TAC TOE. The player can choose any one symbol between O (Zero) and X (Cross).")
    input("2. The aim is to create 3 consequtive positions of same symbol, it may be a horizontal, vertical or diagonal line.")
    input("3. Any player/computer if completes the above criteria wins.")
    input("4. The player has three modes to play this game:\n   (i) Player V/S Computer\n   (ii) Player V/S Player\n   (iii) Computer V/S Computer")
    rboard()
    input("5. These are the position available to the player on the board. The player can interact with the game via selecting the position [acc to their respective numbers].\n\n******************** END ********************")
    os.system('cls')


def game():
    r = 0
    l=0
    while l==0:
        input("******************** WELCOME TO PLAY TIC TAC TOE ********************\n\n(Press Enter to Continue)")
        kkk = int(input("Choose the Gamestyle:\n1. Player V/S Computer\n2. Player V/S Player\n3. Computer V/S Computer\n4. Learn Rules\n5. Quit\n"))
        if kkk == 1:
            l1 = player(1)
            k = l1[0]
            name1 = l1[1]
            name2 = computer(2)
            l+=1
        elif kkk ==2:
            l1 = player(1)
            k = l1[0]
            name1 = l1[1]
            name2 = player(2)
            l+=1
        elif kkk ==3:
            l1 = computer(1)
            k = l1[0]
            name1 = l1[1]
            name2 = computer(2)
            l+=1
        elif kkk==4:
            rules()
        elif kkk == 5:
            print("Bye Bye!!!")
            exit()
    if k == 1:
        sym = "X"
        Csym = "O"
    elif k == 2:
        sym = "O"
        Csym = "X"
    ls = []
    for i in range(1, 10):
        if i <= 6 and i % 3 == 0:
            ls.append("___")
        elif i <= 6:
            ls.append("___|",)
        elif i % 3 == 0:
            ls.append("   ")
        else:
            ls.append("   |",)
    print(ls[0], ls[1], ls[2])
    print(ls[3], ls[4], ls[5])
    print(ls[6], ls[7], ls[8])
    print("\n")
    ul = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    p = []
    c = []
    while r <= 9:
        r += 1
        if len(ul) == 0:
            print("It's a Tie!!!")
            break
        if sym == "X" and r % 2 == 0:
            o = 0
            while o == 0:
                try:
                    if kkk == 1 or kkk ==2:
                         a = int(input("Enter the position: "))
                    else:
                        b = random.randint(0, len(ul)-1)
                        a = ul[b]  
                    ul.remove(a)
                    p.append(a)
                    o+=1
                except:
                    print("Invalid Option")
            for i in range(1, 10):
                if i <= 6 and i % 3 == 0:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {sym} ")
                    else:
                        pass
                elif i <= 6:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {sym} |")
                    else:
                        pass
                elif i % 3 == 0:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {sym} ")
                    else:
                        pass
                else:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {sym} |")
                    else:
                        pass
        elif sym == "O" and r % 2 != 0:
            o = 0
            while o==0:
                try:
                    if kkk == 1 or kkk ==2:
                        a = int(input("Enter the position: "))
                    else:
                        b = random.randint(0, len(ul)-1)
                        a = ul[b]
                    ul.remove(a)
                    p.append(a)
                    o+=1
                except:
                    print("Invalid Option")
            for i in range(1, 10):
                if i <= 6 and i % 3 == 0:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {sym} ")
                    else:
                        pass
                elif i <= 6:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {sym} |")
                    else:
                        pass
                elif i % 3 == 0:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {sym} ")
                    else:
                        pass
                else:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {sym} |")
                    else:
                        pass
        else:
            o = 0
            while o==0:
                try:
                    if kkk ==2:
                        a = int(input("Enter the position: "))
                    else:
                        b = random.randint(0, len(ul)-1)
                        a = ul[b]
                    ul.remove(a)
                    c.append(a)
                    o+=1
                except:
                    print("Invalid Option")
            for i in range(1, 10):
                if i <= 6 and i % 3 == 0:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {Csym} ")
                    else:
                        pass
                elif i <= 6:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {Csym} |")
                    else:
                        pass
                elif i % 3 == 0:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {Csym} ")
                    else:
                        pass
                else:
                    if i == a:
                        ls.pop(i-1)
                        ls.insert(i-1, f" {Csym} |")
                    else:
                        pass
        print(ls[0], ls[1], ls[2])
        print(ls[3], ls[4], ls[5])
        print(ls[6], ls[7], ls[8])
        print("\n")
        # print(p,"\n",c)
        if 1 in p and 2 in p and 3 in p:
            print(f"{name1} Wins!!!")
            break
        elif 4 in p and 5 in p and 6 in p:
            print(f"{name1} Wins!!!")
            break
        elif 7 in p and 8 in p and 9 in p:
            print(f"{name1} Wins!!!")
            break
        elif 1 in p and 4 in p and 7 in p:
            print(f"{name1} Wins!!!")
            break
        elif 2 in p and 5 in p and 8 in p:
            print(f"{name1} Wins!!!")
            break
        elif 3 in p and 6 in p and 9 in p:
            print(f"{name1} Wins!!!")
            break
        elif 3 in p and 5 in p and 7 in p:
            print(f"{name1} Wins!!!")
            break
        elif 1 in p and 5 in p and 9 in p:
            print(f"{name1} Wins!!!")
            break
        

        elif 1 in c and 2 in c and 3 in c:
            print(f"{name2} Wins!!!")
            break
        elif 4 in c and 5 in c and 6 in c:
            print(f"{name2} Wins!!!")
            break
        elif 7 in c and 8 in c and 9 in c:
            print(f"{name2} Wins!!!")
            break
        elif 1 in c and 4 in c and 7 in c:
            print(f"{name2} Wins!!!")
            break
        elif 2 in c and 5 in c and 8 in c:
            print(f"{name2} Wins!!!")
            break
        elif 3 in c and 6 in c and 9 in c:
            print(f"{name2} Wins!!!")
            break
        elif 3 in c and 5 in c and 7 in c:
            print(f"{name2} Wins!!!")
            break
        elif 1 in c and 5 in c and 9 in c:
            print(f"{name2} Wins!!!")
            break
            

       


# ___|___|___
# ___|___|___ #This is the desired output in the terminal
#    |   |
while True:
    try:
        l = 0
        os.system('cls')
        game()
        while l==0:
            a = input("Do You Want to Play again?\n(y/n)")
            if a == "y":
                 l+=1
            elif a == "n":
                print("Fuck Off!!!")
                exit()
            else:
                print("Invalid Option")

    except ValueError as e:
        print("Invalid Option")

