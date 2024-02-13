# # 'AAABBCCCCDDDEEF' => 'A3B2C4D3E2F1'
# import itertools
#
#
# def char_count(str1):
#     li = list(str1)
#     # print(li)
#     p = []
#     st = ''
#     for i in li:
#         if i not in p:
#             k = li.count(i)
#             # print(k)
#             p.append(i)
#             sr = i + str(k)
#             st += sr
#     return st
#
#
# def char_count2(str1):
#     st = ''
#     c = 1
#     # li=list(itertools.groupby(str1))
#     # print(li)
#     res = ["".join(group) for ele, group in itertools.groupby(str1)]
#     for t in res:
#         r=t[0]+str(len(t))
#         st+=r
#     return st
#
#
# # print(char_count('AAABBCCCCDDDEEF'))
# print(char_count2('AAABBCCAADDDEEF'))
# Python
# 3.12
# .1(tags / v3
# .12
# .1: 2305
# ca5, Dec
# 7
# 2023, 22: 03:25) [MSC v.1937 64 bit(AMD64)]
# on
# win32
# Type
# "help", "copyright", "credits" or "license()"
# for more information.
#     2 + 3
# 5
# print
# u
# SyntaxError: Missing
# parentheses in call
# to
# 'print'.Did
# you
# mean
# print(...)?
# print('jgsdd')
# jgsdd
# for i range(9):
#
# SyntaxError: invalid
# syntax
# for t in range(7):
#     print(t, end=' ')
#
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# if 'wfw':
#     print('usgdhnsj')
#
# usgdhnsj
# width = 20
# height = 5 * 9
# width * height
# 900
# n
# Traceback(most
# recent
# call
# last):
# File
# "<pyshell#13>", line
# 1, in < module >
# n
# NameError: name
# 'n' is not defined
# 4 * 3.75 - 1
# 14.0
# 'spam eggs'
# 'spam eggs'
# 'doesn\'t'
# "doesn't"
# s = 'First line.\nSecond line.'
# s
# 'First line.\nSecond line.'
# print(s)
# First
# line.
# Second
# line.
# print('first \nSecond')
# first
# Second
# 3 * 'un' + 'ium'
# 'unununium'
# print('py''thon')
# python
# s = 'gubj'
# print(s
# 'tttt')
# SyntaxError: invalid
# syntax
# s = 'python'
# s[-2:]
# 'on'
# s[-7:]
# 'python'
# s[:2] + s[2:]
# 'python'
# s[4:89]
# 'on'
# s[0] = 'p'
# Traceback(most
# recent
# call
# last):
# File
# "<pyshell#30>", line
# 1, in < module >
# s[0] = 'p'
# TypeError: 'str'
# object
# does
# not support
# item
# assignment
# sq = [1, 4, 9, 16, 25]
# sq
# [1, 4, 9, 16, 25]
# sq[0]
# 1
# sq[-1]
# 25
# sq[-2]
# 16
# sq[-3:]
# [9, 16, 25]
# sq * 3
# [1, 4, 9, 16, 25, 1, 4, 9, 16, 25, 1, 4, 9, 16, 25]
# sq ** 3
# Traceback(most
# recent
# call
# last):
# File
# "<pyshell#38>", line
# 1, in < module >
# sq ** 3
# TypeError: unsupported
# operand
# type(s)
# for ** or pow(): 'list' and 'int'
# sq.append(7 * 7)
# sq
# [1, 4, 9, 16, 25, 49]
# sq[:]
# [1, 4, 9, 16, 25, 49]
# n = [1, 2, 3]
# x = [sq, n]
# x
# [[1, 4, 9, 16, 25, 49], [1, 2, 3]]
# x[0]
# [1, 4, 9, 16, 25, 49]
# x[0][0]
# 1
# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a + b
#
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# print( if [])
# SyntaxError: invalid
# syntax
# if []:
#     'jhdjd'
#
# if []:
#     print('sfdg')
#
# if [1, 2]:
#     print('kjsgdkj')
#
# kjsgdkj
# for i in sq:
#     print(i, len(i))
#
# Traceback(most
# recent
# call
# last):
# File
# "<pyshell#64>", line
# 2, in < module >
# print(i, len(i))
# TypeError: object
# of
# type
# 'int'
# has
# no
# len()
# for i in sq:
#     print(i)
#
# 1
# 4
# 9
# 16
# 25
# 49
# for t in sq:
#     print(t, end=' ')
#
# 1
# 4
# 9
# 16
# 25
# 49
# list(range(5, 10))
# [5, 6, 7, 8, 9]
# list(range(0, 10, 3))
# [0, 3, 6, 9]
# list(range(-10, -100, -30))
# [-10, -40, -70]
# list(range(0, 10, -2)
#      )
# []
# list(range(0, 10, -2))
# []
# list(range(10, 0, -2))
# [10, 8, 6, 4, 2]
# a = ['ddssd', 'fdfe', 'ee', 'ewefrevgr']
# for t in range(len(a)):
#     print(t, a[t])
#
# 0
# ddssd
# 1
# fdfe
# 2
# ee
# 3
# ewefrevgr
# range(10)
# range(0, 10)
# sum(range(10))
# 45
# str(range(10))
# 'range(0, 10)'
# for n in range(2, 10):
# for n in range(2,10):
#     for x in range(2,n):
#         # print(n, x)
#         if n%x==0:
#
#             # print(n,'equals',x,'*',n//x)
#             break
#     else:
#         print(n,'is a prime number')
# for num in range(2,10):
#     if num%2==0:
#         print('found an even number',num)
#         continue
#     print("Found an odd number",num)
# def error_io(status):
#     match status:
#         case 400 | 402:
#             return "bad request"
#         case 404:
#             return "not found"
#         case 418:
#             return "i'm a teapot"
#         case _:
#             # return "somthing wrong"
#             raise ValueError("guyigu")


