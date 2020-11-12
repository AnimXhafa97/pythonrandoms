# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 20:45:09 2020

@author: animx
"""


from graphics import *
import pygame, sys
import math
import numpy as np
from queue import PriorityQueue

#pygame.init()

# #set the screen size and captions
size = (500, 500)
rows = 50
margin = 1
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("A* Pathfinding")
# screen.fill((173, 172, 166))

#define colors
aqua = (0, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 128, 0)
red = (255, 0, 0)
white = (255, 255, 255)
purple = (128, 0, 128)

#initialize PriorityQueue
q = PriorityQueue()

#define the empty board
#board = [[0 for x in range(rows)] for y in range(rows)]


#define all possible states of each node
class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = white
        self.width = width
        self.neighbors = []
        #self.total_rows = total_rows
    
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == red
    
    def is_open(self):
        return self.color == aqua
    
    def is_barrier(self):
        return self.color == black
    
    def is_start(self):
        return self.color == green
    
    def is_end(self):
        return self.color == blue
    
    def reset(self):
        return self.color == white
    
    def close(self):
        self.color = red
    
    def open_node(self):
        self.color = green
    
    def barrier(self):
        self.color = black
    
    def start(self):
        self.color = aqua
    
    def end(self):
        self.color = blue
        
    def path(self):
        self.color = purple
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
    
    def update_neighbors(self, grid):
        pass
    
    def __lt__(self, other):
        return False
    


def init_grid():
    board = []
    for i in range(rows):
        board.append([])
        for j in range(rows):
            node = Node(i, j, size[0]/rows)
            board[i].append(node)
    return board


#heuristic
def h(c, end):
    x1, y1 = c
    x2, y2 = end
    return abs(x1 - x2) + abs(y1 - y2)


#distance between current node and start node
def g(c, start):
    x1, y1 = start
    x2, y2 = c
    return abs(x1 - x2) + abs(y1 - y2)





def get_neighbors(node):
    c = Node(node[1], node[0], size[0]/rows)
    neighbors = c.neighbors
    neighbors.extend([(c.col-1, c.row+1), (c.col, c.row+1), (c.col+1, c.row+1), (c.col-1, c.row), (c.col+1, c.row), (c.col-1, c.row-1), (c.col, c.row-1), (c.col+1, c.row-1)])
    return neighbors

#get_neighbors((34, 16))

#in case the massive priorityqueue becomes an issue
def play():
    pass


start = (5,5)
current = start
goal = (3, 8)

while current != goal:
    print("Current: " + str(current))
    neighbors = get_neighbors(current)
    # print("Start" + str(start))
    # print("Current 1 " + str(current))
    for i in range(len(neighbors)):
        current = neighbors[i]
        f = g(current, start) + h(current, goal)
        q.put((f, neighbors[i]))
    print(q.queue)
    #print(neighbors)
    current = q.get()[1]
    if current == goal:
        print("WE DID IT!")
        print("Current: " + str(current))
    q.queue.clear()
    print(q.queue)

board = init_grid()

# =============================================================================
# #main game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         
#         #this code should be expanded for the weights functionality
#         elif event.type == pygame.MOUSEBUTTONDOWN and pygame.MOUSEMOTION:
#             pos = pygame.mouse.get_pos()
#             y_pos = int(pos[0] // (board[0][0].width + margin))
#             x_pos = int(pos[1] // (board[0][0].width + margin))
#             board[x_pos][y_pos] = 1
#     
#     
#     
#     #draw the grid
#     for i in range(rows):
#         for j in range(rows):
#             color = white
#             if board[i][j] == 1:
#                 color = red
#             pygame.draw.rect(screen, color, [j*(board[0][0].width + margin), i*(board[0][0].width + margin), board[0][0].width, board[0][0].width])
#     
#     #evaluating the nodes with arbitrary start and goal
# 
#     pygame.display.flip()
#         
# pygame.quit()
# =============================================================================
