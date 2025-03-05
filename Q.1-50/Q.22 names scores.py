import math
import time
start=time.time()

# Read the names from the file
with open('names.txt', 'r') as file:
    names = file.read().replace('"', '').split(',')

names.sort()

alphabetical_value = lambda name: sum(ord(char)-ord("A")+1 for char in name)
total_score = sum((i + 1) * alphabetical_value(name) for i, name in enumerate(names))

print(total_score)

stop=time.time()
print(stop-start)
