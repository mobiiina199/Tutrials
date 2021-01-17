# -*- coding: utf-8 -*-
"""
Created on Thu May 16 19:09:56 2019

@author: mobina
"""
# for-in loop on strings

text = 'hello world'

for i in text:
    print(i)

# for-in loop on list

for fruit in ['weintrauben', 'grapefruit', 'pflaume', 'zitrone', 'ananas']:
    print(fruit)

# for-in loop on range

for i in range(1, 10, 2):
    print(i)

for c in text:
    if c == ' ':
       break
    print(c)
    
for c in text:
    if c == ' ':
       continue
    print(c)    
    
# for in loop with break and continue

for c in text:
    if c == ' ':
       continue
    if c == 'r':
       break
    print(c)

import random
total = 5
while total < 50:
    print(total)
    total += random.randrange(20)


id_str = input('Type in ypur ID: ')
while len(id_str) != 9:
    id_str = input('Type in ypur ID: ')
    
print('your id is ' + id_str)

# a.find(str, start , end)
text = 'The black cat climbed the green tree.'
start = 0
while True:
    loc = text.find('c', start)
    if loc == -1:
        break
    print(loc)
    start = loc + 1
    
import random  

hidden = random.randrange(1, 20)

while True:
    user_input = input(' please enter your guess[x]: ')
    print(user_input)
    
    if user_input == 'x' :
        print('sad to see you leaving early')
        exit()
    guess = int(user_input)
    
    if guess == hidden :
        print('hit!')
        break
    
    if guess < hidden :
        print('your guess is smaller')
    else:
        print('your guess is bigger')



        

