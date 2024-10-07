'''
Brick Builder
Sidonia Stanton
10/3/24
'''

'''
*** DELETE BEFORE SENDING ***

1. standard triangle - input # to get base size

2. upside down triangle - same thing but # is top size

3. ramp - standard triangle that aligns right

4. wedge - upside down triangle that aligns right

5. pyramid - similar to ramp - not increasing x by 1 every time bc input # is number of rows

6. empty square - hollow square - input # is base x height 

'''
userInput = int(input('Please enter a number: '))

'''
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
'''

#   F I X
# pyramid - WIP - use multiple loops - x increase by 2 each time - dont have to include spaces on right
for row in range(userInput): # for each horiz row in the range of user input # -- establush number of rows
    for col in range(userInput - row - 1): # for each row - for each column of O's print single o
        print(" ", end='')
    for col in range(row * 2 + 1): # for each column of x print single x
        print ("x", end='')
    print()

#  add 2 every row - row * 2 + 1
print()

