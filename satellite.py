import pgzrun
from random import randint

WIDTH = 1000
HEIGHT = 800

satellite = Actor("satellite")

def draw():
  screen.blit("space",(0,0))
  satellite.draw()

pgzrun.go()