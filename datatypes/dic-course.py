# what is dictionary?
# # A dictionary is a collection of key-value pairs where each
# key is unique and is used to store and retrieve values efficiently.

# data={
#     'name':'ram',
#     'age':25
# }
# print(dir(data))
# print(data.keys())
# print(data.values())
# print(data.items())
# data.update({'names':['ram','shyam','hari']})
# print(data)

# print(data['names'])
# print(data.get('name','key not found')) 
# print("we are learning dictionary")


# data=[
#     {'name':'ram','address':'ktm'},
#     {'name':'sita','address':'bkt'},
# ]

# print(data[1]['name'])

# data={
#     'name':'sita',
#     'address':{
#         'city':'kathmandu',
#         'country':'nepal'
#     },
#     'contact':[
#         {'type':'email'},
#         {'type':'phone'}
#     ]
# }

# print(data['address']['city'])
# print(data['contact'][1]['type'])


# data={
#     'name':'sita',
#     'password':'sita002',
#     'role':'admin'
# }

# print(dir(data))
# data.pop('password')
# data.popitem()
# data['phone']=9845000000
# data['name']='sophia'
# data.update({'name':'laxmi'})
# print(data)