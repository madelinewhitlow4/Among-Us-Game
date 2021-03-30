
import random
import json
import sys
import random
import time
import os
from PIL import Image

#IF you don't have this installed you can comment out lines that begin with cprint()
from termcolor import cprint 
from pyfiglet import figlet_format



class Task:
    '''This class creates different tasks by calling different methods based on the class name, it takes the input of name''' 
    
    # Initializing the task name upon creation
    def __init__(self, name):
        self.name = name
    
    # Math task will generate a math equation for the user to solve 
    # if they don't answer correctly they must continue until they do
    def math_game(self):
        '''Generates a math equation when called - takes no inputs'''
        ans = 0
        ans2 = 1
        # Generating 2 random integers for the math problem
        while ans != ans2:
            x = random.randint(0,1000)
            y = random.randint(0,1000)
            operator = ['-', '+', '*', '/']
            
            # Selecting an operator for the math problem
            op_num = random.randint(0,3)
            
            # Printing user explanation and the equation and asking for an input
            print("Let's do some math!")
            print("Please answer the math problem listed below - if you get it wrong you'll have to try again.")
            print("Round your answer to two decimal places.")
            print(f'{x} {operator[op_num]} {y}')
            ans2 = float(input())
            # Depending on the operator that was randomly chosen we'll compute the ideal solution 
            if op_num == 0:
                ans = x - y
                ans = round(ans,2)
            if op_num == 1:
                ans = x + y
                ans = round(ans,2)
            if op_num == 2:
                ans = x * y
                ans = round(ans,2)
            if op_num == 3:
                ans = x / y
                ans = round(ans,2)
            if op_num == 4:
                ans = x**y
                ans = round(ans,2)
        print('You did it!')
        return 'done'

    def quotes(self):
        '''Generates a quote and a list of possible authors - takes no inputs'''
        # Initializing answer variables 
        ans = 10
        ans2 = 11
        # Importing quotes data from a json file and pulling out the 'quotes' 
        with open("Task Files/quotes.json") as f:
            quotes_data = json.load(f)
        quotes_dict = quotes_data['quotes']
        
        # Generating user instructions 
        print("Can you identify the author to this famous quote?")
        print("We'll give you a list of options - select the correct one using the numeric input option.")
        print("If you get it wrong you'll have to try again.")
        print("Good luck!")
        while ans != ans2:
            # Selecting a random quote from the data set and then storing the author in a list
            # for loop will randomly collect other authors in the answer list
            q_num = random.randint(0,len(quotes_dict))
            print('Who said: ')
            print(quotes_dict[q_num]['quote'])
            ans_list = []
            ans_list.append(quotes_dict[q_num]['author'])
            while len(ans_list) < 4:
                opt2 = random.randint(0,len(quotes_dict))
                if quotes_dict[opt2]['author'] not in ans_list:
                    ans_list.append(quotes_dict[opt2]['author'])
                ans = 0
            count = 0
            for choice in ans_list:
                print(f'{count} - {choice}')
                count +=1
            ans2 = int(input())

            if ans != ans2:
                print('Wrong! Try again')
                print(f"The correct answer was {quotes_dict[q_num]['author']}")
        print("Nice job!! You won!")

    def riddle(self):
        '''Generates a riddle and a list of possible answers - takes no inputs'''
        # Initializing answer variables 
        ans = 10
        ans2 = 11
        # Importing riddles data and identifying 'riddle' and 'answer' 
        # the riddles dictionary is unique in that it 
        # first requires a number represented as a string to access values
        with open("Task Files/riddles.json") as f:
            riddles_data = json.load(f)
        print("Can you identify the answer to this riddle?")
        print("We'll give you a list of options - select the correct one using the numeric input option.")
        print("If you get it wrong you'll have to try again.")
        print("Good luck!")
        while ans != ans2:
            num = random.randint(1,len(riddles_data))
            num = str(num)
            print('The riddle is ... ')
            print(riddles_data[num]['riddle'])
            ans_list = []
            ans_list.append(riddles_data[num]['answer'])
            while len(ans_list) < 4:
                opt2 = random.randint(1,len(riddles_data) - 1)
                opt2 = str(opt2)
                if riddles_data[opt2]['answer'] not in ans_list:
                    ans_list.append(riddles_data[opt2]['answer'])
                ans = 0
            count = 0
            for choice in ans_list:
                print(f'{count} - {choice}')
                count +=1
            ans2 = int(input())

            if ans != ans2:
                print('Wrong! Try again')
                print(f"The correct answer was {riddles_data[num]['answer']}")
        print("Nice job!! You won!")   

    def trivia(self):
        '''Generates a jeopardy question and a list of possible answers - takes no inputs'''
        # Initializing answer variables
        ans = 10
        ans2 = 11
        # Opening jeopardy questions json file and randomly selecting a question
        # Collecting a list of random other answers, this technically isn't a very good option
        # since most of the answers don't make sense but I didn't want to require users to input
        # values that weren't numeric
        with open("Task Files/JEOPARDY_QUESTIONS1.json") as f:
            trivia_data = json.load(f)
        print("Can you answer this jeopardy question?")
        print("We'll give you a list of options - select the correct one using the numeric input option.")
        print("If you get it wrong you'll have to try again.")
        print("Good luck!")
        while ans != ans2:
            num = random.randint(0,len(trivia_data) - 1)
            print('Your jeopardy category is ... ')
            print(trivia_data[num]['category'])
            print('Your jeopardy question is ... ')
            print(trivia_data[num]['question'])
            ans_list = []
            ans_list.append(trivia_data[num]['answer'])
            while len(ans_list) < 4:
                opt2 = random.randint(1,len(trivia_data) - 1)
                if trivia_data[opt2]['answer'] not in ans_list:
                    ans_list.append(trivia_data[opt2]['answer'])
                ans = 0
            count = 0
            for choice in ans_list:
                print(f'{count} - {choice}')
                count +=1
            ans2 = int(input())
            if ans != ans2:
                print('Wrong! Try again')
                print(f"The correct answer was {trivia_data[num]['answer']}")
        print("Nice job!! You won!")   

    def wordwisdom(self):
        '''Generates a word and a list of possible defintitions - takes no inputs'''
        # Initializing answer variables 
        ans = 10
        ans2 = 11
        # Importing dictionary data from a json file 
        with open("Task Files/dictionary.json") as f:
            dictionary_data = json.load(f)
        
        # Generating user instructions 
        print("Can you identify the defintion of this word?")
        print("We'll give you a list of options - select the correct one using the numeric input option.")
        print("If you get it wrong you'll have to try again.")
        print("Good luck!")
        while ans != ans2:
            # Selecting a random word from the data set and then storing the definition in a list
            # for loop will randomly collect other definitions in the answer list
            word = random.choice(list(dictionary_data.keys()))
            print('What does this word mean? ')
            print(word)
            ans_list = []
            ans_list.append(dictionary_data[word])
            while len(ans_list) < 4:
                opt2 = random.choice(list(dictionary_data.keys()))
                if dictionary_data[opt2] not in ans_list:
                    ans_list.append(dictionary_data[opt2])
                ans = 0
            count = 0
            for choice in ans_list:
                print(f'{count} - {choice}')
                count +=1
            ans2 = int(input())

            if ans != ans2:
                print('Wrong! Try again')
                print(f"The correct answer was {dictionary_data[word]}")
        print("Nice job!! You won!")


