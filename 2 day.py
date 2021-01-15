# -*- coding: utf-8 -*-
"""
Created on Thu May 15 17:22:45 2019

@author: mobina
"""

a = 4
b = 6
c = 2.5
print(a + b)
print(b / a)
print(b // a)  # floor division
print(b - a)
print(b * c)
print(b ** a)  # power
print(b % c)  # modulus
a += 5  # a = a + 5
print(a)
a -= 2  # a = a - 2
print(a)



import random

a = random.random()
print(a)

random.seed(37)  # Fixed random numbers

print(random.random())
print(random.random())
print(random.random())
print(random.random())

random.seed(80)  # Fixed random numbers

print(random.random())
print(random.random())
print(random.random())
print(random.random())



print(1 + int( 6 * random.random() ))
print(random.randrange(1, 7))
print(random.randrange(40, 70))



letter = 'adsghkjofrji'
print(random.choice(letter))

fruits = ['kiwi', 'die bime', 'die himbeere', 'der pfirsich', 'die melonen', 'die flaume']

print(random.choice(fruits))



# Fixing the previous code
import random

x = random.random()
print(x)

from random import random

x = random()
print(x)



import random

x = random.randrange(1, 21)


user_input = input('Please enter your guess: ')
print(user_input)

guess = int(user_input)

if guess == x:
    print('hit!')
elif guess > x:
    print('the hiden values is ', x, ',  your guess is too high!')
else:
    print('the hiden values is ', x, ', your guess is too low!')
    



fruits = ['kiwi', 'bime', 'himbeere', 'pfirsich', 'melonen', 'flaume']
salad = random.sample(fruits, 3)
print(salad)


# barresi inke x  is boolean or not, if joze un mavaredi bashe ke boolean
# mahsub mishan reterun true dar gher in surat false
x = 0
if x:
    print('true')
else:
    print("false")



values = ['', (), {}, [], 5, True, False]

for v in values:
    if v:
        print('is true:', v)
    else:
        print('is false:', v)

'''is false: 
is false: ()
is false: {}
is false: []
is true: 5
is true: True
is false: False'''


# strings

DS = 'data science is cool!'

DS1 = 'data ''science is cool!'
print(DS1)

h = 'hi '
len(h)

title = 'we have some title'
print(title)
print('_'*len(title))


x = 'xYsZee'
print(len(x))

y = x.upper()
print(y)

z = x.lower()
print(z)



title = 'we have some title'
print(title.find('have'))  # 3
print(title.find('title'))  # 13
print(title.rfind('title'))  # 13


if 'so' in title:
    print('found so')
else:
    print('NOT found so')










