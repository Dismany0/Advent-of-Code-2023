sum = 0
f = open('Dec 2/input.txt', 'r')
for line in f:
    data = line[line.index(':') + 1:].split(";")

    maxred, maxgreen, maxblue = 0, 0, 0

    for showing in data:
        balls = showing.split(",")
        red, green, blue = 0, 0, 0
        for ball in balls:
            if "red" in ball:
                red += int(ball.split()[0])
            if "green" in ball:
                green += int(ball.split()[0])
            if "blue" in ball:
                blue += int(ball.split()[0])
        if red > maxred:
            maxred = red
        if green > maxgreen:
            maxgreen = green
        if blue > maxblue:
            maxblue = blue

    sum += maxred * maxgreen * maxblue
print(sum)