class Character:
    '''Creating a new character giving them a team (randomly assigned)
        This takes initial variables of color and name. This class has various methods which allow 
        characters to accomplish actions throughout the game'''
    
    def __init__(self,name, color):
        self.color = color
        self.name = name
        # If a character has been killed by an imposter their status will be changes to 'Dead'
        self.status = 'Alive'
        # characters will be randomly assigned a role with 
        # 70% probability of crew mate and 30% prob of imposter
        weights = [.3,.7]
        choices = [0,1]
        self.role = random.choices(choices, weights)
        if self.role[0] == 0:
            self.role_name = "Imposter"
        else:
            self.role_name = "Crew Mate"
        
        
    # When the character class is called the output will be something like 'madeline (pink)'
    def __repr__(self):
        print_str = self.name + ' (' + self.color + ')'
        return print_str
    
    
    # Checks all the rooms in the map to find where the character is and prints the location
    # This method requires the input of the map where the character has been initialized. 
    def locate_character(self, AmongUsMap):
        for room in AmongUsMap.rooms_dict:
            if self in room.characters_in_room:
                current_room = room
                return current_room
    
    # Move character from one room to another  
    # This method requires the input of the map where the character has been initialized. 
    def enter_room(self, room_to_enter, AmongUsMap):
        
        #locating where the character was and removing their name from room list
        current_room = self.locate_character(AmongUsMap)
        current_room.characters_in_room.remove(self)
        # adding name to room object and updating characters location
        room_to_enter.characters_in_room.append(self)
        
    # This method is only called for the main character (user interacting with the program)
    # If the character's role is imposter this method will be called to 'kill' other players
    # First we check to see if other players are in room 
    # and if they are crew mates (not fellow imposters) 
    # Then we ask the user if they would like to kill, if there are other crew mates 
    # in the room when they kill then they will also die because they have been caught 
    def main_kill(self, AmongUsMap):
        current_room = self.locate_character(AmongUsMap)
        players_in_room = current_room.characters_in_room
        # check if there are other players in the room
        print('-'*50)
        time.sleep(2)
        
        crew_in_room = []
        for player in players_in_room:
            if player.role[0] == 1:
                crew_in_room.append(player)
                    
        if len(players_in_room) == 1:
            print(f"No one else is in the {current_room.room_name} so you can't kill anyone - try a different room.")
            time.sleep(2)
            for player in AmongUsMap.player_list:
                current_room = player.locate_character(AmongUsMap)
                print(f"{player} is a {player.role_name} and they're currently in the {current_room.room_name}") 
                
        elif len(players_in_room) >1 and len(crew_in_room) <1:
            print("The other player in this room is an imposter!\n so you can't kill them, you need to move rooms again.")
            time.sleep(2)
            for player in AmongUsMap.player_list:
                current_room = player.locate_character(AmongUsMap)
                print(f"{player} is a {player.role_name} and they're currently in the {current_room.room_name}") 
                
        elif len(crew_in_room) > 0:
            action = input("There are crewmates in the room\nbut you're not sure how many \nand if you kill someone while a crewmate is in the room \nyou may get caught. \nDo you want to kill someone? y/n")
            if action == 'y':
                print()
                crew_num = len(crew_in_room)
                killed_player = crew_in_room[0]
                print(f'You killed {killed_player}!!!')
                killed_player.status = 'Dead'
                killed_player.locate_character(AmongUsMap)
                players_in_room.remove(killed_player)
                if crew_num > 1:
                    print('Uh oh...............................')
                    print(f'You killed a crewmate but {crew_in_room[1]} saw you do it!')
                    print(f"The remaining crew members took a vote.. they can't keep an imposter on this ship")
                    self.status = 'Dead'
  
            if action == 'n':
                print("You're going to have to be more aggressive than that if you want to win!")
                print("Let's try a different room.")
                time.sleep(2)
                for player in AmongUsMap.player_list:
                    current_room = player.locate_character(AmongUsMap)
                    print(f"{player} is a {player.role_name} and they're currently in the {current_room.room_name}") 

    
    # This method is only called for the non main characters
    # If the character's role is imposter this method will be called to 'kill' other players
    # this method works the same as main_kill except that the imposter will always kill
    # and this method doesn't require user inputs
    def kill(self, AmongUsMap):
        current_room = self.locate_character(AmongUsMap)
        players_in_room = current_room.characters_in_room
        
        crew_in_room = []
        for player in players_in_room:
            if player.role[0] == 1:
                crew_in_room.append(player)
        if len(players_in_room) > 1 and len(crew_in_room) > 0:
            killed_player = crew_in_room[0]
            if killed_player == AmongUsMap.main_character:
                killed_player.status = 'Dead'
            elif killed_player != AmongUsMap.main_character and len(crew_in_room) > 1:
                print('-'*50)
                print(f'{killed_player} was killed in the {current_room.room_name}!!!')
                print(f'But {crew_in_room[1]} was also in {current_room.room_name} and saw {self} do it!')
                print(f"We can't keep these imposters aboard! The crew takes it to a vote and {self} is voted off.")
                killed_player.status = 'Dead'
                self.status = 'Dead'
                players_in_room.remove(killed_player)
                players_in_room.remove(self)
                    
            elif killed_player != AmongUsMap.main_character and len(crew_in_room) == 1:
                killed_player = crew_in_room[0]
                print('-'*50)
                print(f'Someone killed {killed_player} in the {current_room.room_name}!!!')
                killed_player.status = 'Dead'
                players_in_room.remove(killed_player)
                    
    # This method is called for the main user when they come to a room and have to complete a task
    # This method calls the Task class associated with the room and then triggers a task method to 
    # start the game/task.
    def invoke_task(self, AmongUsMap):
        current_room = self.locate_character(AmongUsMap)
        if current_room not in AmongUsMap.room_task_dict:
            print("You've already completed the task in this room, try going to one of these rooms: ")
            for room in AmongUsMap.room_task_dict:
                print(room.room_name)
            time.sleep(2) 
        else:
            current_task = AmongUsMap.room_task_dict[current_room]
            print(f"You're in the {current_room.room_name} so your task is {current_task.name}.")
            print('-'*50)
            time.sleep(2)
            if current_task.name == 'Math':
                os.system('clear')
                cprint(figlet_format('Math!', font='larry3d'), 'green', attrs=['bold'])
                current_task.math_game()
            if current_task.name == 'Trivia':
                os.system('clear')
                cprint(figlet_format('Trivia!', font='larry3d'), 'green', attrs=['bold'])
                current_task.trivia()
            if current_task.name == 'Riddles':
                os.system('clear')
                cprint(figlet_format('Riddles!', font='larry3d'), 'green', attrs=['bold'])
                current_task.riddle()
            if current_task.name == 'Word Wisdom':
                os.system('clear')
                cprint(figlet_format('Word Wisdom!', font='larry3d'), 'green', attrs=['bold'])
                current_task.wordwisdom()
            if current_task.name == 'Famous Quotes': 
                os.system('clear')
                cprint(figlet_format('Famous Quotes!', font='larry3d'), 'green', attrs=['bold'])
                current_task.quotes()

            time.sleep(2)
            print('-'*50)
            print(f"You've completed the {current_task.name} task! Nice work!")
            del AmongUsMap.room_task_dict[current_room]
            print(f"You have {len(AmongUsMap.room_task_dict)} tasks left.")
            time.sleep(2)  

