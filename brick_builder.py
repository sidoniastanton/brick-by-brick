'''
Brick Builder
Sidonia Stanton
10/3/24

Please disregard my notes. I'm keeping them in case I need to come back and see how I did something.
'''

userInput = int(input('Please enter a number: '))


# standard triangle
for row in range(userInput):
    for col in range(row + 1):
        print("x", end='')
    print()

print()

# upside down triangle
for row in range(userInput):
    for col in range(userInput - row):
        print("x", end='')
    print()

print()
# ramp
for row in range(userInput):
    for col in range(userInput - row - 1):
        print(" ", end='')
    for col in range(row + 1):
        print ("x", end='')
    print()

print()

# wedge
for row in range(userInput):
    for col in range(row + 1):
        print(" ", end='')
    for col in range(userInput - row):
        print("x", end='')
    print()

print()



# pyramid - x increase by 2 each time - dont have to include spaces on right
for row in range(userInput): # for each horiz row in the range of user input # -- establush number of rows
    for col in range(userInput - row - 1): # for each row - for each column of O's print single o
        print(" ", end='')
    for col in range(row * 2 + 1): # for each column of x print single x
        print ("x", end='')
    print()

#  add 2 every row - row * 2 + 1
print()

for row in range(userInput):
    for col in range(userInput):
        print(" ", end='')
        if(row==0 or row==userInput-1 or col==0 or col==userInput-1):
            print('x', end='')
        else:
            print(" ", end='')
    print()
   