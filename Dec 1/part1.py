sum = 0
f = open('Dec 1/input.txt', 'r')

for line in f:
    num = ""
    for char in line:
        if char.isdigit():
            num += char
            break
    for char in reversed(line):
        if char.isdigit():
            num += char
            break
    sum += int(num)
print(sum)

