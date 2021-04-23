from collections import defaultdict

V, E = list(map(int, input().split()))
adj = defaultdict(list)
for _ in range(E):
	a, b, c = list(map(int, input().split()))
	adj[a].append((c, b))
	adj[b].append((c, a))

INF = float('inf')
distances = [INF] * (V + 1)
distances[1] = 0
visit = [False] * (V + 1)
ans = 0
for _ in range(V):
	min_index = -1
	min_value = INF

	for i in range(1, V + 1):
		if not visit[i] and distances[i] < min_value:
			min_index = i
			min_value = distances[i]

	visit[min_index] = True
	ans += min_value

	for weight, node in adj[min_index]:
		if not visit[node] and weight < distances[node]:
			distances[node] = weight
print(ans)
