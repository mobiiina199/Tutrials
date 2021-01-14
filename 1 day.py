# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:54:45 2019

@author: mobina
"""

#1Daysofpythonchallenge

"hello".format()
#'hello'
"hello, {}".format("mobina")
#'hello, mobina'
"{} {} {}".format("hello","dear","mobina")
#'hello dear mobina'
"{1} {2} {0}".format("hello","dear","mobina")
#'dear mobina hello'
"user not found for username {username}".format(username="shima")
#'user not found for username shima'
"{{{}}}".format("mobina")
#'{mobina}'
example_dict={
    "name":"mobina",
    "age":"old",
    "height": "tall"}
"{0[name]}".format(example_dict)
#'mobina'
"{d[name]}".format(d=example_dict)
#'mobina'
"Dict: {d[name]}, {d[age]}, {d[height]}".format(d=example_dict)
#'Dict: mobina, old, tall'

def main():
    a = input('first number: ')
    b = input('second number: ')
    print(int(a) + int(b))

main()


#How can I check if a string can be converted to a number?
num = input('Type in a number:')
print(num)
print(num.isdecimal())
print(num.isnumeric())

if num.isdecimal():
    num = int(num)
    print(num)
    
    
#Converting str to int
a = '56'
print(a)
print(type(a))#<class 'str'>
b = int(a)
print(type(b))#<class 'int'>



#Converting float to int
a = 2.1
print(type(a))
b = int(a)
print(type(b))

print( int(float(2.1)) )
print( int(str(2)) )
print( int(float(2)) )



def main():
    expected_answer = '42'
    inp = input('Enter your answer:')
    
    if expected_answer == inp:
        print('welcome!')

main()


def main():
    a = input('First number: ')
    b = input('second number: ')
    
    if int(b) == 0:
        print('can not divide by 0')
    else:
        print('Divide', a, 'by', b)
        print( int(a) / int(b) )

main()



def main():
    a = input('First number: ')
    b = input('second number: ')
    
    if int(b) == int(a):
        print('they are equal.')
    elif int(a) < int(b):
        print(a + ' is smaller than ' + b)
    else:  
        print(a + ' is bigger than ' + b)

main()



def main():
    a = float(input('Number: '))
    b = float(input('Number: '))
    op = input('operator (+, -, /, *): ')
    
    if op == '+':
        res = a+b
    elif op == '-':
        res = a-b
    elif op == '/':
        res = a/b
    else:
        res = a*b
        return
    
    print(res)
    return
    
main()




def main():
    a = input('Number: ')
    b = input('Number: ')
    op = input('operator (+, -, /, *): ')
    
    command = a + op + b
    print(command)
    res = eval(command)
    print(res)

main()