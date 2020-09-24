import sys

sys.stdin = open("./input.txt", "r")

n, m = map(int, sys.stdin.readline().split())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i


def findParent(x):
    if parent[x] != x:
        parent[x] = findParent(parent[x])
    return parent[x]


def unionParent(a, b):
    a = findParent(a)
    b = findParent(b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 0:
        unionParent(a, b)

    elif command == 1:
        if findParent(a) == findParent(b):
            print("YES")
        else:
            print("NO")
