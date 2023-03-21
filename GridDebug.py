'''
Grid Debug
Pawelski
3/21/2023
Python II
'''

def draw_grid(width, height):
    '''
    Draws a grid with a given width and height.
    '''
    for i in range(height):
        for j in range(width * 2):
            print("-", end="")
        print()
        for j in range(width + 1):
            print("| ", end="")
        for i in range(width * 2):
            print("-", end="")
    print()


repeat = "y"
while repeat == "y":
w = int(input("What is the width of the grid? >> "))
    h = int(input("What is the height of the grid? >> "))
    draw_grid(h, w)
    repeat = input("Would you like to draw another grid? (y/n) >> ")
    print()
