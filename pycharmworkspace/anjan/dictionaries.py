# Dictionary is similar to list.
# Dictionary has key and value.
# Empty Dictioanry is declared using Curl Braces

wordsAndThingsDict = {}

# Adding some things to the dictionary
wordsAndThingsDict["Apple"] = "Red things that taste good. Specially not ana orange"
wordsAndThingsDict["Orange"] = "Makes great Juice."
wordsAndThingsDict[3] = "The number 3"
wordsAndThingsDict['A List'] = ['oh','boy!','A list in a dictioanry']
wordsAndThingsDict['Inception'] = {'Nested':'When dictionary is a VALUES is a dictionary'}

# Print the dictionary
print(str(wordsAndThingsDict))

for key in wordsAndThingsDict:
    print("Key :: " + str(key))

    # Print the value of using the key to "look it up"
    print("Value :: " + str(wordsAndThingsDict[key]))
    print()


screen = {'height':1704,'width':1080}
screen/2
