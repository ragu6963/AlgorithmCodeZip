# 2차원 DFS
import sys
sys.stdin = open("./input.txt", "r")
n = int(input())
graph = []
for i in range(n):
    tmp = list(map(int, input()))
    graph.append(tmp)

visit = [[0 for _ in range(n)] for _ in range(n)]
start = (0, 0)


def dfs(graph, visit, start, index):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        x = node[0]
        y = node[1]
        visit[x][y] = index
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx == n:
                continue
            if ny < 0 or ny == n:
                continue
            if visit[nx][ny] != 0:
                continue
            if graph[nx][ny] == 1:
                next_node = (nx, ny)
                stack.append(next_node)


index = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visit[i][j] == 0:
            dfs(graph, visit, (i, j), index)
            index += 1

value_dict = {}
for row in visit:
    for v in row:
        if v == 0:
            continue
        if v in value_dict:
            value_dict[v] += 1
        else:
            value_dict[v] = 1

value_dict = sorted(value_dict.items(), key=lambda x: x[1])
print(len(value_dict))
for k, v in value_dict:
    print(v)
