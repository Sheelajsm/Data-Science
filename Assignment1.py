Questions

# 1)Different ways of commenting Python

# By using Hashtag symbol and by triple quotes at the begining and ending of string literals.
# Select single line or multiple line, right click the mouse, by clicking on Block comment also  we  can comment in python.
# Doc strings - They are used to document our code. triple quotes within the string literal.

# 2)
# Syntax: isalnum()
# Define a variable as string consisting of both numbers and characters then print ("Statement ",variable.isalnum))it returns true or false.

# 3)
# Syntax: variable.insert(index,value)
# print(variable)
# We can insert an object within the List

# 4)
# variable.remove(element)
# variable.pop() ==>last element got removed
# The del keyword is used
# Syntax: del variable[index]
# print(variable)
# variable.clear() ==> clear all the elements

# 5)
# Textual, Numerical, sequence, Dictionary(mapping/Hashtags), Boolean, Binary,none 
# Nums=[0,20,-30,50,60]
# Nums.reverse()
# print(Nums)
# o/p: [60, 50, -30, 20, 0]

# 6)
# Nums=[0,20,-30,50,60]
# Nums.sort()
# print (Nums) 
 # O/p: [-30, 0, 20, 50, 60]
 
# 7)
# Python assigns values from right to left. When assigning multiple variables in a single line, 
# different variable names are provided to the left of the assignment operator separated by a 
# comma. The same goes for their respective values except they should to the right of the 
# assignment operator.
# a,b,c,d=1,3,4,"abc"
# print(a,b,c,d)

# 8)
# List=[1,[2,'three',[2,'abc',6.0],[18,'abc','6.3']],4.5]
# print(len(List))
# o/p: 3

# 9)
# str,int,float,complex,list tuple,range, dict,set,none

# 10)
# slice==> [start:end:skip]
# A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, 
# and where to end. 
# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(0, 8, 3)
# print(a[x])
# o/p ('a', 'd', 'g')

# 11)
# def swapPositions(list, pos1, pos2):
     
    # list[pos1], list[pos2] = list[pos2], list[pos1]
    # return list
 
# List = [1,2,3,5,6,8,"ABCD","MNO",6.0]
# pos1, pos2  = 1, 7
 
# print(swapPositions(List, pos1, pos2))
# o/p: [1, 'MNO', 3, 5, 6, 8, 'ABCD', 2, 6.0]

# 12)
# str1 = "The government has decided to rename the historic Rajpath in the \"national\" capital as Kartavya Path, sources said on September 5,2022"
# print(str1.split(' ')[11])
# o/p: "national"

# 13)
# x=[1,2,3,5,6,8,"ABCD","MNO",6.0]
# even=x[1::2]
# print(even)

# o/p: [2, 5, 8, 'MNO']

# 13)

# We can remove Duplicate elements in a list by using set() function.
# Syntax: variable_list=list(set(variable_list))


# 14)
employee_1={
        "Name":"Manju",
        "Age":40,
        "Company":"Volvo",
        "Salary":12.5,
        "Skill":["Excel","Python","VB"]
        }
employee_2={
         "Name":"Sanju",
         "Age":30,
         "Company":"Oracle",
         "Salary":10.5,
         "Skill":["Python","C","Java"]
         }
employee_1.update(employee_2)
print(employee_1)

 #o/p {'Name': 'Sanju', 'Age': 30, 'Company': 'Oracle', 'Salary': 10.5, 'Skill': 'Python'}


