for x in range(2, 13):
    for y in range(1, 13):
        print(f'{x} x {y} = {x * y}', file="timestable.txt")
    print('==============================')

print("Done")