class AmongUsMap:
    '''Generates the map, associated players and associated rooms when called. This class takes inputs of the specific map you want to play (as a numeric value) and a main character.'''
    maps_list = ['Original', 'Hogwarts', 'The Office']
    
    def __init__(self,map_selection, main_character):
        self.maps_list = ['Original', 'Hogwarts', 'The Office']
        self.map_name = self.maps_list[map_selection]
        self.main_character = main_character
        
        # Depending on the choice of map there are different sets of players involved
        # as well as different rooms and a different map image that will display. 
        # The rooms dictionary is called to determine based on 
        # which room a player is in the rooms they can then move to since not every room is connected
        if self.maps_list[map_selection].lower() == 'original':
            scooby = Character('Toast', 'brown')
            velma = Character('Rae', 'orange')    
            daphne = Character('Poki', 'yellow')    
            shaggy = Character('Corpse', 'green')
            fred = Character('Dream', 'blue')
            self.player_list =[scooby, velma, daphne, shaggy, fred, self.main_character]
            cafeteria = Room('Cafeteria', self.player_list)
            cockpit = Room('Cockpit')
            weapons = Room('Weapons')
            engine = Room('Engine')
            electrical = Room('Electrical')
            self.rooms_dict = {cafeteria: [cockpit, weapons, engine, electrical] ,cockpit: [electrical, cafeteria, engine] ,weapons: [electrical, cafeteria, engine], engine: [cockpit, cafeteria, weapons], electrical: [cockpit, cafeteria, weapons]}
            self.mapimage = Image.open("Map Files/Among Us Map.png")

        elif self.maps_list[map_selection].lower() == 'hogwarts':
            scooby = Character('Harry Potter', 'brown')
            velma = Character('Hagrid', 'orange')    
            daphne = Character('Ron Weasley', 'yellow')    
            shaggy = Character('Hermione Granger', 'green')
            fred = Character('Dumbledore', 'blue')
            self.player_list =[scooby, velma, daphne, shaggy, fred, self.main_character]
            cafeteria = Room('The Great Hall', self.player_list)
            cockpit = Room('Gryffindor Common Room')
            weapons = Room('Library')
            engine = Room("Head Master's Office")
            electrical = Room('Room of Requirement')
            self.rooms_dict = {cafeteria: [cockpit, weapons, engine, electrical] ,cockpit: [electrical, cafeteria, engine] ,weapons: [electrical, cafeteria, engine], engine: [cockpit, cafeteria, weapons], electrical: [cockpit, cafeteria, weapons]}
            self.mapimage = Image.open("Map Files/HP_map.png")

            
        elif self.maps_list[map_selection].lower() == 'the office':
            scooby = Character('Jim Halpert', 'brown')
            velma = Character('Pam Beesly', 'orange')    
            daphne = Character('Michael Scott', 'yellow')    
            shaggy = Character('Dwight Schrute', 'green')
            fred = Character('Ryan (the temp)', 'blue')
            self.player_list =[scooby, velma, daphne, shaggy, fred, self.main_character]
            cafeteria = Room('Dunder Mifflin', self.player_list)
            cockpit = Room('The Annex')
            weapons = Room("Michael's Office")
            engine = Room("Vance Refrigeration")
            electrical = Room('The Warehouse')
            self.rooms_dict = {cafeteria: [cockpit, weapons, engine, electrical] ,cockpit: [electrical, cafeteria, engine] ,weapons: [electrical, cafeteria, engine], engine: [cockpit, cafeteria, weapons], electrical: [cockpit, cafeteria, weapons]}
            self.mapimage = Image.open("Map Files/office_map.png")
            
        else:
            print("Invalid input.. doesn't matter - let's play the original map")
            self.map_name == 'original'
            
        self.rooms_list = [cafeteria, cockpit, weapons, engine, electrical]    
        # Every time the game is played a new combination of room and task will be generated
        math = Task('Math')
        trivia = Task('Trivia')
        riddle = Task('Riddles')
        wordwisdom = Task('Word Wisdom')
        quotes = Task('Famous Quotes')
        self.task_list = [math, trivia, riddle, wordwisdom, quotes]
        random.shuffle(self.task_list)
        self.room_task_dict = {}
        for i in range(0,len(self.task_list)):
            self.room_task_dict[self.rooms_list[i]] = self.task_list[i]


