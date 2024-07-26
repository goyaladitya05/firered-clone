import random
import time
import mysql.connector as s

mycon = s.connect(host="localhost", user = "root", password = "aditya", database = "poke")
if mycon.is_connected():
    print("Successfully Connected!")
cursor = mycon.cursor()


creditOG = 5000
user_poke = ["Pikachu", "Charizard"]
list = ["Pikachu", "Charizard", "Arcanine", "Blastoise", "Bulbasaur"]
credit_list = [10,50,100,150,200,250,300,350,400,450,500]

def pokemon():
    global list 
    global credit_list 
    global user_poke
    global creditOG

    def call():
        attacker = random.choice(list)
        return attacker

    def fight():
        global creditOG
        
        user_poke_hp = 100
        opp_poke_hp = 100
        credit = 0

        while True:
            user_poke_hp = 100
            opp_poke_hp = 100

            opp = call()
            print(f"\nA Wild {opp} Appears!")
            
            choice = input("Do you want to fight or run? : ")
            a = choice.lower()
            if a.strip() == "fight":
                pass
            else:
                break

            time.sleep(1)

            print("\nAvailable Pokemons for Battle are : ")
            for i in user_poke:
                print(i, sep = ",")

            ask_poke = input("\nWhich Pokemon would you like to Choose ? : ")

            for j in user_poke:
                    if j.lower() == ask_poke.lower():
                        selected_poke = ask_poke
                    else:
                        continue

            while True:


                time.sleep(1)
                print("\nThe Moves of the Pokemon are : \n")

                cursor.execute("select poke_move, poke_index from poke where poke_name = '{}';".format(selected_poke))
                data = cursor.fetchmany(3)
                moves = [i[0] for i in data]
                index =  [i[1] for i in data]
                print(moves)
                print(index)                    
                
                ask_move1 = input("\nEnter Move : ")
                ask_move = ask_move1.strip()

                time.sleep(1)
                #USER POKE ATTACK
                #
                #
                #
            
                if ask_move.title() in moves:
                    no = moves.index(ask_move.title())
                    pass
                else:
                    continue
                print(f"\nYour {selected_poke.title()} used {ask_move.title()}\n\nThe Opponent Lost", index[no], "HP!")
                opp_hurt = index[no]
                opp_poke_hp = opp_poke_hp - opp_hurt
                if opp_poke_hp <= 0:
                    print(f"You Won!\nYou've Captured {opp}")
                    credit_gained = random.choice(credit_list)
                    credit = credit + credit_gained
                    print(f"You've Gained {credit_gained} Credits!")
                    user_poke.append(opp)
                    break
                else:
                    print(f"Your Opponents HP Is {opp_poke_hp}")

                time.sleep(1)
                #OPP POKE ATTACK
                #
                #
                #

                cursor.execute("select poke_move, poke_index from poke where poke_name = '{}';".format(opp))
                odata = cursor.fetchmany(3)
                omoves = [i[0] for i in odata]
                oindex =  [i[1] for i in odata]              

                
               
                opp_move = random.choice(omoves)
                index_opp = omoves.index(opp_move)
                print(f"\nThe Opponent used {opp_move}\n\nYour {selected_poke.title()} lost", oindex[index_opp], "HP!")
                user_hurt = oindex[index_opp]
                user_poke_hp = user_poke_hp - user_hurt
                if user_poke_hp <= 0:
                    print("You lost")
                    if len(user_poke)>1:
                        user_poke.remove(selected_poke.title())
                        print(user_poke)
                        poke_again = input("Choose Another Pokemon : ")
                        user_poke_hp = 100
                        user_poke.append(selected_poke.title())
                        poke_again_lower = poke_again.lower()
                        selected_poke = poke_again_lower.title()
                        continue
                    else:
                        break
                else:
                    print(f"Your {selected_poke.title()}'s HP Is {user_poke_hp}")

                    time.sleep(1)

                    ask_ifrun = input("\nDo you want to Keep Fighting or Run? (y/n) : ")
                    if ask_ifrun.lower().strip() == "y":
                        continue
                    else:
                        break
                        
            global creditOG
            creditOG = creditOG + credit
            looprun = input("\nDo you want to Play on? (y/n) : ")
            time.sleep(1)
            if looprun.lower()!="y":
                print("\nThe Pokemons You've Caught are : ")
                for i in user_poke:
                    print(i, sep = ",")
                print(f"Your Credit Points are {creditOG}")
                time.sleep(1)
                break  
    fight()

