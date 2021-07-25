# Breadth First Search: Shortest Reach
q = int(input())

def bfs_shortest_reach(q):
  for i in range(q):
    nm = list(map(int, input().split()))
    n = nm[0]
    m = nm[1]

    visited = [False] * (n + 1)
    dist = [-1] * (n + 1)

    adj_list = [[]] * (n + 1)

    for j in range(m):
      edge = list(map(int, input().split()))
      adj_list[edge[0]].append(edge[1])
      adj_list[edge[1]].append(edge[0])
    
    start = int(input())

    dist[start] = 0

    



