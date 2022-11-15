# -*- coding: utf-8 -*-
"""
Brandon Bihl
Ballon Fight
"""

import pgzrun
import pygame
import pgzero
import random
from pgzero.builtins import Actor
from random import randint

#Declare constants
FONT_COLOR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600

balloon = Actor("balloon.png")
balloon.pos = 400 , 300

bird = Actor("bird-up")
bird.pos = randint(800,1600) , randint(10,200)

house = Actor("house")
house.pos = randint(800,1600), randint(10,200)

tree = Actor("tree")
tree.pos = randint(800, 1600), 450

bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0
Lives = 0
Level = 0
scores = []

def update_high_scores():
    global score, scores
    filename = r"\\Mac\Home\Downloads\Python Games Resource Pack\Chapter 8 Balloon Flight\Game Files\high-scores.txt"
    scores = []
    with open(filename, "r") as file:
        line = file.readline()
        high_scores = line.split()
        for high_score in high_scores:
            if (score > int(high_score)):
                scores.append(str(score) + " ")
                score = int(high_score)
            else:
                scores.append(str(high_score) + " ")
    with open(filename, "w") as file:
        for high_score in scores:
            file.write(high_score)


def display_high_scores():
    screen.draw.text("HIGH SCORES", (350,150), color = "black")
    y = 175
    position = 1
    for high_score in scores:
        screen.draw.text(str(position) + ". " + high_score, (350,y) ,color="Black")
        y += 25
        position += 1
        



def draw():

  #  screen.clear()
    screen.blit("background", (0,0)) #add a background image to the game window
    if not game_over:
        balloon.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text("Score: " + str(score), (700,5), color="black")
        
    else:
        display_high_scores()
        
def on_mouse_down():
    global up
    up = True
    balloon.y -= 5
    
def on_mouse_up():
    global up
    up = False

def flap():
    global bird_up
    if bird_up:
        bird.image = "bird-down"
        bird_up = True

def update():
    global game_over, score, number_of_updates, Lives, Level
    
    if not game_over:
        if not up:
            balloon.y -= 4
            
        else:
            balloon.y += 3
            
        if bird.x > 0:
            if Level <1:
                bird.x -= 10
            elif Level <2:
                bird.x -= 15
            else:
                bird.x -= 25
                
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            score += 1
            number_of_updates = 0
            
        if house.right > 0:
            if Level <1:
                house.x -= 2
            elif Level <2:
                 house.x -= 4
            else:
                house.x -= 6
                
        else:
            house.x = randint(800,1600)
            score += 1
            
        if tree.right >0:
            if Level <1:
                tree.x -= 2
            else:
                tree.x -=4
        else:
            tree.x = randint(800,1600)
            score += 1
        if balloon.top < 0 or balloon.bottom > 560:
            game_over = True
            update_high_scores()
            
        if balloon.collidepoint(bird.x, bird.y) or \
            balloon.collidepoint(house.x, house.y) or \
            balloon.collidepoint(tree.x, tree.y):
            Lives += 1
            print(Lives)
            
        if Lives > 50 :
            game_over = True
            update_high_scores()
            
        if score > 10:
            Level = 1
            print(Level)
        
        if score > 30:
            Level = 2
        
            
pgzrun.go()