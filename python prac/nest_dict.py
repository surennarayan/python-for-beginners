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
# pets = [] #as of now i add three but think it conation millons of pets and owner details
# pet = {
#     'name': 'maccow',
#     'animal': 'parrot',
#     'kind': 'bird',
#     'owner': 'jack',
# }
# pets.append(pet)
# pet1 = {
#     'name': 'puli',
#     'animal': 'lion',
#     'kind': 'wild animal',
#     'owner': 'surendra'
# } 
# pets.append(pet1)
# pet2 = {
#     'name': 'veera',
#     'animal': 'dog',
#     'kind': 'domestic animal',
#     'owner': 'kalbhairav'
# } 
# pets.append(pet2)
# for pet in pets:
#     print(f"\n here's what i know {pet['name'].title()}")
#     for key, value in pet.items():
#         print(f"{key} : {value}")
# print("Practice is Best way to Success")

# # Practing more on the nesting 

# favorite_places = {
#     'surendra': {
#         'place1': 'america',
#         'place2': 'europe',
#         'place3': 'london'
#     },
#     'dharani': {
#         'place1': 'delhi',
#         'place2': 'chennai',
#         'place3': 'tiruvanamali',
#     },
#     'narayan': {
#         'place1': 'shiva temple',
#         'place2': 'murugan temple',
#         'place3': 'tirupati',
#     }
# }
# for person_name, person_info in favorite_places.items():
#     print(f"\n {person_name.title()} likes these places")
#     for key, value in person_info.items():
#         print(f"\t {value.title()}")

# nesting more
# cities = {
#     'bangalore': {
#         'country': 'india',
#         'population': '1 million',
#         'fact': 'my birth place',
#     },
#     'london': {
#         'country': 'united kingdom',
#         'population': '2 million',
#         'fact': 'good place for tourism',
#     },
#     'new_york': {
#         'country': 'united states',
#         'population': '3 million',
#         'fact': 'more tech hubs',
#     }
# }
# for city, city_info in cities.items():
#     country = city_info['country'].title()
#     population = city_info['population'].title()
#     fact = city_info['fact'].title()
#     print(f"{city.title()} is in {country} and The population is {population} and its good for {fact}.") 
# doram = "f{city.title()} is in '{country'} and The population is '{population'} and its good for '{fact'}."
# print(len(doram))
   
# fav_numbs = {'suren': [9, 3, 11],
#              'vasa': [12, 11, 14],
#              'narayan': [29, 40, 38],
#               }
# fav_numbs['dharani'] = [3, 4, 5]
# for name, numbers in fav_numbs.items():
#     print(f"{name.title()} likes the following numbers: ")         
#     for number in numbers:
#         print(f" {number}")

#input() funtion
# car = input("What kind of car would you like? ")
# print(f"Let me see if i can find you a {car.title()}")

# party_size = input("How many people are in your dinner group: ")
# party_size = int(party_size)
# if party_size > 8:
#     print("Sorry the table is full please wait for a table")
# else:
#     print("Your table is ready")

# num = int(input("Enter the number: "))
# if num % 10 == 0:
#     print(f"{num} its the multiple of 10 ")
# else: 
#     print("No the multiple of 10")

# while looping

# prompt = "What toppings would you like? "
# prompt += "\nEnter quit to exit: "
# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"I'll add your {topping}topping to pizza")
#     else:
#         break

prompt = "What's your age? "
prompt += "\n enter quit to exit: "
while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("The ticket is free!")
    elif age < 13:
        print("the ticket is $10.")
    else:
        print("the ticket is 15$.")