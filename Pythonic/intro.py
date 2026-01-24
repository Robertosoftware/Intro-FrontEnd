colors = ["red", "yellow", "blue"]

#Pythonic examples

## List manipulation

# Not pythonic
for i in range(len(colors)):
    print(colors[i])


# pythonic
for color in colors:
    print(color)

for i, color in enumerate(colors):
    print(i,"->",color)


## Value swapping

fruits=["apple","banana"]
f1, f2 = fruits
print(f1)