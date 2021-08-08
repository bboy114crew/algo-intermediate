# # Printer Queue
# from heapq import heappush, heappop

# t = int(input())

# for _ in range(t):
#   # n is the number of jobs in the queue
#   # m is the position of your job
#   n, m = list(map(int, input().split()))

#   # the priorities of the jobs in the queue
#   jobs_priorities = list(map(int, input().split()))
#   job = []
#   h = []
#   time = 0
#   for i in range(n):
#     heappush(h, (-jobs_priorities[i], i))
#     job.append((jobs_priorities[i], i))
  
#   while len(job):
#     if (job[0][0] != -h[0][0]):
#       top = job.pop(0)
#       job.append(top)
#     else:
#       time += 1
#       heappop(h)
#       top = job.pop(0)
#       if top[1] == m:
#         break

#   print(time)

# # Pangram
# n = int(input())

# str = str(input())

# lower_string = str.lower()

# dict_char = {
# }

# for char in lower_string:
#   if char not in dict_char:
#     dict_char[char] = 0
#   else:
#     dict_char[char] += 1

# number_of_char = len(dict_char)

# if number_of_char == 26:
#   print('YES')
# else:
#   print('NO')

# # Soldier and Bananas
# k, n, w = list(map(int, input().split()))
# total_money_he_need = 0

# for i in range(w):
#   total_money_he_need += (i + 1) * k

# result = total_money_he_need - n

# if result <= 0:
#   print(0)
# else:
#   print(result)

# # Find The Median
# n = int(input())
# a = list(map(int, input().split()))

# median = 0

# a.sort()

# x = n // 2

# if n % 2 == 0:
#   median = (a[x] + a[x - 1]) / 2
# else:
#   median = a[x]

# print(median)

# # Bombs! NO they are Mines!!
# import queue

# def bombs(m, n, start, end, matrix):
#   sx, sy = start
#   ex, ey = end
#   dis = [[-1 for j in range(n)] for i in range(m)]
#   dis[sx][sy] = 0
#   # queue for store current point
#   q = queue.Queue()
#   q.put((sx, sy))
#   while not q.empty():
#     x, y = q.get()
#     # points right arround current point
#     arrounds = []
#     arrounds.append((x + 1, y))
#     arrounds.append((x, y + 1))
#     arrounds.append((x - 1, y))
#     arrounds.append((x, y - 1))

#     for arround in arrounds:
#       a_x, a_y = arround
#       # check if point inside matrix
#       if (a_x >= 0 and a_y >= 0 and a_x < m and a_y < n):
#         # check if point not visited and is posible move
#         if dis[a_x][a_y] == -1 and matrix[a_x][a_y] == False:
#           dis[a_x][a_y] = dis[x][y] + 1
#           if a_x == ex and a_y == ey:
#             print(dis[ex][ey])
#             return
#           q.put(arround)

# while True:
#   r, c = list(map(int, input().split()))
#   if r == 0 and c == 0:
#     break
#   rows = int(input())
#   matrix = [[False for index in range(c)] for index in range(r)]
#   for _ in range(rows):
#     data = list(map(int, input().split()))
#     u = data[0]
#     v = data[1]
#     for i in range(2, len(data)):
#       matrix[u][data[i]] = True
#   start = list(map(int, input().split()))
#   start = (start[0], start[1])
#   end = list(map(int, input().split()))
#   end = (end[0], end[1])
#   result = 1
#   bombs(r, c, start, end, matrix)
