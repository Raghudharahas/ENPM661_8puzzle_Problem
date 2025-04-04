import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pygame
import time


class Node:
    def __init__(self, state, index, parent_index):
        self.Node_State_i = np.array(state)  # 3x3 NumPy array representing the state
        self.Node_Index_i = index  # Unique index for the node
        self.Parent_Node_Index_i = parent_index  # Parent node index

def find_blank_tile(state):
    i, j = np.where(state == 0)
    return int(i[0]), int(j[0])

# Move functions
def ActionMoveLeft(CurrentNode):
    i, j = find_blank_tile(CurrentNode.Node_State_i)
    if j > 0:
        new_state = CurrentNode.Node_State_i.copy()
        new_state[i, j], new_state[i, j - 1] = new_state[i, j - 1], new_state[i, j]
        return True, new_state
    return False, None

def ActionMoveRight(CurrentNode):
    i, j = find_blank_tile(CurrentNode.Node_State_i)
    if j < 2:
        new_state = CurrentNode.Node_State_i.copy()
        new_state[i, j], new_state[i, j + 1] = new_state[i, j + 1], new_state[i, j]
        return True, new_state
    return False, None

def ActionMoveUp(CurrentNode):
    i, j = find_blank_tile(CurrentNode.Node_State_i)
    if i > 0:
        new_state = CurrentNode.Node_State_i.copy()
        new_state[i, j], new_state[i - 1, j] = new_state[i - 1, j], new_state[i, j]
        return True, new_state
    return False, None

def ActionMoveDown(CurrentNode):
    i, j = find_blank_tile(CurrentNode.Node_State_i)
    if i < 2:
        new_state = CurrentNode.Node_State_i.copy()
        new_state[i, j], new_state[i + 1, j] = new_state[i + 1, j], new_state[i, j]
        return True, new_state
    return False, None

def bfs_solver(initial_state, goal_state):
    queue = [Node(np.array(initial_state), 0, -1)]
    visited = set()
    explored_nodes = []
    index = 0
    
    while queue:
        current_node = queue.pop(0)
        explored_nodes.append(current_node)
        
        if np.array_equal(current_node.Node_State_i, goal_state):
            return current_node, explored_nodes
        
        visited.add(tuple(map(tuple, current_node.Node_State_i)))
        
        for move_func in [ActionMoveLeft, ActionMoveRight, ActionMoveUp, ActionMoveDown]:
            status, new_state = move_func(current_node)
            if status and tuple(map(tuple, new_state)) not in visited:
                index += 1
                queue.append(Node(new_state, index, current_node.Node_Index_i))
    
    return None, explored_nodes

def generate_path(goal_node, explored_nodes):
    path = []
    current = goal_node
    while current.Parent_Node_Index_i != -1:
        path.append(current)
        current = next(node for node in explored_nodes if node.Node_Index_i == current.Parent_Node_Index_i)
    path.reverse()
    return path

def write_output(explored_nodes, solution_path):
    with open("Nodes.txt", "w") as f:
        for node in explored_nodes:
            for row in node.Node_State_i:
                f.write(" ".join(map(str, row)) + "\n")
            f.write("\n")
    
    with open("NodesInfo.txt", "w") as f:
        for node in explored_nodes:
            f.write(f"{node.Node_Index_i} {node.Parent_Node_Index_i} {node.Node_State_i.tolist()}\n")
    
    with open("nodePath.txt", "w") as f:
        for node in solution_path:
            for row in node.Node_State_i:
                f.write(" ".join(map(str, row)) + "\n")
            f.write("\n")

initial_state = [[4, 1, 3], [7, 2, 5], [0, 8, 6]]
print("Initial State:")
print(np.array(initial_state))
goal_state = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
print("Goal State:")
print(goal_state)
print() 

goal_node, explored_nodes = bfs_solver(initial_state, goal_state)
if goal_node:
    solution_path = generate_path(goal_node, explored_nodes)
    write_output(explored_nodes, solution_path)
    print("Solution found! Output files generated.")
else:
    print("No solution found.")
