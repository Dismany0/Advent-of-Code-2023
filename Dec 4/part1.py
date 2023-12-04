sum = 0
f = open('Dec 4/input.txt', 'r')
for line in f:
    data = line[line.index(":")+1:]
    winning_numbers, my_numbers = data.split("|")
    winning_numbers = [int(x.strip()) for x in winning_numbers.split()]
    my_numbers = [int(x.strip()) for x in my_numbers.split()]

    matches = 0
    for number in my_numbers:
        if number in winning_numbers:
            matches += 1

    if matches == 0:
        sum += 0
    else:
        sum += 2 ** (matches - 1)
print(sum)
