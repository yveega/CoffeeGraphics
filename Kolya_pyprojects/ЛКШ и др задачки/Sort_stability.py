with open('stdin', 'r') as fi:
    l = []
    for line in fi:
        l.append(list(map(int, line.split())))

n = l[0][0]
l = l[1:]

for _ in range(n-1):
    for i in range(n-1):
        if l[i][0] > l[i+1][0]:
            l[i], l[i+1] = l[i+1], l[i]

with open('stdout', 'w') as fo:
    for pair in l:
        print(pair[0], pair[1], file=fo)
