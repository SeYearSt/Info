f = open('res.txt', 'w')

for i in range(100000000):
    i = str(i)
    count = len(i)
    for j in range(8-count):
        f.write('0')
    f.write(i)
    f.write('\n')

f.close()
