# Loops ..
# While loops..
# n = 5
# while  n > 0 :
#     print(n)
#     n = n - 1
# print('blast off')


# For loops ... it will check the values

# num = [1,2,3,4,5]
# for i in num:
#     print('it is a num')

# num = [1,2,3,4]
# print(len(text))
# text = 'john'
# for i in text :
#     if i == 'h' :
#         print(' h is included')
#         break
#     else :
#         print( ' h is not included')

#  Range  -- (start , stop, step and skip)
# for i in range(1, 11,2) :
#     print(i)

# find the even number ..
# for i in range(1,11) :
#     if i%2 == 0 :
#         print(i)

# for i in range(1 , 4) :
#     print('outer loop')
#     for j in range(1 , 3):
#         print(' inner loop')


# number = int(input("Enter a number"))
# even = 0 
# odd = 0 
# for i in range(number) :
#     if i % 2 == 0 :
#         even  = even + 1 
#     else :
#         odd = odd + i 
#         print(f"Sum of even numbers are {even} and odd numbers are {odd}")

# in the range  a single value (5) it will be stop automattically ..
# for i in range(5):
#     print(i)
# for i in range(5 , 10) :
#     print(i)

# for i in range(15 , 10 , -1) :
#     print(i)

# convert range to list ..
# numbers = list(range(1,6))
# print(numbers)  

# using range() with leng ()
# fruits = ['apple' , 'orange' , 'kiwi' , 'banana']
# for item in range(len(fruits)) :
#     print( item , fruits[item])