def starbox(width, height, symbol='*'):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    for i in range(height):
        if i==0 or i==height-1:
            print((symbol+" ") * width) #print top edge of box
        else:
            print(symbol+" "+ "  " * (width-2) +symbol)

# Test Cases
print("Test 1:")
starbox(5, 5,'$')

print("Test 2:")
starbox(8, 10)

