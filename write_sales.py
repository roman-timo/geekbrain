import sys

start = int(sys.argv[1])
sale = str(sys.argv[2])

with open('bakery.csv', 'r', encoding='utf-8') as f:
    with open('temp_bakery.csv', 'w', encoding='utf-8') as f2:
        for tup_line in enumerate(f):

            if tup_line[0] == start - 1:
                f2.writelines(f'{sale}\n')
            else:
                f2.writelines(tup_line[1])

with open('temp_bakery.csv', 'r', encoding='utf-8') as f:
    with open('bakery.csv', 'w', encoding='utf-8') as f2:
        for line in f:
            f2.writelines(line)

