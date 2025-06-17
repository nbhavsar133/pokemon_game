
import random
from names_generator import generate_name
#from simple_term_menu import TerminalMenu
name1=generate_name(style='capital')
'''import win32api
import os
import time'''




'''
- printing statements
- lists, indexing
- loops (for, while)
- defining functions (parameters and arguments, methods for classes)
- variables and assigning variables
- data types (string, int, float, boolean)
- if statements (if, else, elif)
- python keywords (true, false, return, break)
- classes & objects (needs revison)
'''


'''
text-based game
pokemon game
how does pokemon work?

every pokemon has ability to attack - the attack command needs to know who to attack - this can change depending on who is being attacked


'''


class Trainer():
    def __init__(self,name):
        self.squad = []
        self.name = name
    def main_pokemon(self):
        choose = "Who is your main Pokemon, Ash?"
    



#Ash = Trainer("Ash")
#print(Ash.name)


class Pokemon():
    def __init__(self,name,power):
        self.power = power
        self.name = name
        self.attack_power = random.randrange(20,50)
        self.health = 100
        
    def attack(self,victim):
        attack_result = random.randrange(1,4)
        if attack_result==1:
            victim.health-=self.attack_power
            if victim.health<=0:
                # victim.dead()
                return f"{victim.name} was hit by {self.name} with an attack power of {self.attack_power}. {victim.name} is dead."
            return f"{victim.name} was hit by {self.name} with an attack power of {self.attack_power}. {victim.name}'s health is now {victim.health}."
        
        if attack_result==2:
            num = random.randrange(2,5)
            self.multiplier(num)
            victim.health-=self.attack_power
            if victim.health<=0:
                # victim.dead()
                #print(f"{victim.name} was hit by {self.name} with an attack power of {self.attack_power} and a lucky multiplier of {num}.")
                return f"{victim.name} was hit by {self.name} with an attack power of {self.attack_power} and a lucky multiplier of {num}. {victim.name} is dead."
            return f"{victim.name} was hit by {self.name} with an attack power of {self.attack_power} and a lucky multiplier of {num}. {victim.name}'s health is now {victim.health}."
            
        if attack_result==3:
            return f"{self.name}'s attack has missed."
    def multiplier(self,factor):
        self.attack_power*=factor
    # def dead(self):
    #     print(f"{self.name} is dead.")