class Room:
    '''Generates a room class, takes a room_name as input as well as player_list, the player list is optional and should only be given when the room is the 'main' room or the starting point of all players.'''  

    # Characters in room is used to identify who is in the room at any given time. 
    def __init__(self,room_name, player_list = 'na'):
        self.room_name = room_name
        self.characters_in_room = []
        if self.room_name == 'Cafeteria' or self.room_name == 'Dunder Mifflin' or self.room_name == 'The Great Hall':
            for player in player_list:
                self.characters_in_room.append(player)

def Game_Setup(name, color_selection, map_name = 'Original'):
    '''This function will start the game and initiate the classes needed'''

    # generating players and assigning roles
    main_character = Character(name, color_selection)

    # Creating the map
    map1 = AmongUsMap(map_name, main_character)
    
    return main_character, map1
                
                
class GamePlay():
    '''This class initiaties the game by asking for user inputs for the main character and map
    within the class there are different actions that are called as the game moves forward.'''

    
    # This method opens the game by explaining the rules, asking for user inputs
    # This is where the main character understands their role and thus their path forward (imposter/crewmate)
    def opening(self):
        os.system('clear')
        cprint(figlet_format('Among Us!', font='larry3d'), 'blue', attrs=['bold'])
        time.sleep(2)
        print(f'Welcome to Among Us! The game where you trust no one!')
        time.sleep(3)
        
        name = input("Input a username: ")
        print('-'*50)
        colors = ['pink', 'purple', 'red', 'black', 'white', 'turquoise']
        maps_list = ['Original', 'Hogwarts', 'The Office']
        count = 0
        for color in colors:
            print(f'{count} - {color}')
            count +=1
            
        color_num = int(input("What color do you want to be? (input the number from the list above)"))
        print('-'*50)
        color_selection = colors[color_num]
        count = 0
        for map1 in maps_list:
            print(f'{count} - {map1}')
            count +=1
        map_num = int(input("Which map do you want to play? (input the number from the list above)"))
        print('-'*50)
        self.main_character, self.map1 = Game_Setup(name, color_selection, map_num)
        self.player_list = self.map1.player_list
        print()
        print()
        print('The manifest for the ship is: ')
        print()
        time.sleep(3)

        for player in self.player_list:
              print(player)
        print('-'*50)
        print(f'You are a {self.main_character.role_name} aboard a spacecraft.') 
        time.sleep(3)

        if self.main_character.role[0] == 0:
            print("""Your mission is to kill everyone on board (except your fellow Imposters)\nYou must kill everyone before the Crewmates finish all of their tasks.\nYou will be able to move from room to room killing crewmates. \nBut be careful, if you kill a player and another player catches you, you lose!\nGood luck!!""")
        else:
            print("""Your goal is to finish all of your tasks without getting killed!\nThere are imposters onboard the ship but you don't know who they are!\nYou will be able to move from room to room completing your tasks. \nGood luck!""")
        time.sleep(5)
        print('-'*50)

        print("""Now - decide which room to enter first!""")
    
    # This method is called for the main character to do an action 
    # depending on their role that action will either be task or kill
    def action(self):
        if self.main_character.role[0] == 0:
            self.main_character.main_kill(self.map1)
        else:
            self.main_character.invoke_task(self.map1)
    
    # This method is called for players that aren't the main character and only when they are imposters
    def other_player_action(self):
        for player in self.player_list:
            if player.role[0] == 0:
                player.kill(self.map1)
  
    # This method moves players (main and others) throughout the map. 
    # The main character decides where they want to go but the other characters move at random. 
    def move_players(self):
    # Move players randomly consider moving this to a different part of the game
        for player in self.player_list:
            if player == self.main_character:
                count = 0
                current_room = player.locate_character(self.map1)
                rooms_to_move_to = self.map1.rooms_dict[current_room]
                for room in rooms_to_move_to:
                    print(f'{count} - {room.room_name}')
                    count +=1
                self.map1.mapimage.show()
                room_to_enter = 9
                while room_to_enter > len(rooms_to_move_to):
                    room_to_enter = int(input("Which room would you like to enter? (please enter the numeric value of the room)"))
                player.enter_room(rooms_to_move_to[room_to_enter], self.map1)
            if player != self.main_character and player.status != 'Dead':
                current_room = player.locate_character(self.map1)
                rooms_to_move_to = self.map1.rooms_dict[current_room]
                room_to_enter = random.randrange(0,len(rooms_to_move_to) - 1)
                player.enter_room(rooms_to_move_to[room_to_enter], self.map1)

    # This method is important in checking whether the game needs to end or not so it has to be called after every action
    # This is where we determine if a player has been killed and if they have we remove them from the player list
    # For the main character there are a few different print statements depending on when they got killed

    def check_casualties(self):
        # Checking for non main character deaths
        for player in self.player_list:
            if player.status == 'Dead' and player != self.main_character:
                self.player_list.remove(player)
        
        # Determining how many crewmates are still alive (if they're all dead the game ends)
        count = 0
        remaining_crew = []
        for player in self.player_list:
            if player.role[0] == 1:
                remaining_crew.append(player)
        
        # If the main character is dead and their role was crewmate they've died by an imposter in the same room
        if self.main_character.status == 'Dead' and self.main_character.role[0] == 1:
            os.system('clear')
            print('OHHHHHH NOOOOOOOOOOOO!') 
            time.sleep(2)
            print('You were distracted doing your task and you were killed by an imposter!!!!')
            time.sleep(2)
            cprint(figlet_format('Mission Failure!', font='larry3d'), 'red', attrs=['bold'])
            count = 9
            return count 
        
        # If the main character is dead and their role was imposter they were caught killing another player
        elif self.main_character.status == 'Dead' and self.main_character.role[0] == 0:
            os.system('clear')
            print('OHHHHHH NOOOOOOOOOOOO!')
            time.sleep(2)
            print('You got caught... ')
            time.sleep(2)
            cprint(figlet_format('Mission Failure!', font='larry3d'), 'red', attrs=['bold'])
            count = 9
            return count 
        # If the main character is alive and their role was imposter and no crewmates are alive then they have won    
        elif len(remaining_crew) == 0 and self.main_character.role[0] == 0:
            os.system('clear')
            cprint(figlet_format('Congrats!', font='larry3d'), 'green', attrs=['bold'])
            time.sleep(2)
            print('You killed all of the crew mates onboard before they finished their tasks!!!!')
            time.sleep(2)
            print('MISSION ACCOMPLISHED - EVERYONE IS DEAD!!!!')
            count = 9
            return count  
            
        # If the main character is alive and their role was crewmate and they've finished all their tasks then they've won
        elif self.main_character.role[0] == 1 and len(self.map1.room_task_dict) == 0:
            os.system('clear')
            cprint(figlet_format('Congrats!', font='larry3d'), 'green', attrs=['bold'])
            time.sleep(2)
            print('You finished all your tasks without getting killed by an imposter!!!!')
            time.sleep(2)
            print('MISSION ACCOMPLISHED - YOU WON AND BEAT ALL THE IMPOSTERS ABOARD !!!!')
            count = 9
            return count



# Initiating GamePlay class which begins the game
game1 = GamePlay()
# Call opening method from game1 which intros the game and initiatives various classes
game1.opening()

# This loop will run until the status is changed to 9 this status changes in the check_casualties method
# This status indicates that something has happened to the main character and the game should end
status = 0
while status != 9:
    status = game1.check_casualties()
    game1.move_players()
    game1.action()
    status = game1.check_casualties()
    if status != 9:
        game1.other_player_action()
        status = game1.check_casualties()
