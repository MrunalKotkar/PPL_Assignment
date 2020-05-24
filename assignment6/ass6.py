#Exceptions in python

try:
    for i in range(3):
        print(3/i)
except:
    print("You divided by 0")
    print("This prints because the exception was handled")

print("\n")

#Multiple except
a,b=1,0
try:
          #print(a/b)
          print("This won't be printed")
          print('10'+10)
except TypeError:
          print("You added values of incompatible types")
except ZeroDivisionError:
          print("You divided by 0")
print("\n")

#one more example
a,b=1,0
try:
   print(a/b)
except:
   print("You can't divide by 0")
print("Will this be printed?")
print("\n")

#Multiple exceptions in one Except
try:
      #print('10'+10)
      print(1/0)
except (TypeError,ZeroDivisionError):
      print("Invalid input")
print("\n")

#Generic except after all exceptions
try:
    print('1'+1)
    print(summation)
    print(1/0)
except NameError:
    print("sum does not exist")
except ZeroDivisionError:
    print("Cannot divide by 0")
except:
    print("Something went wrong")

#print("\n")

#we can’t put a statement between try and catch blocks.

#Raise error
a,b=int(input()),int(input())
try:
       if b==0:
             raise ZeroDivisionError
except:
   print("You divided by 0")
print("Will this print?")

#We can also raise by an argument

#File handling
try:
    file = open('msk.txt', 'r')
    for each in file:
        print(each)
except:
    print("File does not exist")
print("File handling.")