#!/usr/bin/env python 
import random, math
random.seed()
x = math.floor(random.random()*100)+1
z = 0
b = 0
while x != z:
   b=b+1
   z = input("Guess my number: ")
   if z < x: print("Higher!")
   if z > x: print("Lower!")
   if z == x + 1 or z == x - 1  : print("You are very close!")
print("Correct! " + str(b) + " tries =)")
