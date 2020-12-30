
from  random import shuffle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from State import State

initial_state = [0, 0, 0, 0, 0, 0, 0, 0]

def hill_climbing(initial_state):
    current_state = State(initial_state)
    
    while True:
        best_neighbor = current_state.neighbor()

        if best_neighbor.evaluation() >= current_state.evaluation():
            return current_state.state
        current_state = best_neighbor
    return current_state

def random_restart(initial_state):
    state = State(initial_state)
    count = 0
    while State(initial_state).evaluation() > 0 & count < 15:
        shuffle(initial_state)
        state = hill_climbing(initial_state)
        count += 1
    return state

#board graphic based on the solution
def board(solution): 
    matrix = np.zeros([8,8], dtype=int)
    matrix = matrix.tolist()
    for item in solution:
        for i in range(len(solution)):
            if i == item:
                for j in range(len(solution)):
                    if  j == solution.index(item):
                        matrix[i][j] = 1
                        
    l =[]
    for i in range(1, len(solution)+1):
        l.append(i)
    
    plt.figure(figsize=(5,5))
    sns.heatmap(matrix, linewidths=.8,cbar=False,cmap='Set3',xticklabels=l,yticklabels=l)
    


