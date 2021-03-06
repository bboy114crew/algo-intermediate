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

# # CamelCase
# english_string = str(input())

# number_of_word = 0
# # a -> z 97 -> 122
# for i in range(len(english_string)):
#   if i == 0:
#     if ord(english_string[i]) >= 97 and ord(english_string[i]) <= 122:
#       number_of_word += 1
#   else:
#     if ord(english_string[i]) >= 65 and ord(english_string[i]) <= 90:
#       number_of_word += 1

# print(number_of_word)

# Word Transformation
import queue
def BFS(s, f):
  q = queue.Queue()
  q.put(s)
  dist[s] = 0

  while not q.empty():
    u = q.get()

    for v in graph[u]:
      if dist[v] == -1:
        dist[v] = dist[u] + 1
        q.put(v)

        if v == f:
          return

n = int(input())
input()
while n > 0:
  n -= 1
  dict = []

  while True:
    word = input()
    if word == '*':
      break
    dict.append(word)

  len_dict = len(dict)

  graph = [[] for _ in range(len_dict)]
  '''
  L??u la??i t????t ca?? ca??c t???? co?? trong t???? ??i????n.
  Ta xem m????t t???? trong t???? ??i????n la?? m????t ??i??nh cu??a ?????? thi??.
  Ta se?? ta??o danh sa??ch ca??nh t???? ca??c ??i??nh na??y.
  V????i hai t???? co?? ?????? da??i b????ng nhau va?? kha??c nhau ??u??ng m????t ki?? t????,
  ta se?? th????c hi????n n????i hai ??i??nh ??a??i di????n cho hai t???? na??y la??i.
  '''
  for u in range(len_dict - 1):
    for v in range(u + 1, len_dict):
      if len(dict[u]) == len(dict[v]):
        count = 0
        for i in range(len(dict[u])):
          if dict[u][i] != dict[v][i]:
            count += 1
        if count == 1:
          graph[u].append(v)
          graph[v].append(u)
  while True:
    try:
      line = input()
      if line == '':
        break
    except EOFError:
      break

    sWord, fWord = line.split()
    s = dict.index(sWord)
    f = dict.index(fWord)
    dist = [-1] * len_dict
    BFS(s, f)
    print('{} {} {}'.format(sWord, fWord, dist[f]))