def store():
    #### SYNTAX ERROR ON CONTINUE ELSE
    
    while True:
        global creditOG
        global user_poke
        print("The Store has the following Pokemons Available : ")
        print("Pokemons\tPrice")
        print("Pikachu\t               2000")
        print("Charizard\t               2500")
        time.sleep(1)
        print(f"\nYou Have {creditOG} Credit's in your Bank!")
        time.sleep(1)
        ask_store = input("Do you want to Buy a Pokemon? (y/n) : ")
        ask_store_lower = ask_store.lower()

        if ask_store_lower.strip() == "n":
            break
        else:
            ask_store_poke = input("\nWhich Pokemon would you like to Buy : ")
            ask_store_poke_lower = ask_store_poke.lower()

        if ask_store_poke_lower.strip() == "pikachu":
            if creditOG >= 2000:
                ask_confirm = input("Confirm Buy? (y/n) : ")
                ask_confirm_lower = ask_confirm.lower()
                if ask_confirm_lower.strip() == "n":
                    break
                elif ask_confirm_lower.strip() == "y":
                    creditOG = creditOG - 2000
                    print("Bought!")
                    time.sleep(1)
                    adding_poke = ask_store_poke_lower.strip()
                    user_poke.append(adding_poke.title())
                    print("You Now have the Following Pokemons!")
                    for i in user_poke:
                        print(i)
                    break
                else:
                    continue
            else:
                    print("\nYou Do not Have Enough Credits!")
                    time.sleep(1)
                    continue

        if ask_store_poke_lower.strip() == "charizard":
            if creditOG >= 2000:
                ask_confirm = input("Confirm Buy? (y/n) : ")
                ask_confirm_lower = ask_confirm.lower()
                if ask_confirm_lower.strip() == "n":
                    break
                elif ask_confirm_lower.strip() == "y":
                    creditOG = creditOG - 2500
                    print("Bought!")
                    time.sleep(1)
                    adding_poke = ask_store_poke_lower.strip()
                    user_poke.append(adding_poke.title())
                    print("\nYou Now have the Following Pokemons!")
                    time.sleep(1)
                    for i in user_poke:
                        print(i)
                        
                    break
                else:
                    continue
            else:
                print("You Do not Have Enough Credits!")
                time.sleep(1)
                continue
            
def check_credit():
    global creditOG
    time.sleep(1)
    a = f"\nYou Have {creditOG} Credit's in your Bank Account!"
    print(a)
    time.sleep(1)

