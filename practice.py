# colors = ['red', 'green', 'blue']

# # Get the length of the list
# print(len(colors))

# idx = 1
# print(colors[-1])

# colors[-1] = 'brown'
# print(colors)

# colors.append('purple')
# print(colors)

# colors.extend(['yellow', 'silver'])

# print(colors)

# colors.insert(1,'orange')

# print(colors)

# green = colors.pop(2)
# print(colors)

# del colors[1]
# print(colors)

# colors.remove('red')
# print(colors)

# colors.clear()
# print(colors)

# colors = ['red', 'green', 'blue']

# for color in colors:
#     print(color)
    
# for idx, color in enumerate(colors):
#     print(idx, colod

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # even_squares = []
# # for n in nums:
# #         square = n * n
# #         if square % 2 == 0:
# #             even_squares.append(square)
# # print(even_squares)

# even_squares =[n *n for n in nums if (n*n) % 2 ==0]
# print(even_squares)

# colors = ('red', 'green', 'blue');
# green = colors[1];
# print(green)

# blue_idx = colors.index('blue')
# print(blue_idx)

# for idx, color in enumerate(colors):
#     print(idx, color)
    
    
# colors = ('red', 'green', 'blue')
# red, green, blue = colors
# print(red, green, blue) 

for even in range (2,10, 2):
    print(even)
    
nums = list(range(10))

print(nums)

odds = tuple(range(1, 10, 2))

print(odds)

for num in range(5, 0, -1):
    print(num)

short_name = 'Alexendria'[0:4]
print(short_name)

colors = ('red', 'green','blue')
print( colors[:2])

print(colors[1:])

fruit = ('apples', 'bananas', 'oranges')
fruit_copy = fruit[:]
print(fruit_copy)