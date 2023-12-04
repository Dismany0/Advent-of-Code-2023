sum = 0
f = open('Dec 4/input.txt', 'r')

# 1 for number of lines in file
repeatArray = [1 for line in f]
f.close()

f = open('Dec 4/input.txt', 'r')

for i, line in enumerate(f):
    print(i)
    data = line[line.index(":")+1:]
    winning_numbers, my_numbers = data.split("|")
    winning_numbers = [int(x.strip()) for x in winning_numbers.split()]
    my_numbers = [int(x.strip()) for x in my_numbers.split()]

    copies = repeatArray[i]
    matches = 0
    for number in my_numbers:
        if number in winning_numbers:
            matches += 1
    
    for next in range(matches):
        repeatArray[i + next + 1] += copies

    sum += copies



print(sum)
