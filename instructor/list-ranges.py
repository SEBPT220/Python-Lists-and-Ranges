colors = ['red', 'green', 'blue']


print(len(colors))
idx = 1
print(colors[idx + 1])
print(colors[-1])

colors.append('purple')

print('***************************************************')
print(colors)
print('***************************************************')
# basically the equivalent of adding two arrays
# colors + ['black', 'white']  --> methond(val) -> []
colors.extend(['orange', 'black'])

print(colors)
print('***************************************************')

colors.insert(1, 'yellow')

print(colors)

print('***************************************************')
# IF YOU WANT A COPY OF THE ITEM YOU REMOVE
green = colors.pop(2)
print(colors)
print(green)
print('***************************************************')
# IF YOU WANT TO REMOVE AN ITEM

# DEL operator 0(1)
del colors[1]
print(colors)

print('***************************************************')
#remove method - removes the first occurence of the value
# careful, this is just a hidden find loop ie O(n)
colors.remove('orange')

print(colors)
print('***************************************************')

# Resetting the list to empty
# colors.clear()


# LOOPING LISTS

# for in List - i just want to loop n times, to do something with each item
for color in colors:
  print(color)


print('***************************************************')

# when you need to know the INDEX AND ITEM, use the for in enumareate(list)

for idx, color in enumerate(colors):
  print(idx, color)