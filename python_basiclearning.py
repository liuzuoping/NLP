# Introduction to Python
# python中的变量和操作
# Printing to he console

print("Hello world")

a = 10
b = "This is a string"
c = 12.5

print(a,b,c)

print("The value of a is ",a)


# Mathematical Operations

num1 = 12
num2 = 4

result = num1+num2
result = num1-num2
result = num1*num2
result = num1/num2
result = num1%num2

print(result)


# Special operations

sen = "I love Avengers\n"
print(sen*5)

print("I like cats", end=" ")
print("so much")


# Structure of if statements
"""
if condition:
    Statements
elif condition:
    Statements
else:
    Statements
"""

# python中的条件语句
#Grade of a student

marks = 90

# No braces in Python, Indectation does the job

if marks > 90:
    print("Grade O")
elif marks > 80:
    print("Grade E")
elif marks > 70:
    print("Grade A")
elif marks > 60:
    print("Grade B")
elif marks > 50:
    print("Grade C")
else:
    print("Better luck next time")

# Divisible or not

number1 = 45
number2 = 5

if number1%number2 == 0:
    print("Divisible")
else:
    print("not divisible")



# python中的循环
# While Loop

"""
while condition:
    Statements
"""

i = 1;

while i <= 10:
    print(i)
    i += 1

# For loop

for i in range(1, 11):
    print(i)

# Nested Loops

"""
12345
12345
12345
12345
"""

for i in range(1, 5):
    for j in range(1, 6):
        print(j, end=" ")
    print()

# Loop Control Statements

i = 1

while i <= 10:
    print(i)
    i += 1

# Break statement

i = 1

while i <= 10:
    if i > 5:
        # come out of this loop
        break
    print(i)
    i += 1

# Continue

i = 1

while i <= 10:
    if i >= 4 and i <= 7:
        i += 1
        continue
    print(i)
    i += 1

for i in range(1, 11):
    if i >= 4 and i <= 7:
        continue
    print(i)

# Pass

i = 1

if i == 1:
    pass
else:
    pass

# python中的列表
# Non homogeneous collection of elements

list1 = [12, 12.8, 'This is a string']

# Printing the list

print(list1)
print(list1[0])
print(list1[1])
print(list1[2])

# Adding elements to the list

list1.append(50)
list1.insert(0, 'Another string')

print(list1[3])

# Updating List

list1[1] = 20

# Deleting elements of the list

list1.pop()

del list1[2]

# Length of the list

print(len(list1))

# Looping through List

# Method 1 : Using Indexes (Mainly for updating)

for i in range(0, len(list1)):
    print(list1[i])
    list1[i] = 12  # Something else

# Method 2 : For each technique (Mainly for accessing)

for item in list1:
    print(item)


# python中的元组
# Same as List but immutable

tuple1 = (12,)

tuple1 = ('This is a string', 14.5, 0.9, 500, 'Another string')
tuple2 = ('Next tuple', 14.5, 0.9, 500)

# Printing elements of tuples

print(tuple1)
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])

# Adding two tuples

tuple3 = tuple1 + tuple2

# Length of a tuple

print(len(tuple3))

# Looping through a tuple

# Method 1

for i in range(0, len(tuple1)):
    print(tuple1[i])

# Method 2

for item in tuple1:
    print(item)


# python中的字典
# Key - Value Pairs

dict1 = {}

# Adding elements to the dictinary

dict1['apple'] = 'Apple is a fruit'
dict1['orange'] = 'Orange is a fruit'
dict1['car'] = 'Cars are fast'
dict1['python'] = 'Python is a snake'

# Printing dictionary elements

print(dict1)
print(dict1['apple'])
print(dict1['car'])
print(dict1['python'])

print(dict1.get('jython','Does not exist'))

# Deleting elements

del dict1['apple']

# Length of a dictionary

print(len(dict1))

# List of keys and Values

listOfKeys = list(dict1.keys())
listOfValues = list(dict1.values())

# Looping through lists

for key in dict1.keys():
    print(dict1[key])

# python中的文件操作
# Console I/O

inp = input('Enter a number: ')
number1 = int(inp)

inp = input('Enter a number: ')
number2 = int(inp)

print(number1 + number2)

# File I/O

# Writing to a file

inp = input('Enter some text: ')

with open('textFile.txt', 'a') as f:
    f.write(inp)

# Reading from a file

with open('textFile.txt', 'r') as f:
    string = f.read()
    print(string)


# python中的函数
# Block of meaningful code

def functionName(arg1, arg2):
    print(arg1, arg2)


functionName('The number is', 12)


def sumOfTwo(num1, num2):
    return (num1 + num2)


print(sumOfTwo(12, 15))


# Classes and Objects
# python中的类和对象
# Simple Class
class Fish:
    def swim(self):
        print("Fish is swimming")

    def eat(self):
        print("Fish is eating")


fish = Fish()
fish.swim()
fish.eat()


# Overriding constructor
class Game:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(self.name, "has started")

    def stop(self):
        print(self.name, "has stopped")


game = Game("Counter Strike")
game.start()
game.stop()


# python中的列表操作
# List comprehension in Python

numbers = [1,2,3,4,5,6,7,8,9,10]

# Copying using a loop
newNumbers = []
for number in numbers:
    newNumbers.append(number)

# Copying using list comprehension
newNumbers = [number for number in numbers]

# Copying and filtering based on condition
newNumbers = [number for number in numbers if number <= 5]

# Copying and filtering based on another list
numbers2 = [1,3,5,7,9]
newNumbers = [number for number in numbers if number not in numbers2]

# Some more examples
newNumbers = [number*2 for number in numbers]
newNumbers = [number for number in numbers if number%2 == 1]

# Generator Comprehension
squareGen= (number**2 for number in numbers)
list(squareGen)

# Dictionary Comprehension
myDict = {"apple":1,"orange":4,"banana":10}
newDict = {key:myDict[key] for key in myDict.keys()}

newDict = {key:myDict[key] for key in myDict.keys() if myDict[key] > 5}


# Joining list of words
words = ["I","love","Avengers","so","much"]
sentence = ' '.join(words)
sentence = '.'.join(words)