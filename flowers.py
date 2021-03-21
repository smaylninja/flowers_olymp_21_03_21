
f = open('input.txt', 'r')

fl = list(map(float, f.read().split(' ')))

f.close()

minimum = min(fl[0] + fl[1], fl[2] + fl[3])

f = open('output.txt', 'w')
if (fl[1] + fl[3] >= minimum):
    f.write('no')
else:
    f.write('yes')