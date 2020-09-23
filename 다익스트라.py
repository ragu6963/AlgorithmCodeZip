# 다익스트라
import heapq
import sys


def Solve():
    input = sys.stdin.readline
    INF = int(1e9)
    n, m, start = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # i는 현재 노드와 인접한 다른 노드들
        # i[0]은 다른 노드 번호
        # i[1]은 다른 노드로 가는 비용
        for i in graph[now]:
            # cost는 현재 노드까지 비용 + 다음 노드로 가는 비용
            cost = dist + i[1]
            # 기존 비용 보다 cost(현재 노드까지 비용 + 다음 노드로 가는 비용) 가 작을 때
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    city = 0
    cost = 0
    for i in distance:
        if i != INF:
            city += 1
            cost = max(cost, i)
    print(city - 1, cost)


if __name__ == "__main__":
    Solve()

