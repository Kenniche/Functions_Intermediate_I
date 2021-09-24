
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]



# 1.1  Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
print("---1.1---")
x[1][0] = 15
print (x)


# 1.2 Change the last_name of the first student from 'Jordan' to 'Bryant'
print("---1.2---")
students[0]['last_name'] = 'Bryant'
print(students)


# 1.3 In the sports_directory, change 'Messi' to 'Andres'
print("---1.3---")
sports_directory ['soccer'][0]="Andres"
print(sports_directory)

# 1.4 Change the value 20 in z to 30
print("---1.4---")

z [0]['y'] = 30
print (z)



#  2.Iterate Through a List of Dictionaries
print("----2----")

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for i in some_list:
        print(f'first_name - {i["first_name"]}, last_name - {i["last_name"]}')

iterateDictionary(students)

# 3. Get Values From a List of Dictionaries
print("----3----")

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])
iterateDictionary2("first_name", students)
print("-------")
iterateDictionary2("last_name", students)


# 4. Iterate Through a Dictionary with List Values
print("----4----")
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(f"{len(some_dict[key])} {key.upper()}")
        for item in some_dict[key]:
            print(item)
        print("--------") 

printInfo(dojo)