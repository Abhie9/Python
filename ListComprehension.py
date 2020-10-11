import random
'''Comprehensive list to print the square of given range'''

square=[i**2 for i in range(1,10)]
print(square)

'''print the table of choosen number'''
userIn=int(input("Pleas enter the number: "))
table=[print(userIn,i,userIn*i) for i in range(1,11)]

'''print the list deleting the even numbers'''
odds=[i for i in range(21)]
odds=[i for i in odds if i%2!=0]
print(odds)
