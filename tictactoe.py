#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 14:29:31 2020

@author: animxhafa
"""

import copy
import tkinter
from tkinter import *


key = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

new_board = copy.deepcopy(board)

corners = [0,2,6,8]
centers = [1,3,4,5,7]

positions = {
        
        "X" : [],
        "O" : [],
        
        }

    
win = {
       
       "1": [0,1,2],
       "2": [3,4,5],
       "3": [6,7,8],
       
       "4": [0,4,8],
       "5": [2,4,6],
       
       "6": [0,3,6],
       "7": [1,4,7],
       "8": [2,5,8],
       
       
       }



def showKey():
    print(key[0:3])
    print(key[3:6])
    print(key[6:9])

def drawBoard():
    print("Enter X or O at the board position given by the following key: ")
    print("Ex. Enter '0' to place X or O at the top-left corner of the board. \n")
    print("KEY: \n")
    
    showKey()
    print("\n"*2)
    
    print("BOARD: \n")
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

#drawBoard()
    



def drawNew():
    print(new_board[0:3])
    print(new_board[3:6])
    print(new_board[6:9])


def playerMove(letter):
     ''' Allows players to put either an X or an O onto the board at an open position'''
     print(str(letter) + " is playing:")
     pos = int(input("Position: "))
     if pos > 8:
         print("Please choose a position between 0 and 8. ")
         drawNew()
         playerMove(letter)
         
    ##this is the code that actually inputs a letter
     if new_board[pos] == ' ':
         new_board[pos] = letter
         positions[letter].append(pos)
     ##    
         
     elif new_board[pos] != ' ':
         print("That space is already taken, try again. \n")
         drawNew()
         playerMove(letter)
     print("\n"*3)


def checkWinner(bo, letter):
    '''New and improved way of checking for winner without the extra positions dictionary.
    Note that this does not yet have a draw condition in it.'''
    if bo[0] == letter and bo[1] == letter and bo[2] == letter:
        return True
    if bo[3] == letter and bo[4] == letter and bo[5] == letter:
        return True
    if bo[6] == letter and bo[7] == letter and bo[8] == letter:
        return True
    
    #diagonals
    if bo[0] == letter and bo[4] == letter and bo[8] == letter:
        return True
    if bo[2] == letter and bo[4] == letter and bo[6] == letter:
        return True
    
    #verticals
    if bo[0] == letter and bo[3] == letter and bo[6] == letter:
        return True
    if bo[1] == letter and bo[4] == letter and bo[7] == letter:
        return True
    if bo[2] == letter and bo[5] == letter and bo[8] == letter:
        return True
    else:
        return False
    

def compMove1(letter):
    '''If the AI sees a move that is going to win the game in one go, it makes that move'''
    
    testboard = new_board.copy()
    for i in range(len(testboard)):
        if testboard[i] == ' ':
            testboard[i] = letter
            checkWinner(testboard, letter)
            if checkWinner(testboard, letter) == True:
                new_board[i] = letter
                drawNew()
                return True
                break
            else:
                testboard = new_board.copy()

    
        
def compMove2(p, letter):
    ''' If the player has a winning move, block that move.'''
    
    testboard = new_board.copy()
    
    for i in range(len(testboard)):
        if testboard[i] == ' ':
            testboard[i] = p
            checkWinner(testboard, p)
            
            if checkWinner(testboard, p) == True:
                new_board[i] = letter
                break
            else:
                testboard = new_board.copy() 


def compMove3(bo, letter):
    ''' If the corners are available, take one of the corners'''
    
    for i in corners:
        if bo[i] == ' ':
            bo[i] = letter
            return True
            break



def compMove4(bo, letter):
    ''' If the center is available, take the center'''
    
    for i in centers:
        if bo[i] == ' ':
            bo[i] = letter
            return True
            break

        

def compMove5(bo, letter):
    ''' If the other moves are not available, make any available move'''
    
    for i in range(len(bo)):
        if bo[i] == ' ':
            bo[i] = letter
            return True
            break

# =============================================================================
# def compMove(letter, p, bo):
#     move = 0
#     
#     compMove1(letter)    
#     if compMove1(letter) == True:
#         return move
#     
#     compMove2(p, letter)
#     if compMove2(p, letter) == True:
#         return move
#     
#     compMove3(bo, letter)
#     if compMove3(bo, letter) == True:
#         
#         return move
#     
#     compMove4(bo, letter)
#     if compMove4(bo, letter) == True:
#         compMove4(bo, letter)
#         return move
#     
#     compMove5(bo, letter)
#     if compMove5(bo, letter) == True:
#         
#         return move 
#     
#     
# =============================================================================
        
def compMove(letter, p, bo):
    ''' Links all the computer moves together into one function that executes 
        linearly'''
    #move = 0
    
    #take the winning move
    testboard = new_board.copy()
    for i in range(len(testboard)):
        if testboard[i] == ' ':
            testboard[i] = letter
            checkWinner(testboard, letter)
            if checkWinner(testboard, letter) == True:
                new_board[i] = letter
                return True
            else:
                testboard = new_board.copy()
    
    #blocks an opponents winning move
    for i in range(len(testboard)):
        if testboard[i] == ' ':
            testboard[i] = p
            checkWinner(testboard, p)
            
            if checkWinner(testboard, p) == True:
                new_board[i] = letter
                return True
            else:
                testboard = new_board.copy()
    
    #takes first available corner
    for i in corners:
        if bo[i] == ' ':
            bo[i] = letter
            return True
     
    #takes first available center position
    for i in centers:
        if bo[i] == ' ':
            bo[i] = letter
            return True
    
    #makes first available legal move
    for i in range(len(bo)):
        if bo[i] == ' ':
            bo[i] = letter
            return True

def playGame():
    showKey()
    print("\n"*2)
    drawNew()
    
    playerMove('X')
    compMove('O', 'X', new_board)
    
    drawNew()
    
    while checkWinner(new_board, 'X') != True:
        playerMove('X')
        
        if checkWinner(new_board, 'X') == True:
            drawNew()
            print('X wins!')
            break
        
        compMove('O', 'X', new_board)
        if checkWinner(new_board, 'O') == True:
            drawNew()
            print('O wins!')
            break
        drawNew()
        

playGame()

            
            

# =============================================================================
# Bugs:
#     Computer cheats and makes multiple moves in one go.
#     Player and computer moves do not alternate
#     The player cannot choose to play against another player or against the comp:
#         Easy fix
    # Game does not handle draws
# =============================================================================
        
        
    


    
    
    
    
    
    
    
    
    
    
