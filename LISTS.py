# LISTS
    # list = collection
    # collection allows to put many values in single 'variable'
    
friends = ['Jospeh', 'Glenn', 'Sally'] #contains 3 strings
carryon = ['socks', 'shirt', 'perfume']
print friends [1]
#   Glenn
    # no collection --> variable has one value; new value overwrites old value


# list constants
    # are surrounded by [] + elements in list are separated by ,
    # a list can be empty and a list element can be another list

print [1,24,76]
print ['red', 'yellow', 'blue']
print []
print [1, [5,6], 7]
print ['red', 24, 98.6]


# lists and definite loops

friends = ['Jospeh', 'Glenn', 'Sally']
for friend in friends:
    print 'Happy New Year:', friend
print 'Done'


# lists are mutable

    # elements of a list can be changed using the index operator

lotto = [2,14,26,41,63]
lotto[2] = 28
print lotto
#   [2,14,28,41,63]

# len() function
    
    # len() function takes a list as a parameter and returns the number of elements in the list

x = [1,2,'joe',99]
print len(x)
#   4


# range function

    # returns a list of numbers that range from zero to one less than the parameter
    # index loop using for and an integer iterator

print range(4)
#   [0,1,2,3]
friends = ['Jospeh', 'Glenn', 'Sally']
print len(friends)
#   3
print range(len(friends))
#   [0,1,2]

for i in range(len(friends)):
    friend = friends[1]
    print 'Happy New Year:', friend
    
    
# concatenating lists

    # by using +

a = [1,2,3]
b = [4,5,6]
c = a+b
print c
#   [1,2,3,4,5,6]


# slicing lists

t = [9,41,12,3,74,15]
t[1:3]
#   [41,12]
t[:4]
#   [9,41,12,3]


# list methods

x = list()
dir(x)
#   ['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# building a list

    # create an empty list + fill with append method

stuff = list()
stuff.append('book')
stuff.append(99)
print stuff
#   ['book', 99]


# True False operator
    
    # to check if something is in a list
    # do not modify list

some = [1,9,21,10,16]
9 in some
#   True
15 in some
#   False
20 not in some
#   True


# sort lists

friends = ['Jospeh', 'Glenn', 'Sally']
friends.sort()
print friends
#   ['Glenn', 'Joseph', 'Sally']


# built in functions

nums = [3, 41, 12, 9, 74, 15]
print len(nums)
#   6
print max(nums)
#   74
print min(nums)
#   3
print sum(nums)
#   154
print sum(nums)/len(nums)
#   25


# averaging with a list

total = 0
count = 0
while True:
    inp = raw_input('Enter a number:')
    if inp == 'done': break
    value = float(inp)
    total = total + value
    count = count + 1
    
average = total/count
print 'Average', average

numlist = list()
while True:
    inp = raw_input('Enter a number:')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist)/len(numlist)
print 'Average', average


# split() function

    # breaks a string into parts 
    # split delimiter can be defined eg split(';') or split('g') --> splits after each ; or g
    
abc = 'With three words'
stuff = abc.split()
print stuff
#   ['With, 'three', 'words']
print len(stuff)
#   3
for w in stuff:
    print w
#   With
#   three
#   words


# exercise

fhand = open('mbox-short.txt') # opens file
for line in fhand: # runs through each line
    line = line.rstrip() # get rid of whitespaces at the end of the line
    if not line.startswith('From '): continue # skips lines that do not start with From 
    words = line.split() # take line and split it into elements
    print words[2] # take word 2
    email = words[1] # choose word 2 eg email address
    pieces = email.split('@') # splits email adress in two pieces --> before and after @
    print pieces[1] # get part after @ sign
    
    
 # just a test
    
    

    


    
