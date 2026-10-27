# types of error handling 

# try :
    # code that may cause an error

# except :
#    runs when an error occurs 

# else : 
    # runs when no error occurs 

# finally :
    # always run 

# try:
#     num1 = 10 
#     num2 = 0
#     result = num1/num2
#     print(result)
# except :
#     print('An error occured ')
# else :
#     print(' no errors occurs ')

# finally :
#     print('i run always ')


# try:
#     num1 = 10 
#     num2 = 2
#     result = num1/num2
#     print(result)
# except :
#     print('An error occured ')
# else :
#     print(' no errors occurs ')

# finally :
#     print('i run always ')



try :
    num1 = 10 
    num2 = 0 
    result = num1/num2
    print(result)
except ZeroDivisionError :
    print(" can't divide ")

