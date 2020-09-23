from collections import deque

# # 1차원 bfs
# def bfs(graph, start):
#     q = deque()
#     visit = list()
#     q.append(start)
#     while q:
#         node = q.pop(0)

#         if node not in visit:
#             visit.append(node)
#             # q.append(graph(node))
#             q.extend(graph(node))

#     return visit


#  2차원 bfs
import sys
from collections import deque

sys.stdin = open("./input.txt", "r")
n, m, = list(map(int, sys.stdin.readline().split()))
graph = []
visit = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(n):
    tmp_lst = list(map(int, sys.stdin.readline().strip()))
    graph.append(tmp_lst)

start = (0, 0)


def bfs(graph, start, visit):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque()
    q.append((start, 1))
    while q:
        node, cost = q.popleft()
        x = node[0]
        y = node[1]
        visit[x][y] = 1
        if x == n - 1 and y == m - 1:
            return cost
        for i in range(4):
            nx = node[0] + dx[i]
            ny = node[1] + dy[i]
            if nx < 0 or nx >= n:
                continue
            if ny < 0 or ny >= m:
                continue
            elif visit[nx][ny] == 0 and graph[nx][ny] == 1:
                q.append(((nx, ny), cost + 1))
                visit[nx][ny] = 1


print(bfs(graph, start, visit))

