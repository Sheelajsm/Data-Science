# 1. Python program to print first n prime numbers where n is the input
n=int(input("Enter the number:"))
list_prime=[]
for i in range(2,n+1): 
    if n>1:
        prime=true
        for j in range(2,i):
            if(i%j) == 0:
            prime=false
            break
        else:
            print(i)
        if prime:
            list_prime.append(i)
o/p: 
 Enter the number:12
2
3
5
7
11
            
       
2. Python Program to remove duplicate elements from a list WITHOUT using set
input = [1,2,23,12,45,56,35,23,45,67,98]
output=[]
for i in input:
    if i not in output:
       output.append(i)
print(output)
            
#o/p: 
[1, 2, 23, 12, 45, 56, 35, 67, 98]



3. Filter the price in a dictionary, check if the price of the item is 
	greater than 2000, between 3000-7000 and so on
	Ex: 
		smart_phone_dict =  {'Samsung': 35500, 'Realme': 14000, 'Moto G10 Power': 3500, 'OnePlus 8 Pro':50000, 'Samsung 2': 6000, 'Lika': 1500
		, 'Lava': 2500,  'Redme': 4500}

smart_phone_dic =  {'Samsung': 35500,
                     'Realme': 14000, 
                     'Moto G10 Power': 3500,
                     'OnePlus 8 Pro':50000,
                     'Samsung 2': 6000, 
                     'Lika': 1500 ,
                     'Lava': 2500,  
                     'Redme': 4500}

smart_phone_dict = dict()
smart_phone = dict()
for (key, value) in smart_phone_dic.items():
    if value >2000: 
        smart_phone_dict[key]=value
print(smart_phone_dict)

for (key, value) in smart_phone_dic.items():
    if value > 2000 and value < 7000:
        smart_phone[key]=value
print(smart_phone)


# O/P:
{'Samsung': 35500, 'Realme': 14000, 'Moto G10 Power': 3500, 'OnePlus 8 Pro': 50000, 'Samsung 2': 6000, 'Lava': 2500, 'Redme': 4500}
{'Moto G10 Power': 3500, 'Samsung 2': 6000, 'Lava': 2500, 'Redme': 4500}