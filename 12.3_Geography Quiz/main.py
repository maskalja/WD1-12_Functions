import random
count = 0

capitals = {"Slovenia": "Ljubljana", "Austria": "Vienna", "Hungary": "Budapest", "USA": "Washington"}
countries = ["Slovenia", "Austria", "Hungary", "USA"]

for country in countries:
    count += 1

r = random.randint(0, count-1)

answer = input(f"What is the capital of {countries[r]}? ")
if answer.lower() == capitals[countries[r]].lower():
    print("Correct answer!")
else:
    print("Wrong answer!")