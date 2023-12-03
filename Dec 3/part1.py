sum = 0
f = open('Dec 3/input.txt', 'r')
data = []
for line in f:
    #split line into list of characters
    data.append(list(line))
f.close()

gears = [[0 for x in range(len(data[y]))] for y in range(len(data))]

def search_around(x, y, length, data, num):
    foundSymbol = False
    #print around the number
    for ys in range(-1, 2):
        if y+ys < len(data) and y+ys >= 0:
            for xs in range(-1, length+1):
                if x+xs < len(data[y+ys]) and x+xs >= 0:
                    if not data[y+ys][x+xs].isdigit() and data[y+ys][x+xs] != "." and data[y+ys][x+xs] != "\n":
                        foundSymbol = True

                        if data[y+ys][x+xs] == "*":
                            
                            if isinstance(gears[y+ys][x+xs], int):
                                
                                if gears[y+ys][x+xs] == 0:
                                    gears[y+ys][x+xs] = -int(num)    
                                elif gears[y+ys][x+xs] < 0:
                                    gears[y+ys][x+xs] *= -int(num)                              
                                else:
                                    gears[y+ys][x+xs] = "N/A"                
    return foundSymbol

for y, line in enumerate(data):
    num = ""
    for x, char in enumerate(line):
        if char.isdigit():
            num += char
        else:
            if num != "":
                if search_around(x - len(num), y, len(num), data, num):
                    sum += int(num)
                    # print(num, end=" ")
                num = ""
mult = 0
for value in gears:
    for value2 in value:
        if value2 != "N/A" and value2 >= 0:
            mult += gears[gears.index(value)][value.index(value2)]

print(sum)
print(mult)
