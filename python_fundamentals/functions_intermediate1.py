import random
def randInt(min=0,max=100):
    num = random.random() *(max-min) + min
    num = round(num)
    return num

print(randInt())
print(randInt(max = 20))
print(randInt(min=10, max=35))
print(randInt(min =75))