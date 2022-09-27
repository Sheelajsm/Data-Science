# 1. Write a function to find sum of the list elements
	# Ex: Input [12,2,46]
	# output = 60
    
# total = 0
# list1 = [12, 2, 46]
# for i in range(0, len(list1)):
    # total = total + list1[i]
# print("Sum of all elements in given list: ", total)

# O/P: Sum of all elements in given list:  60


# def total():
    # print(12+2+46)
# total()

 
    
# 2. Write a function to count the number of times a letter appered in a word
	# example: p count in apple is 2
	# input word, letter
	# output count
    
# x = "apple"
# print(x.count("p"))

# o/p: 2


	
# 3. Write a function to print positive numbers in a list
	# Ex: Input [-12,2,46, -20, 40, -99, 33]
	# output = [2,46,40,33]
    
# list2 = [-12,2,46, -20, 40, -99, 33]
# list_positive = []
# list_positive = [i for i in list2 if i>=0]
# print(list_positive)

# o/p: [2, 46, 40, 33]


	
# 4. Wite a function to print empty elemets in list
	# Ex: Input [apple, '', 123, [], 22, 45, -30, None]
	# output = [apple, 123, 22, 45]
# count = 0	
# list3 = ["apple", '', 123, [], 22, 45, -30, None]
# for i in list3:
    # i = i + 1
    # list3.remove("")
    # list3.remove([])
    # list3.remove(None)
# print(i)
# print("List of non empty elements in a list=",str(list3))

# O/P: List of non empty elements in a list= ['apple', 123, 22, 45, -30]

input = ["apple", '', 123, [], 22, 45, -30, None]
for i in input:
    if not i:
        print(i)
        input.remove(i)
        
o/P:

[]
None

        
        
# input = ["apple", '', 123, [], 22, 45, -30, None]
# output = []
# for i in input:
    # if i:
        # output.append(i)
# print(output)
               
        

# 5. Wite a function to print duplicate elements in the list
# list4 = [10,12,13,14,10,23,12,14,17]
# new_list = []
# #new_list = list([item for item in list4 if list4[item]>1])

# for i in list4:
    # #n = list4.count(i)
    # #if n > 1:
    # if new_list.count(i) == 0:  
        # new_list.append(i)
# print("Duplicate elements in a list=", new_list)
 
# #O/p: [10, 12, 14]



# 6. Wite a function to find second largest number in a list
# list1 = [9, 6, 4, 10, 13, 2, 3, 5]
# Elements_list = set(list1)
# Elements_list.remove(max(Elements_list))
# print(max(Elements_list))

# O/p: 10



# 7. Write a function using list-comprehension to create a list of numbers which are divisible by 3
	# example input [1, 3, 5, 9, 11, 12, 20, 15, 50, 33]
	# output => [3,9,12,15,33]
# List5=[1, 3, 5, 9, 11, 12, 20, 15, 50, 33]
# new_list=[ i for i in List5 if i%3==0]
# print(new_list)

# O/P: [3, 9, 12, 15, 33]



# 8. Write a function to sort a list without using sort function
# List6 = [2, 5, 4 -2, -1, 8, 9]

# for i in range(len(List6)):
    # for j in range(i + 1, len(List6)):
        # if List6[i] > List6[j]:
            # List6[i], List6[j] = List6[j], List6[i]
# print(List6)

# O/P: [-1, 2, 2, 5, 8, 9]



# 9.  Python function to convert Fahrenheit to Celsius
# def convert(x):
    # ft = float(x)
    # s = (ft-32)*5/9
    # return s

# print(convert(76))  

# O/P: 24.444444444444443




# 10. Python function to remove  vowels in a given word
# x = 'united states'
# newstr = (x)
# vowels = ('a', 'e', 'i', 'o', 'u')
# for i in x:
    # if i in vowels:
       # newstr = newstr.replace(i,"")        
# print(newstr)

# O/P: ntd stts

       #['apple', '', 123, [], 22, 45, -30, None]
       #['apple', 123, 22, 45, -30]
