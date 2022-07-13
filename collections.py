
print('''
    Defining a list
''')

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print('''
    Accessing a list by position
''')

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

print('''
    Changing the values in a list
''')

myFruitList[2] = "orange"
print(myFruitList)

print('''
    Exercise 2: Introducing the tuple data type
''')

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print('''
    Accessing a tuple by position
''')
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

print('''
    Exercise 3: Introducing the dictionary data type
''')

myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print('''
    Accessing a dictionary by name
''')

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
