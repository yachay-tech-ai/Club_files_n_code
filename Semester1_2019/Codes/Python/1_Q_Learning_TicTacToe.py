# -*- coding: utf-8 -*-
#Importing the libraries

from random import randint, uniform
from sklearn.externals import joblib
from copy import deepcopy
import numpy as np


#Creating the environment
class TicTacToe:
    def __init__(self, player1="X", player2="O"):
        self.player1 = player1
        self.player2 = player2
        self.board = None
        self.actions = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    
    def initGame(self):
        self.board = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(' ')
            self.board.append(row)
    
    def printBoard(self):
        empty_board = "      ___ ___ ___\n     |   |   |   |\n     | 0 | 1 | 2 |\n  ___|___|___|___|\n |   |   |   |   |\n | 0 |   |   |   |\n |___|___|___|___|\n |   |   |   |   |\n | 1 |   |   |   |\n |___|___|___|___|\n |   |   |   |   |\n | 2 |   |   |   |\n |___|___|___|___|\n"
        '''   ___ ___ ___
             |   |   |   |
             | 0 | 1 | 2 |
          ___|___|___|___|
         |   |   |   |   |
         | 0 | a | b | c |
         |___|___|___|___|
         |   |   |   |   |
         | 1 | d | e | f |
         |___|___|___|___|
         |   |   |   |   |
         | 2 | g | h | i |
         |___|___|___|___|'''
        a = self.board[0][0] 
        b = self.board[0][1] 
        c = self.board[0][2] 
        d = self.board[1][0] 
        e = self.board[1][1] 
        f = self.board[1][2] 
        g = self.board[2][0] 
        h = self.board[2][1] 
        i = self.board[2][2] 
        current_board = empty_board[0:101] + a + empty_board[102:105] + b + empty_board[106:109] + c + empty_board[110:158] + d + empty_board[159:162] + e + empty_board[163:166] + f + empty_board[167:215] + g + empty_board[216:219] + h + empty_board[220:223] + i + empty_board[224:]
        print(current_board)
        print("-"*30)

    def checkWin(self, player):
        mark = 'X' if player==1 else 'O'
        for i in range(3):
            if (self.board[i][0]==mark and self.board[i][1]==mark and self.board[i][2]==mark):
                return True
            if (self.board[0][i]==mark and self.board[1][i]==mark and self.board[2][i]==mark):
                return True
        if (self.board[0][0] == mark and self.board[1][1]==mark and self.board[2][2]==mark):
            return True
        if (self.board[2][0] == mark and self.board[1][1]==mark and self.board[0][2]==mark):
            return True
        return False

    def checkEqual(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        else:
            return True

    def getPossibleActions(self):
        possible_actions = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    possible_actions .append((i,j))
        return possible_actions 

    def getAction(self):
        possible_actions = self.getPossibleActions()
        action = possible_actions[randint(0,len(possible_actions)-1)]
        return action

    def calculateReward(self, player, player_training):
        if self.checkWin(player):
            if player_training == 1:
                if player == 1:
                    return 20, True
                else:
                    return -10, True
            else:
                if player == 2:
                    return 20, True
                else:
                    return -10, True
        elif self.checkEqual():
            return -10, True
        else:
            return -1, False
    
    def play(self, action, player, player_training):
        self.board[action[0]][action[1]] = 'X' if player == 1 else 'O'
        return self.calculateReward(player, player_training)

    def playRandom(self, player, player_training):
        action = self.getAction()
        self.board[action[0]][action[1]] = 'X' if player == 1 else 'O'
        return self.calculateReward(player, player_training)

    def verifyAction(self, action):
        possible_actions = self.getPossibleActions()
        if action in possible_actions:
            return True
        return False
        
    def playHuman(self, player):
        while True:
            action = input("Input the action: ")
            try:
                action = action.split(",")
            except:
                print("The action needs to be two numbers between 0-2. Ex: 0,1. Try again")
            try:    
                action[0] = int(action[0])
                action[1] = int(action[1])
                action = tuple(action)
                if self.verifyAction(action):
                    break
                else:
                    print("The action needs to be two numbers between 0-2. Ex: 0,1. Try again")
            except:
                print("The action needs to be two numbers between 0-2. Ex: 0,1. Try again")
        return self.play(action, player, 1)
    
    def initRealGame(self):
        self.player1 = "Q-Learning Agent"
        self.player2 = input("Input the name of the player: ")
        q_table_player1 = joblib.load("q_table_player1.sav")
        states_player1 = joblib.load("states_player1.sav")
        self.initGame()
        self.printBoard()
        _ = input(f"Press enter to start the game and good luck {self.player2} ;)")
        while True:
            possible_actions = self.getPossibleActions()
            index_state = states_player1.index(self.board)
            probabilities_possible_actions = []
            indexes_possible_actions = []
            for action in possible_actions:
                action_index = self.actions.index(action)
                probabilities_possible_actions.append(q_table_player1[index_state][action_index])
                indexes_possible_actions.append(action_index)
            max_prob = max(probabilities_possible_actions)
            index_max_prob = indexes_possible_actions[probabilities_possible_actions.index(max_prob)]
            action = self.actions[index_max_prob]
        
            reward_player1, end_game = self.play(action, 1, 1)  
            self.printBoard()
            if end_game:
                if reward_player1 == 20:
                    print(f"{env.player1} wins!")
                if reward_player1 == -10:
                    print("Tie")
                break
            
            _ , end_game = self.playHuman(2)
            self.printBoard()
            if end_game:
                print(f"{env.player2} wins!")
                break
            
            
#Defining the parametersalpha = 0.1
alpha = 0.1
gamma = 0.6
threshold = 0.1
env = TicTacToe()


#Training player 1 
states_player1 = []
q_table_player1 = []
for i in range(1,1000001):
    env.initGame()
    while True:
        if env.board not in states_player1:
            states_player1.append(deepcopy(env.board))
            q_table_player1.append([0,0,0,0,0,0,0,0,0])
            action = env.getAction() 
            max_prob = 0
            index_state = -1
            index_max_prob = env.actions.index(action)
        else:   
            index_state = states_player1.index(env.board)
            if uniform(0, 1) < threshold:
                action = env.getAction()
                index_max_prob = env.actions.index(action)
                max_prob = q_table_player1[index_state][index_max_prob]
            else:
                possible_actions = env.getPossibleActions()
                probabilities_possible_actions = []
                indexes_possible_actions = []
                for action in possible_actions:
                    action_index = env.actions.index(action)
                    probabilities_possible_actions.append(q_table_player1[index_state][action_index])
                    indexes_possible_actions.append(action_index)
                max_prob = max(probabilities_possible_actions)
                index_max_prob = indexes_possible_actions[probabilities_possible_actions.index(max_prob)]
                action = env.actions[index_max_prob]

        reward_player1, end_game = env.play(action, 1, 1)  
                
        if end_game:   
            old_value = max_prob
            next_max = 0
            new_value = (1 - alpha) * old_value + alpha * (reward_player1 + gamma * next_max)
            q_table_player1[index_state][index_max_prob] = new_value
            break
        
        reward_player2, end_game = env.playRandom(2, 1)
        
        if env.board not in states_player1:
            states_player1.append(deepcopy(env.board))
            q_table_player1.append([0,0,0,0,0,0,0,0,0])
                
        total_reward = reward_player1 + reward_player2
        old_value = max_prob
        index_next_state = states_player1.index(env.board)
        next_max = max(q_table_player1[index_next_state])
        new_value = (1 - alpha) * old_value + alpha * (total_reward + gamma * next_max)
        q_table_player1[index_state][index_max_prob] = new_value

        if end_game:
            break

    if i % 100000 == 0:
        print(f"Episode: {i}")
print("Training finished.\n")
joblib.dump(q_table_player1, 'q_table_player1.sav')
joblib.dump(states_player1, 'states_player1.sav')


#Training player 2
states_player2 = []
q_table_player2 = []
for i in range(1,1000001):
    env.initGame()
    reward_player1, end_game = env.playRandom(1, 2)
    if env.board not in states_player2:
        states_player2.append(deepcopy(env.board))
        q_table_player2.append([0,0,0,0,0,0,0,0,0])
    while True:
        index_state = states_player2.index(env.board)
        if uniform(0, 1) < threshold:
            action = env.getAction()
            index_max_prob = env.actions.index(action)
            max_prob = q_table_player2[index_state][index_max_prob]
        else:
            possible_actions = env.getPossibleActions()
            probabilities_possible_actions = []
            indexes_possible_actions = []
            for action in possible_actions:
                action_index = env.actions.index(action)
                probabilities_possible_actions.append(q_table_player2[index_state][action_index])
                indexes_possible_actions.append(action_index)
            max_prob = max(probabilities_possible_actions)
            index_max_prob = indexes_possible_actions[probabilities_possible_actions.index(max_prob)]
            action = env.actions[index_max_prob]
           
        reward_player2, end_game = env.play(action, 2, 2)
        if end_game:
            old_value = max_prob
            next_max = 0
            new_value = (1 - alpha) * old_value + alpha * (reward_player2 + gamma * next_max)
            q_table_player2[index_state][index_max_prob] = new_value
            break
        
        reward_player1, end_game = env.playRandom(1, 2)
        
        if env.board not in states_player2:  
            states_player2.append(deepcopy(env.board))
            q_table_player2.append([0,0,0,0,0,0,0,0,0])
        
        total_reward = reward_player1 + reward_player2
        old_value = max_prob
        index_next_state = states_player2.index(env.board)
        next_max = max(q_table_player2[index_next_state])
        
        new_value = (1 - alpha) * old_value + alpha * (total_reward + gamma * next_max)
        q_table_player2[index_state][index_max_prob] = new_value

        if end_game:
            break
        
    if i % 100000 == 0:
        print(f"Episode: {i}")
print("Training finished.\n")
joblib.dump(q_table_player2, 'q_table_player2.sav')
joblib.dump(states_player2, 'states_player2.sav')   


#Evaluating the performance of a random player
total_wins = []
total_ties = []
total_losses = []
q_table_player2 = joblib.load("q_table_player2.sav")
states_player2 = joblib.load("states_player2.sav")
threshold = 0.5
for _ in range(1000):
    wins, ties, losses = 0, 0, 0
    games = 100
    for _ in range(games):
        env.initGame()
        while True:
            reward_player1, end_game = env.playRandom(1, 1) 
            if end_game:
                if reward_player1 == 20:
                    wins += 1
                if reward_player1 == -10:
                    ties += 1
                break     
            
            if uniform(0, 1) < threshold:
                action = env.getAction()
            else:
                possible_actions = env.getPossibleActions()
                index_state = states_player2.index(env.board)
                probabilities_possible_actions = []
                indexes_possible_actions = []
                for action in possible_actions:
                    action_index = env.actions.index(action)
                    probabilities_possible_actions.append(q_table_player2[index_state][action_index])
                    indexes_possible_actions.append(action_index)
                max_prob = max(probabilities_possible_actions)
                index_max_prob = indexes_possible_actions[probabilities_possible_actions.index(max_prob)]
                action = env.actions[index_max_prob]

            reward_player2, end_game = env.play(action, 2, 1)  
                    
            if end_game:
                losses += 1
                break
            
    total_wins.append(wins)
    total_ties.append(ties)
    total_losses.append(losses)

print("RESULTS RANDOM PLAYER")
print(f"Percentage of wins: {np.mean(total_wins)}%")
print(f"Pertentage of ties: {np.mean(total_ties)}%")
print(f"Percentage of losses: {np.mean(total_losses)}%")


#Evaluating the performance of a Q-Learning Player
total_wins = []
total_ties = []
total_losses = []
q_table_player1 = joblib.load("q_table_player1.sav")
states_player1 = joblib.load("states_player1.sav")
q_table_player2 = joblib.load("q_table_player2.sav")
states_player2 = joblib.load("states_player2.sav")
threshold = 0.5
for _ in range(1000): 
    wins, ties, losses = 0, 0, 0
    games = 100
    for _ in range(games):
        env.initGame()
        while True:
            possible_actions = env.getPossibleActions()
            index_state = states_player1.index(env.board)
            probabilities_possible_actions = []
            indexes_possible_actions = []
            for action in possible_actions:
                action_index = env.actions.index(action)
                probabilities_possible_actions.append(q_table_player1[index_state][action_index])
                indexes_possible_actions.append(action_index)
            max_prob = max(probabilities_possible_actions)
            index_max_prob = indexes_possible_actions[probabilities_possible_actions.index(max_prob)]
            action = env.actions[index_max_prob]
    
            reward_player1, end_game = env.play(action, 1, 1)  
    
            if end_game:
                if reward_player1 == 20:
                    wins += 1
                if reward_player1 == -10:
                    ties += 1
                break
            
            if uniform(0, 1) < threshold:
                action = env.getAction()
            else:
                possible_actions = env.getPossibleActions()
                index_state = states_player2.index(env.board)
                probabilities_possible_actions = []
                indexes_possible_actions = []
                for action in possible_actions:
                    action_index = env.actions.index(action)
                    probabilities_possible_actions.append(q_table_player2[index_state][action_index])
                    indexes_possible_actions.append(action_index)
                max_prob = max(probabilities_possible_actions)
                index_max_prob = indexes_possible_actions[probabilities_possible_actions.index(max_prob)]
                action = env.actions[index_max_prob]
            
            reward_player2, end_game = env.play(action, 2, 1)
            
            if end_game:
                losses += 1
                break
            
    total_wins.append(wins)
    total_ties.append(ties)
    total_losses.append(losses)

print("RESULTS Q-LEARNING PLAYER")
print(f"Percentage of wins: {np.mean(total_wins)}%")
print(f"Pertentage of ties: {np.mean(total_ties)}%")
print(f"Percentage of losses: {np.mean(total_losses)}%")


#Visualizing the results of Q-Learning
q_table_player1 = joblib.load("q_table_player1.sav")
states_player1 = joblib.load("states_player1.sav")
q_table_player2 = joblib.load("q_table_player2.sav")
states_player2 = joblib.load("states_player2.sav")
threshold = 0.1
env.initGame()
env.printBoard()
_ = input("Press enter to continue: ")
while True:
    possible_actions = env.getPossibleActions()
    index_state = states_player1.index(env.board)
    probabilities_possible_actions = []
    indexes_possible_actions = []
    for action in possible_actions:
        action_index = env.actions.index(action)
        probabilities_possible_actions.append(q_table_player1[index_state][action_index])
        indexes_possible_actions.append(action_index)
    max_prob = max(probabilities_possible_actions)
    index_max_prob = indexes_possible_actions[probabilities_possible_actions.index(max_prob)]
    action = env.actions[index_max_prob]

    reward_player1, end_game = env.play(action, 1, 1)  
    env.printBoard()
    _ = input("Press enter to continue: ")
    if end_game:
        if reward_player1 == 20:
            print(f"{env.player1} wins!")
        if reward_player1 == -10:
            print("Tie")
        break
    
    if uniform(0, 1) < threshold:
        action = env.getAction()
    else:
        possible_actions = env.getPossibleActions()
        index_state = states_player2.index(env.board)
        probabilities_possible_actions = []
        indexes_possible_actions = []
        for action in possible_actions:
            action_index = env.actions.index(action)
            probabilities_possible_actions.append(q_table_player2[index_state][action_index])
            indexes_possible_actions.append(action_index)
        max_prob = max(probabilities_possible_actions)
        index_max_prob = indexes_possible_actions[probabilities_possible_actions.index(max_prob)]
        action = env.actions[index_max_prob]
    
    reward_player2, end_game = env.play(action, 2, 1)
    env.printBoard()
    _ = input("Press enter to continue: ")
    
    if end_game:
        print(f"{env.player2} wins")
        

#Playing a Real Game
env.initRealGame()

