
'''
Given the list y = [6,4,2] add the items 12, 8
Change the 2nd item of the list to 3
Repeat this for a dictionary.
Key values in dict should be named> Lowest, second lowest, medium, highest, etc.
You can use max(), min()
'''
listy = [6,4,2]
listy.append(12)
listy.append(8)
listy[1] = 3
print(listy)

highestValue = max(listy)
lowestValue = min(listy)

print(highestValue,lowestValue)


dictY = {
    "Highest":highestValue,
    "Second highest":8,
    "Medium":6,
    "Second lowest":3,
    "Lowest":lowestValue,
    }

dictY["Second lowest"] = 3

print(dictY)