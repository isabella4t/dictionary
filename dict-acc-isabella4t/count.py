
def count():
    crayons = {} # an empty crayon dictionary
    with open('crayons', 'r') as f: # opens the file for reading
        for x in f:
            x = x.strip('\n')
            if x in crayons:
                crayons[x] = crayons[x] + 1
            else:
                crayons[x] = 1
    return crayons
print(count()) ## Favorite crayons to eat are Green and Violet
##crayons, wiht 126 green and 131 violet crayons
