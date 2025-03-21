# Nesting with Dictionaries 
# peoples = []
# person1 = {
#     'first_name': 'surendra',
#     'last_name': 'narayan',
#     'qualification': 'BTech',
#     'age': 23
# }
# peoples.append(person1)
# person2 = {
#     'first_name': 'Dharani',
#     'last_name': 'narayan',
#     'qualification': 'Bsc',
#     'age': 18
# }
# peoples.append(person2)
# person3 = {
#     'first_name': 'narayana',
#     'last_name': 'murthy',
#     'qualification': 'BTech',
#     'age': 40
# }
# peoples.append(person3)
# for people in peoples:
#     name = f"{people['first_name'] +' '+ people['last_name'] }"
#     qf = people['qualification']
#     age = people['age']
#     print(f"I'm {name.title()} and my qualification is {qf} and age is {age}")

# working with nesting more

pets = [] #as of now i add three but think it conation millons of pets and owner details
pet = {
    'name': 'maccow',
    'animal': 'parrot',
    'kind': 'bird',
    'owner': 'jack',
}
pets.append(pet)
pet1 = {
    'name': 'puli',
    'animal': 'lion',
    'kind': 'wild animal',
    'owner': 'surendra'
} 
pets.append(pet1)
pet2 = {
    'name': 'veera',
    'animal': 'dog',
    'kind': 'domestic animal',
    'owner': 'kalbhairav'
} 
pets.append(pet2)
for pet in pets:
    print(f"\n here's what i know {pet['name'].title()}")
    for key, value in pet.items():
        print(f"{key} : {value}")
        
