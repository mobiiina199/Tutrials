# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 05:46:50 2021

@author: Lenovo
"""

txt = 'data science is cool!'
for c in txt:
    print(c)

for c in range(3, 10):
    print(c)

for c in txt:
    if c == ' ':
        
        break
    print(c)



for c in txt:
    if c == ' ':
        continue
    print(c)



import random

total = 0
while total <= 100:
    print(total)
    total += random.randrange(20)

print('Done')



total = 0 
while (total < 10000000) and (total % 17 != 1) and (total ** 2):
    print(total)
    total += random.randrange(20)

print('done')



total = 0
while total < 10000000:
    print(total)
    total += random.randrange(20)
    
    if total % 17 == 1:
        break
    if total ** 2 % 23 == 7:
        break
print('done')



id_str = input('type in your ID: ')

while len(id_str) != 9:
    id_str = input('type in your ID: ')

print('your ID is ' + id_str)



while True:
    id_str = input('type in your ID: ')
    if len(id_str) == 9:
        break
    
print('your ID is ' + id_str)


id_str = input('type in your ID: ')

while len(id_str) <= 9:
    id_str = input('type in your ID: ')

print('your ID is ' + id_str)



while True:
    answer = input('what is the meaning of life?')
    if answer == '42':
        print('yeah, that is it!')
        break
    

while True:
    line = get_next_line()
    
    if last_line:
        break
    
    if last_is_empty:
       continue
    
    if line_has_an_hash_at_the_beining: # #
       continue

    if line_has_two_slashes_at_the_beginning: # //
       continue

    do_the_real_stuff


text = "The black cat climbed the green tree."
start = 0
while True:
    loc = text.find('b', start)
    if loc == -1:
        break
    print(loc)
    start = loc + 1
    


hidden = random.randrange(1, 201)
while True:
    user_input = input('please enter your guess[x]: ')
    print(user_input)
    
    if user_input == 'x':
        print('sad to see you leaving early')
        exit()
    
    guess = int(user_input)
    if guess == hidden:
       print('Hit')
       break()
       
    if guess < hidden:
        print('Your guess is too low')
    else:
        print('your guess is too high')



debug = False
while True:
    if debug:
        print('debug: ', hidden)
        
    user_input = input('please enter your guess[x|s|d]')
    print(user_input)
    
    if user_input == 'x':
        print('sad to see you leaving early')
        exit()
    
    if user_input == 'x':
        print('the hidden value is ', hidden)
        continue
    if user_input == 'd':
        debug = not debug
        continue
    
    guess = int(user_input)
    if guess == hidden:
        print('hit!')
        break
    
    if guess < hidden:
        print('your guess is too low')
    else:
        print('your guess is too high')