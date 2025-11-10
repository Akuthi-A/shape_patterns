def triangle(height):

    for row in range(1, height + 1):
        for height in range(1, row + 1):
            if row >= height:
                print("*", end=" ")
        print()



print(triangle(height=10))