import datetime
import math
import random

randomNumber = random.randint(0,10)
print(randomNumber)
randomPopulation = random.sample(range(10000000), 60)
print(randomPopulation)

Current = datetime.datetime.now()
print(Current)

print(Current.strftime("%a"))
print(Current.strftime("%H"))
print(Current.strftime("%p"))
print(Current.strftime("%Z"))
print(Current.strftime("%j"))