def gym_trainer():
    global creditOG
    gym_trainers = ["Misty", "Brock"]


    def call():
        attacker = random.choice(gym_trainers)
        return attacker

    def fight():
        global creditOG
        credit = 0

        while True:
            user_poke_hp = 100
            opp_poke_hp = 100

            if len(gym_trainers) == 0:
                print("\nNo Gym Trainer is Available right now!")
                time.sleep(1)
                break
            
            opp = call()
            print(f"\nYour Opponent is : {opp}")
            
            choice = input(f"Are you sure you want to fight {opp}? (y/n) : ")
            a = choice.lower()
            if a.strip() == "y":
                pass
            else:
                break

            if opp.lower() == "brock":
                cursor.execute("select distinct b_poke_name from brock_poke")
                lst = cursor.fetchmany(2)
                brock_poke = [i[0] for i in lst]
                opp_poke = random.choice(brock_poke)
                print(f"Brock called {opp_poke}!")
                cursor.execute("select b_poke_move, b_poke_index from brock_poke where b_poke_name = '{}';".format(opp_poke))
                odata = cursor.fetchmany(3)
                omoves = [i[0] for i in odata]
                oindex =  [i[1] for i in odata]


            elif opp.lower() == "misty":
                cursor.execute("select distinct m_poke_name from misty_poke")
                lst = cursor.fetchmany(2)
                misty_poke = [i[0] for i in lst]
                opp_poke = random.choice(misty_poke)
                print(f"Misty called {opp_poke}!")
                cursor.execute("select m_poke_move, m_poke_index from misty_poke where m_poke_name = '{}';".format(opp_poke))
                odata = cursor.fetchmany(3)
                omoves = [i[0] for i in odata]
                oindex =  [i[1] for i in odata]

                
            else:
                print("Trainers are Busy!")


            print("\nAvailable Pokemons for Battle are : ")
            for i in user_poke:
                print(i, sep = ",")

            ask_poke = input("\nWhich Pokemon would you like to Choose ? : ")
            selected_poke = ""

            for j in user_poke:
                    if j.lower() == ask_poke.lower():
                        selected_poke = ask_poke
                    else:
                        continue

            while True:


                time.sleep(1)
                print("\nThe Moves of the Pokemon are : \n")

                cursor.execute("select poke_move, poke_index from poke where poke_name = '{}';".format(selected_poke))
                data = cursor.fetchmany(3)
                moves = [i[0] for i in data]
                index =  [i[1] for i in data]
                print(moves)
                print(index)                    
                
                ask_move1 = input("\nEnter Move : ")
                ask_move = ask_move1.strip()

                time.sleep(1)
                #USER POKE ATTACK

            
                if ask_move.title() in moves:
                    no = moves.index(ask_move.title())
                    pass
                else:
                    continue
                print(f"\nYour {selected_poke.title()} used {ask_move.title()}\n\nThe Opponent Lost", index[no], "HP!")
                opp_hurt = index[no]
                opp_poke_hp = opp_poke_hp - opp_hurt
                if opp_poke_hp >0:
                    print(f"{opp_poke}'s HP Is {opp_poke_hp}")
                    
                if opp_poke_hp <= 0:
                    print(f"You've Beaten {opp_poke}")
                    credit_gained = random.choice(credit_list)
                    credit = credit + credit_gained

                    if opp.lower() == "brock":
                        brock_poke.remove(opp_poke)
                        if len(brock_poke)>0:
                            opp_poke = random.choice(brock_poke)
                            opp_poke_hp = 100
                            time.sleep(1)
                            print(f"\n{opp} Now Calls {opp_poke}")
                            continue
                        else:
                            print(f"You've Beaten {opp}! Congrats on your New Badge!")
                            gym_trainers.remove(opp)
                            break

                    if opp.lower() == "misty":
                        misty_poke.remove(opp_poke)
                        if len(misty_poke)>0:
                            opp_poke = random.choice(misty_poke)
                            opp_poke_hp = 100
                            time.sleep(1)
                            print(f"\n{opp} Now Calls {opp_poke}")
                            continue
                        else:
                            print(f"You've Beaten {opp}! Congrats on your New Badge!")
                            gym_trainers.remove(opp)
                            break
                        

                time.sleep(1)
                #OPP POKE ATTACK
                
                opp_move = random.choice(omoves)
                index_opp = omoves.index(opp_move)
                print(f"\nThe Opponent used {opp_move}\n\nYour {selected_poke.title()} lost", oindex[index_opp], "HP!")
                user_hurt = oindex[index_opp]
                user_poke_hp = user_poke_hp - user_hurt
                if user_poke_hp <= 0:
                        print("You lost")
                        time.sleep(1)
                        user_poke.remove(selected_poke.title())
                        if len(user_poke)>0:
                            print("\nYou Still have These Pokemons Available : ")
                            for i in user_poke:
                                print(i, sep = ",")
                            poke_again = input("Choose Another Pokemon : ")
                            user_poke_hp = 100
                            user_poke.append(selected_poke.title())
                            poke_again_lower = poke_again.lower()
                            selected_poke = poke_again_lower.title()
                            continue
                        else:
                            print("You've Lost")
                            break
                else:
                        print(f"Your {selected_poke.title()}'s HP Is {user_poke_hp}")

                        
            global creditOG
            creditOG = creditOG + credit
            looprun = input("\nDo you want to Fight Another Gym Trainer? (yes/no) : ")
            time.sleep(1)
            if looprun.lower().strip()!="yes":
                break
            else:
                continue
    fight()

    
def check_poke():
    global user_poke
    time.sleep(1)
    print("\nThe Pokemons You've Caught are : ")
    for i in user_poke:
        print(i)
    time.sleep(1)

print("\nWelcome to the Pokemon World!\nCurrently under Construction!\nConquer the World with your Special Pikachu and Pokemon Friends")
print(f"You Have {creditOG} Credit's to begin with!") 
time.sleep(1)
while True:
    print("\nYou Can Currently")
    time.sleep(1)

    print("\n1) Buy Pokemon from Store")
    print("2) Catch Wild Pokemons")
    print("3) Check Bank Account")
    print("4) Check Caught Pokemons")
    print("5) Fight a Gym Trainer")
    print("6) Exit")
    time.sleep(1)
    ask_true = int(input("\nChoose an Option : "))
    if ask_true == 1:
        store()
    elif ask_true == 2:
        pokemon()
    elif ask_true == 3:
        check_credit()
    elif ask_true == 4:
        check_poke()
    elif ask_true == 5:
        gym_trainer()
    elif ask_true == 6:
        exit()
    else:
        print("Enter Correct Option : ")
        continue
            



            
