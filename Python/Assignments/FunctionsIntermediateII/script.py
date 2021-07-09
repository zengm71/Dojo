x = [ [5,2,3], [10,8,9] ] 
def changeX(x):
    for index, sublist in enumerate(x):
        if 10 in sublist:
            for subindex, element in enumerate(sublist):
                if 10 == element:
                    x[index][subindex] = 15
    return(x)
changeX(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
sports_directory

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
z

# 2 Iterate Through a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for student in students:
        print('first_name - ' + student['first_name'] + ", last_name - " + student['last_name'])
iterateDictionary(students) 

# 3 Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for x in some_list:
        print(x[key_name])
iterateDictionary2('first_name', students)    
iterateDictionary2('last_name', students)

# 4 Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for key_, value_ in dojo.items():
        print(str(len(value_)) + ' ' + key_)
        for v in value_:
            print(v)
        print('')
printInfo(dojo)
