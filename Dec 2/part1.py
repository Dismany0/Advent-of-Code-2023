sum = 0
gamecounter = 0
f = open('Dec 2/input.txt', 'r')
for line in f:
    gamecounter += 1
    data = line[line.index(':') + 1:]
    data = data.split(";")

    possible = True
    for showing in data:
        balls = showing.split(",")
        red = 0
        green = 0
        blue = 0
        for ball in balls:
            if "red" in ball:
                red += int(ball.split()[0])
            if "green" in ball:
                green += int(ball.split()[0])
            if "blue" in ball:
                blue += int(ball.split()[0])
        if red > 12 or green > 13 or blue > 14:
            possible = False
    
    if possible:
        sum += gamecounter


print(sum)