#Defining functions

# def fib(n):
#     a,b=0,1
#     while a<n:
#         print(a,end=' ')
#         a,b=b,a+b
#     print()   #print empty line
#
# fib(2000)
# print(fib)
# f=fib
# f(2000)
# def fib2(n):
#     result=[]
#     a,b=0,1
#     while a<n:
#         result.append(a)
#         a,b=b,a+b
#     # else:
#         # return
#     return result
#
# f100=fib2(100)
# print(f100)

# Default Arguments

# def ask_ok(prompt,retries=4,reminder='please try again'):
#     while True:
#         reply=input(prompt)
#         if reply in {'y','ye','yes'}:
#             return True
#         if reply in {'n','no','nop','nope'}:
#             return False
#         retries=retries-1
#         if retries<0:
#             raise ValueError('Invalid user response')
#         print(reminder)
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on,only yes or no!')

# def f(a, L=[]):
#     L.append(a)
#     return L
# print(f(1))  #[1]
# print(f(2))  #[1,2]
# print(f(3))  #[1,2,3]

#keyword arguments

# def parrot(voltage,state='a stiff',action='voom',type='Norwegian blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
#
# parrot(1000)  #positional arguments
# parrot(voltage=1000)   #1 keyword argument
# parrot(voltage=100000,action='voooom')  #2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000) # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump') # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies') # 1 positional, 1 keywor
#invalid calls
# parrot() # required argument missing
# parrot(voltage=5.0, 'dead') # non-keyword argument after a keyword argument
# parrot(110, voltage=220) # duplicate value for the same argument
# parrot(actor='John Cleese') # unknown keyword argument
# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
#
# cheeseshop("Limburger", "It's very runny, sir.",
# "It's really very, VERY runny, sir.",
# shopkeeper="Michael Palin",
# client="John Cleese",
# sketch="Cheese Shop Sketch")

# def standard_arg(arg):
#     print(arg)
#
# def pos_only_arg(arg,/):
#     print(arg)
#
# def kws_only_arg(*,arg):
#     print(arg)
#
# def combined_exp(pos_only,/,standard,*,kwd_only):
#     print(pos_only,standard,kwd_only)
#
# standard_arg(2)
# standard_arg(arg=2)
# pos_only_arg(1)
# # pos_only_arg(arg=1)   Error
# # kws_only_arg(3)  Error
# kws_only_arg(arg=3)
# # combined_exp(1,2,3)  Error
# combined_exp(1,2,kwd_only=3)
# combined_exp(1,standard=2,kwd_only=3)
# combined_exp(pos_only=1, standard=2, kwd_only=3) Error


# def foo(name,/,**kwds):
#     return 'name' in kwds
#
# print(foo(1,**{'name':2}))

#Arbitarary arguments lists

# def concat(*args,sep='/'):
#     return sep.join(args)
#
# print(concat("earth",'mars','venus'))
# print(concat("earth", "mars", "venus", sep="."))

# Unpacking argument list
#
# print(list(range(3,6)))   #[3,4,5]
# args=[3,6]
# print(list(range(*args)))  #[3,4,5]

# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# print(parrot(**d))



