f = open('out.txt')
line = f.readline()
print line
for i in range(10):
    line = f.readline()
    print line

