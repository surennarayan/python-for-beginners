# #Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
  
# # 1 Instantiate the Cat object with 3 cats
# catobj1=Cat('Tom', 15)
# catobj2=Cat('Mike', 25)
# catobj3=Cat('Pussy', 20)


# # 2 Create a function that finds the oldest cat
# def oldest_cat(*args):
#     return max(args)

# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(f'The oldest cat is {oldest_cat(catobj1.age,catobj2.age,catobj3.age)} years old.')

#exercise on list
# visit_places = ['America', 'London', 'Newyork','Australia', 'Swiss']
# print(sorted(visit_places, reverse=True) )
# print(visit_places)
# visit_places.reverse()
# print(visit_places)
# visit_places.reverse()
# print(visit_places)
# visit_places.sort()
# print(visit_places)
# visit_places.sort(reverse=True)
# print(visit_places)
# print(len(visit_places))

# works on list
# pizzas = ['veg pizza','margaritta','chicken pizza']
# for pizza in pizzas:
#     print("I like to have " + pizza)
# print('''the pizza is going real wonderful and 
#   it consists more chesse inti
#       and i really love pizza''')
#one more
# animals = ['cow','lion','elephant']
# for animal in animals:
#     if animal == 'cow':
#         print("I'm " + animal + " i'll produce milk.")
#     elif animal == 'lion':
#         print(animal + " is the king of forest")
#     else:
#         print("A huge " + animal)
# print(" the domestic animal might be useful ")
# SummingMillion = []
# for value in range(1, 100000):
#     SummingMillion.append(value)
# print(min(SummingMillion))
# print(max(SummingMillion))
# print(sum(SummingMillion))
# odd_numbers = []
# for num in range(1,20,2):
#     odd_numbers.append(num)
# print(odd_numbers)
#or
# odd_numbers = list(range(1,20,2))
# for num in odd_numbers:
#     print(num)
# multiple_of_threes = list(range(3,30,3))
# for value in multiple_of_threes:
#     print(value)
#list comprehension for cubes
# cubes = [value**3 for value in range(1,11)]
# print(cubes)
#or
# cubes = list(range(1,11))
# for value in cubes:
#     value = value**3
#     print(value)
# slices = ['car','bike','boat','ship','airline']
# ft = slices[:3]
# print(f"from first {ft}")
# mt = slices[1:4]
# print(f"from middle {mt}")
# lt = slices[2:]
# print(f"last three items {lt}")
# friend_pizzas = pizzas[:]
# pizzas.append('Corn pizza')
# friend_pizzas.append('Mushroom pizza')
# print("my favriote pizza are ")
# print(pizzas)
# print("my friends favriote pizza are ")
# print(friend_pizzas)
# for item in friend_pizzas:
#     print(item)
#tuple
# buffet = ("maggie", "roti", "soup", "panner", "beans")
# for item in buffet:
#     print(item)
# buffet[0] = "apple ice" #throws error because tuple cannot change the value these are not immutable
#fibbonaci series
# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         b = a+b
#         a = b
#     print()
# fibbo = fib(200)
# pizzas = ['veg pizza','margaritta','chicken pizza']
# chuk = 'corn'
# for item in pizzas:
#     if item == 'veg pizza':
#         print("its present")
# if chuk is not pizzas:
#     print(f"{chuk} is not in the list please update the list")
# alien colors
# alien_color = ('green', 'yellow', 'red')
# alien1 = 'greenn'
# if alien1 == alien_color[0] :
#     print("the player earned 5 points")
# elif alien1 != alien_color[0] :
#     print("You got the 10 points "+ alien_color[1])
# else :
#     print("You got 15 points "+ alien_color[2])
# stages of life
# age = int(input("enter your age :"))
# if age < 2:
#     print("you are a baby")
# elif 2 <= age and age < 4:
#     print("the person is a toddler")
# elif 4 <= age and age < 13:
#     print("the preson is a kid")
# elif 13 <= age and age < 20:
#     print("teenager")
# elif 20 <= age and age < 65:
#     print("adult")
# elif age > 65:
#     print("elder")
# working on dictionary
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))
# # Move the alien to the right.
# alien_0['speed'] = 'fast' #note
# # Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# elif alien_0['speed'] == 'fast': # a quick not its just a conditional statement
# # This must be a fast alien.
#     x_increment = 3
# # The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print("New x-position: " + str(alien_0['x_position']))

# person = {'first_name':'narayana',
#           'last_name': 'murthy',
#           'age': 49,
#           }
# print("The Full name of the preson is "+ person['first_name'].title() + " "+ person['last_name'].title() + " and the age is "+ str(person['age']))

# fav_numbs = {'suren': 9,
#              'anusha': 3,
#              'vasa': 12,
#              'narayan': 38,
#              'dharn': 45,
#               }
# for key, value in fav_numbs.items():
#     print(f"The {key.title()}  favorite number is {value}")
# fav_numbs['lang1'] = 'c'            
# print(fav_numbs)
# rivers = {'nile': 'egypt',
#           'ganga': 'india',
#           'deadsea': 'africa'}
# for key, value in rivers.items():
#     print(key.title() + "runs thorugh "+ value.title())
# for item in rivers.keys():
#     print(item.title() +" river")
# for item in rivers.values():
#     print(item.title() +" country")

# polling = {'suren': 'python',
#              'anusha': 'java',
#              'vasa': 'c',
#              'narayan': 'go',
#              'dharn': 'ruby',
#               }
# peoples_poll = ['suren', 'anusha', 'vasa', 'narayan', 'boss',]
# for people in polling.keys():
#     if people in peoples_poll:
#         print(f"Thanks for responding {people}")
#     else:
#         print(f"{people} please take the poll")

#nesting dictionary inside a list
# kitchen = []
# for item in range(20):
#     new_item = {'box1': 'chill', 'capacity': '10kg', 'exp': 2026}
#     kitchen.append(new_item)
# print("The capacity of the kitchen item is " + str(len(kitchen)))
# for new_item in kitchen[:5]:
#         if new_item['capacity'] == '10kg':
#             new_item['box1'] = 'Tea'
#             new_item['capacity'] = '5kg'
#             new_item['exp'] = 2025
# print(kitchen[:5])



