# my_dict ={
#     "name" : "john",
#     "age"  : 40,
#     "city" : "calicut"
# }
# print(my_dict)

# creating dictionaries
# my_dict ={'name' : 'john' , 'age' : 30, 'city' : 'NYC'}
# print(my_dict)
# empty_dict = {}


# my_dict ={
#        "name" : "john" ,
#        "age"  : 40 ,
#        "city" : "calicut"

# }

# print(my_dict["name"])
# print(my_dict["age"])

# METHODS ..

# my_dict ={
#     'name' : 'john' ,
#     'age'  : '30 ' ,
#     'city' : 'NYC' ,
#     'is_active' : True,

# }
#  #keys() - get all keys
# print(my_dict.keys())
# print(type(my_dict.keys()))

# values() - Get all values ..
# print(my_dict.values())

# items() - Get key-value pairs 

# print(my_dict.items())

# print(my_dict["city"])
# get(key, default) - saflely get  value
# print(my_dict,get("rolnum" , 0))

# pop(key) - remove the keywords

# print(my_dict.pop("city"))
# print(my_dict)

# update(dict2) -merge dictionaries

dict1 = {'a' : 1, 'b' : 2}
# dict2 ={'c' : 4, 'd' : 5}
# dict1.update(dict2)
# print(dict1)

# # clear() - Remove the items.
# dict1.clear()
# print(dict1)

# copy() - Create shallow copy 
dict2 ={'c' : 4 ,'d' :5}
new_dict=dict2.copy()
print(new_dict)



