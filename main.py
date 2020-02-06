from Classes.game import Person,bcolors
from termcolor import colored
from Classes.magic import Spell
import random
# Create Black Magic
fire = Spell("Fire",10,60,"black")
thunder = Spell("Thunder",15,120,"black")
quake = Spell("Quake",25,230,"black")

#Create healing magic
cure= Spell ("Cure",12,120,"white")
love= Spell ("Love",20,240,"white")

magic=[fire,thunder,quake,cure,love]


# magic=[
#     {
#         "name":"Fire",
#         "cost":10,
#         "dmg":60

#     },
#     {
#         "name":"Thunder",
#         "cost":15,
#         "dmg":160

#     },
#     {
#         "name":"Blizzard",
#         "cost":25,
#         "dmg":240

#     }
# ]


player = Person(1000,65,30,magic)
enemy = Person(250,65,30,magic)

running =True 
i=0

##PLAYER CHOICE FOR ATTACK##
print(colored("ATTACK", "red"))
while running:
    print("*************************************")
    #Allowing player to choose between attack and magic 
    player.choose_action()
    #minus 1 as indexing starts from 0
    choice=int(input("Choose action:"))-1
    print("You choose {}".format(player.actions[int(choice)]))


    if choice == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attaked with force ", dmg , " making your Enemy HP:", enemy.get_hp())
    else:
        #Allowing Player to choose Spell
        player.choose_magic()
        print("Your mp is:", player.get_mp())
        magic_choice = int(input("Choose magic: "))-1
        
        # magic_dmg =player.generate_spell_damage(magic_choice)
        # spell = player.get_spell_name(magic_choice)
        # cost = player.get_spell_mp_cost(magic_choice)
        
        spell=player.magic[magic_choice]
        magic_dmg=spell.generate_damage()
        current_mp= player.get_mp()

        if spell.cost > current_mp:
            print("ALERT!!!!  Not enough MP")
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(spell.name ,"attacked YOUR ENEMY with force ", str(magic_dmg), " making your Enemy HP:", enemy.get_hp())

    ##ENEMY AI FOR ATTACK##

    if enemy.get_mp() >= 10:
        enemy_choice=int(random.randrange(0,2))
        if enemy_choice==0:
            
            enemy_dmg=enemy.generate_damage()
            player.take_damage(enemy_dmg)
            print("Enemy attacks for", enemy_dmg, "point. Your HP:",player.get_hp())
        else:

            enemy_choice_magic=int(random.randrange(0,3))
            spell=player.magic[enemy_choice_magic]
            current_mp= player.get_mp()
                #magic_choice = int(input("Choose magic: "))-1
            if spell.cost > current_mp:
                enemy_choice_magic=int(random.randrange(0,2))
            if spell.cost > current_mp:
                enemy_choice_magic=0
            
            enemy_magic_dmg=spell.generate_damage()
                 
            
                    
            

            enemy.reduce_mp(spell.cost)
            player.take_damage(enemy_magic_dmg)
            print(spell.name ,"attacked YOU with force ", str(enemy_magic_dmg), " making your HP:", player.get_hp())


    else:
        enemy_choice==0
        enemy_dmg=enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print("Enemy attacks for", enemy_dmg, "point. Your HP:",player.get_hp())

 ##ENEMY AI FOR HEAL##
    if enemy.get_mp() >= 12:
        if enemy.get_hp() <= 250:
            #print("ALERT!!!! You are running out of health")

            #0->YES, 1->NO
            enemy_answer= int(random.randrange(0,2))
            #enemy_answer=0
            if enemy_answer == 0:
                
                enemy_magic_choice = int(random.randrange(0,2))+3
                    
                spell=enemy.magic[enemy_magic_choice]
                current_mp= enemy.get_mp()
                if spell.cost > current_mp:
                    enemy_magic_choice = 3
                enemy_magic_heal=spell.generate_heal()
                print("in loop")
                current_mp= enemy.get_mp()
                
                 

                              
                enemy.reduce_mp(spell.cost)
                enemy.take_heal(enemy_magic_heal)
                print(spell.name ,"healed your enemy with", str(enemy_magic_heal), " making their HP:", enemy.get_hp())


    

##PLAYER CHOICE FOR HEAL###
    
    if player.get_mp()>=12:
        if player.get_hp() < 250:
            print("ALERT!!!! You are running out of health")
            answer=input("Would you like to heal?(Y/N)")
            if answer == "Y":
                player.choose_heal()
                print("Your mp is:", player.get_mp())
                magic_choice = int(input("Choose magic: "))+2
                
                spell=player.magic[magic_choice]
                magic_heal=spell.generate_heal()
                current_mp= player.get_mp()
                if spell.cost > current_mp:
                    print("ALERT!!!!  Not enough MP")
                    continue
                
                player.reduce_mp(spell.cost)
                player.take_heal(magic_heal)
                print(spell.name ,"healed you with", str(magic_heal), " making your HP:", player.get_hp())


##FOR THE HP BAR###
    E_HP=""
    Enemy_hp_per=(enemy.get_hp()/enemy.get_max_hp())*100
    Enemy_hp_per_bar=int((Enemy_hp_per/100)*26)
    for i in range(Enemy_hp_per_bar):
        E_HP+="█"
    for i in range(26-Enemy_hp_per_bar):
        E_HP+=" "    
        
    P_HP=""
    Player_hp_per=(player.get_hp()/player.get_max_hp())*100
    Player_hp_per_bar=int((Player_hp_per/100)*26)
    for i in range(Player_hp_per_bar):
        P_HP+="█"
    for i in range(26-Player_hp_per_bar):
        P_HP+=" "

    P_MP=""
    Player_mp_per=(player.get_mp()/player.get_max_mp())*100
    Player_mp_per_bar=int((Player_mp_per/100)*26)
    for i in range(Player_mp_per_bar):
        P_MP+="█"
    for i in range(26-Player_mp_per_bar):
        P_MP+=" "

    
    #print(E_HP,Enemy_hp_per_bar)
    #print(P_HP,Player_hp_per_bar)

    print("**************************************")
    print("Player")
    print()
    print("Enemy HP:", str(enemy.get_hp())+ "/"+ str(enemy.get_max_hp()),"     |{}|".format(E_HP))
    
    print()
    print("Your HP:",str(player.get_hp())+ "/"+ str(player.get_max_hp()),"        |{}|".format(P_HP))
    
    print()
    print("Your MP:", str(player.get_mp())+ "/"+ str(player.get_max_mp()),"          |{}|".format(P_MP))
    


    if enemy.get_hp()==0:
        print("WINNER WINNER CHICKEN DINNER")
        break
    elif player.get_hp()==0:
        print("TRY AGAIN")
        break