thisIsaTuple = ("a",5,"car")
print(thisIsaTuple)
print(thisIsaTuple[0])

if "a" in thisIsaTuple:
    print("True")
print(len(thisIsaTuple))

thisIsmysecondTuple=(1,3,4,10,22,5)
print(max(thisIsmysecondTuple))
print(min(thisIsmysecondTuple))
print(sum(thisIsmysecondTuple))

thisThirdTuple = thisIsaTuple + thisIsmysecondTuple
print(thisThirdTuple)

thisIsDict = {
    "maker":"Dell",
    "color":"gray",
    "year":2005,
    "price":500
}
print(thisIsDict)
print(thisIsDict["color"])

thisIsDict["maker"] = "Asus"
print(thisIsDict)
