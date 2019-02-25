with open('stdin', 'r') as fi:
    l = []
    for line in fi:
        l.append(line.strip())

n = len(l)


def compare_nums(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return a[i] < b[i]
    return len(a) > len(b)


for _ in range(n-1):
    for i in range(n-1):
        if compare_nums(l[i], l[i+1]):
            l[i], l[i+1] = l[i+1], l[i]

with open('stdout', 'w') as fo:
    print(''.join(l), file=fo)
