sum = 0
f = open('Dec 1/input.txt', 'r')
valid_nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
valid_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for line in f:
    line2 = ["" for i in range(len(line))]
    
    for i, num in enumerate(valid_nums):
        if num in line:
            line2[line.index(num)] = str(i)
            line2[line.rindex(num)] = str(i)

    for i, num in enumerate(valid_numbers):
        if num in line:
            line2[line.index(num)] = str(i)
            line2[line.rindex(num)] = str(i)
    line = "".join(line2)

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
    print(num)

print(sum)