class Game():
    def __init__(self):
        self.scores = []
        self.fighters=[]
        self.trainers=[]
        self.types=["electric","fire","water","dragon","rock","psychic","dark"]
        #self.options = []
        self.Ash = Trainer("Ash")
    def make_trainers(self):
        for n in range(5):
            trainer_name=generate_name(style='capital')
            trainer=Trainer(trainer_name)
            self.trainers.append(trainer)
            print(trainer.name)
            print()
    def make_pokemon(self):
        for i in range(len(self.trainers)):
            for j in range(5):
                pokemon_name= generate_name(style='capital')
                pokemon_power = random.choice(self.types)
                create_pokemon=Pokemon(pokemon_name, pokemon_power)
                specific=self.trainers[i]
                specific.squad.append(create_pokemon)
            '''print()
            print(f"{specific.name}'s Squad: ")
            for m in specific.squad:
                print(f"Name: {m.name} | Type: {m.power} | Attack Power: {m.attack_power}")'''
    '''def get_user_input(choices):
       
        current_choice = 0
        while True:
            
            
            for c in choices:
                p = choices.index(c)
                if p==current_choice:
                    print("> " + c)

                else:
                    print(c)
            print(current_choice)
                
            if win32api.GetAsyncKeyState(0x26) & 0x8000:
                current_choice-=1
                ''''''if current_choice == 0:
                    current_choice = ''''''
            
            if win32api.GetAsyncKeyState(0x28) & 0x8000:
                current_choice+=1
            
            time.sleep(0.1)'''
            

          




            




    #def cage_match():



        
    def team_battles(self):
        '''
         - keep track of score and print score***
         - continue moves/attacks and keep game running until an event occurs which creates a winner/loser***
         - have multipliers for attack power
         - have winner/loser and result of match
         - prizes for winning team(?)
        
        '''
        enemy_trainer = random.choice(self.trainers)
        fighter_1 = self.Ash.squad[0]
        fighter_2 = self.Ash.squad[1]
        enemy_pokemon1 = enemy_trainer.squad[0]
        enemy_pokemon2 = enemy_trainer.squad[1]
        print("IT'S TIME TO FIGHT!!!!!!")
        print(f"Ash, your fighters are: {fighter_1.name} and {fighter_2.name}. {fighter_1.name} is your primary fighter.")
        print(f"The enemy is {enemy_trainer.name} and their fighters are {enemy_pokemon1.name} and {enemy_pokemon2.name}. {enemy_pokemon1.name} is the primary fighter.")


        def make_move(fighter,ep1,ep2):
            if fighter.health>0:
                if ep1.health>0 and ep2.health>0:
                    fighter_move = int(input(f"Who would you like {fighter.name} to attack? Type 0 for {ep1.name} or 1 for {ep2.name}: "))
                    while fighter_move!=0 and fighter_move!=1:
                        print("Please choose an enemy fighter to attack.")
                        fighter_move = int(input(f"Who would you like {fighter.name} to attack? Type 0 for {ep1.name} or 1 for {ep2.name}: "))
                elif ep1.health<=0:
                    print(fighter.attack(ep2))
                elif ep2.health<=0:
                    print(fighter.attack(ep1))
               
                print(fighter.attack(enemy_trainer.squad[fighter_move]))
                print()
            return
        
        def enemy_move(enemy_fighter,p1,p2):
            if p1.health>0 and p2.health>0:
                Ash_victim = random.randrange(0,2)
                print(enemy_fighter.attack(self.Ash.squad[Ash_victim]))
            elif p1.health<=0:
                print(enemy_fighter.attack(p2))
            elif p2.health<=0:
                print(enemy_fighter.attack(p1))
        while True:
          #  move1 = random.randrange(0,2)
           # if move1==0:
            print("Your move, Ash.")
            make_move(fighter_1,enemy_pokemon1,enemy_pokemon2)
            make_move(fighter_2,enemy_pokemon1,enemy_pokemon2)

        
        
            if (fighter_1.health<=0 and fighter_2.health<=0) or (enemy_pokemon1.health<=0 and enemy_pokemon2.health<=0):
                break
            #elif move1==1:
            print(f"It is {enemy_trainer.name}'s move.")

            enemy_move(enemy_pokemon1,fighter_1,fighter_2)
            print()
            enemy_move(enemy_pokemon2,fighter_1,fighter_2)
            print()
            user_check = input("Please click enter to continue.")
            print()
        print("Game over.")
        



    def adding(self):
        add = input("Would you like to add new Pokemon to the squad? y/n " )
        while add !="n":
            naming = input("What would you like to name the Pokemon? ")
            type = int(input("What is the pokemon's type? 1: electric, 2: fire, 3: water, 4: dragon, 5: rock, 6: psychic, 7: dark "))
            if type == 1:
                pokemon_type = "electric"
            elif type==2:
                pokemon_type="fire"
            elif type==3:
                pokemon_type="water"
            elif type==4:
                pokemon_type="dragon"
            elif type==5:
                pokemon_type="rock"
            elif type==6:
                pokemon_type="psychic"
            elif type==7:
                pokemon_type="dark"


            new_pokemon = Pokemon(naming,pokemon_type)
            self.Ash.squad.append(new_pokemon)
            print("Your pokemon has been added.")
            add = input("Would you like to add new Pokemon to the squad? y/n ")
        print("Ash's squad:")
        for i in self.Ash.squad:
            print(f"Name: {i.name} | Type: {i.power} | Attack Power: {i.attack_power}")
Game1=Game()
generate=Game1.make_trainers()
Game1.make_pokemon()


Pikachu = Pokemon("Pikachu","electric",)
Game1.Ash.squad.append(Pikachu)
#print(Ash.squad[0].name)

Squirtle = Pokemon("Squirtle","water")
Game1.Ash.squad.append(Squirtle)
print("Ash's squad:")
for i in Game1.Ash.squad:
    print(i.name)



print(f"Hi, my name is {Pikachu.name}. My type is {Pikachu.power}.")
print(f"Hi, my name is {Squirtle.name}. My type is {Squirtle.power}.")


print()
print()
print()

#Game.adding()

Game1.team_battles()

'''
a = Pikachu.attack(Squirtle)
print(a)
'''
