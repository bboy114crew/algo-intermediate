import queue

# # Transform the Expression
# def transform_the_expression(n, expressions):
#   result = []
#   stack = []
#   for expression in range(len(expressions)):
#     s = ''
#     for index in range(len(expressions[expression])):
#       current = expressions[expression][index]
#       if (current.isalpha()):
#         s += current
#       elif (current == ')'):
#         s += stack[-1]
#         stack.pop()
#       elif (current != '('):
#         stack.append(current)
#     result.append(s)

#   for string in range(len(result)):
#     print(result[string])

# # Input
# n = int(input())
# expressions = []
# for i in range(n):
#   expression = str(input())
#   expressions.append(expression)

# # Run and get output
# transform_the_expression(n, expressions)

# # Street Parade
# def street_parade(cases):
#   for case in cases:
#     a = case["a"]
#     n = case["n"]
#     stack = []
#     sorted_stack = []
#     n_sorted = sorted(a)
#     car_sorted_index = 0
#     for i in range(n):
#       if (a[i] == n_sorted[car_sorted_index]):
#         if (len(stack) == 0):
#           sorted_stack.append(a[i])
#           car_sorted_index += 1
#         else:
#           sorted_stack.append(a[i])
#           len_stack = len(stack)
#           while (len_stack > 0):
#             if (stack[len_stack - 1] == n_sorted[car_sorted_index] + 1):
#               sorted_stack.append(stack.pop())
#               car_sorted_index += 1
#               len_stack -= 1
#             else:
#               break
#           car_sorted_index += 1
#       else:
#         stack.append(a[i])

#     for j in range(len(stack)):
#       sorted_stack.append(stack.pop())

#     can_sort = True

#     for index in range(n):
#       if (n_sorted[index] != sorted_stack[index]):
#         can_sort = False
#         break
#     if (can_sort):
#       print('yes')
#     else:
#       print('no')
# # Input
# cases = []
# n = 1
# while (True):
#   n = int(input())
#   if (n == 0):
#     break
#   else:
#     case = {}
#     a = list(map(int, input().split()))
#     case["n"] = n
#     case["a"] = a
#     cases.append(case)

# # Run and get output
# street_parade(cases)

# # Throwing Cards Away I
# def throwing_cards_away_i(cases):
#   for n in cases:
#     stack = []
#     discarded = []
#     for i in range(n - 1, -1, -1):
#       stack.append(i)

#     while (len(stack) > 1):
#       top = stack.pop()
#       nextTop =  stack.pop()
#       discarded.append(top + 1)
#       stack.insert(0, nextTop)

#     remaining = stack[0] + 1
#     if (len(discarded) == 0):
#       print('Discarded cards:')
#     else:
#       print('Discarded cards:', ', '.join(str(dis) for dis in discarded))
#     print('Remaining card:', remaining)

# # Input
# cases = []
# n = 1
# while (True):
#   n = int(input())
#   if (n == 0):
#     break
#   else:
#     cases.append(n)

# # Run and get output
# throwing_cards_away_i(cases)

# # That is Your Queue
# def that_is_your_queue(cases):
#   t = 0
#   p = 1
#   c = 1

#   for index in range(len(cases)):
#     p = cases[index]["p"]
#     c = cases[index]["c"]
#     n = cases[index]["n"]
#     case_title = 'Case ' + str(index + 1) + ':'
#     print(case_title)
#     my_queue = []
#     for i in range(min(int(p), int(c))):
#       my_queue.append(str(i + 1))
#     for command in n:
#       if (command == "N"):
#         current = my_queue[0]
#         print(current)
#         my_queue.pop(0)
#         my_queue.append(current)
#       else:
#         current = command.split()[1]
#         if (current in my_queue):
#           my_queue.remove(current)
#         my_queue.insert(0, current)

# # Input
# cases = []

# while True:
#   pc = str(input()).split()
#   p = pc[0]
#   c = pc[1]

#   if (p == '0' and c == '0'):
#     break
#   else:
#     case = {}
#     case["p"] = p
#     case["c"] = c
#     commands = []
#     for i in range(int(c)):
#       command = input()
#       commands.append(command)
#     case["n"] = commands
#     cases.append(case)

# # Run and get output
# that_is_your_queue(cases)

# # Compilers and Parsers
# def compilers_and_parsers(n, cases):
#   for case in cases:
#     n = len(case)

#     '''
#     key points:
#       - every '<' inside a VALID prefix MUST be paired with a '>' which is (i) inside THIS prefix and (ii) on the right of this '<'.
#         => "<<>" is not a valid prefix, however "<<>>" or "<><>" is.
#         => from this definition, we can know that a prefix is not valid whenever we encounter a '>' and cannot pair this '>' with any '<' on the left.
#         => we will use a stack to store every '<' we encounter, if this stack is pushed with some '<' and later is empty, we know that at that point, the current prefix is still valid.

#     some test cases:
#     <<>> => 4
#     <><> => 4
#     <<<> => 0
#     <<><<>> => 0
#     Because all item in stack is '<' so instead of store all '<' in stack we just increase number of 'v'
#     '''
#     openings = 0

#     longest_length = 0
#     paired = 0
#     i = 0
#     while i < n:
#       if case[i] == '<':
#         openings += 1
#       else:
#         if openings == 0: # cannot find any '<' on the left to pair with this '>' -> this prefix is INVALID no matter what's behind.
#           break
#         else:
#           # pair the latest '<' with this '>'.
#           openings -= 1
#           paired += 1

#           # when all '<' is paired -> the stack is empty -> we know the current prefix is VALID -> the longest VALID prefix should at least contain this current prefix.
#           if openings == 0:
#             longest_length += paired * 2
#             paired = 0 # reset this counter to 0 to start finding the next potential substring, which might not exist, of the longest VALID prefix.
#       i += 1

#     print(longest_length)

# # Input
# n = int(input())
# cases = []
# for i in range(n):
#   case = str(input())
#   cases.append(case)

# # Run and get output
# compilers_and_parsers(n, cases)

# Processing Queries
# def processing_queries(n, b, tds):
#   q = queue.Queue()
#   processing = 0

#   '''
#   queue processing
#   if t the moment of time when the query appears >= front of queue => dequeue this
#   repeat above action till queue processing empty

#   if can dequeue any processing and queue size <= max queue capacity
#   print time excute of query

#   processing = processing + d

#   and enqueue this processing

#   if queue full i can't dequeue any processing => print -1

#   '''

#   for i in range(n):
#     td = tds[i].split()

#     t = int(td[0])
#     d = int(td[1])

#     while (q.qsize() != 0 and t >= q.queue[0]):
#       q.get()

#     if (q.qsize <= b):
#       processing = max(t, processing) + d
#       q.put(processing)
#       print(processing)
#     else:
#       print(-1)


# # Input
# nb = list(map(int, input().split()))
# n = nb[0]
# b = nb[1]
# tds = []
# for i in range(n):
#   td = str(input())
#   tds.append(td)

# # Run and get output
# processing_queries(n, b, tds)

# Ferry Loading III
class Car:
  def __init__(self, _id, _arrival_time):
    self.id = _id
    self.arrival_time = _arrival_time

def ferry_loading_iii(c, cases):
  for j in range(c):
    n = cases[j]['n']
    t = cases[j]['t']
    m = cases[j]['m']
    cars_arrival_time = cases[j]['cars']

    car_side = [[] , []]
    car_side[0] = queue.Queue()
    car_side[1] = queue.Queue()

    res = [0] * 10005

    for i in range(m):
      arrived, at_bank = cars_arrival_time[i]
        
      if at_bank == "left":
        car_side[0].put(Car(i, int(arrived)))
      else:
        car_side[1].put(Car(i, int(arrived)))
     
    cur_time, cur_side = 0, 0
    waiting = (not car_side[0].empty()) + (not car_side[1].empty())
     
    while waiting:
      if waiting == 1:
        nextTime = car_side[1].queue[0].arrival_time if car_side[0].empty() else car_side[0].queue[0].arrival_time
      else:
        nextTime = min(car_side[0].queue[0].arrival_time, car_side[1].queue[0].arrival_time)
        
      cur_time = max(cur_time, nextTime)
      
      carried = 0
        
      while not car_side[cur_side].empty():
        car = car_side[cur_side].queue[0]
        if car.arrival_time <= cur_time and carried < n:
          res[car.id] = cur_time + t
          carried += 1
          car_side[cur_side].get()
        else:
          break
        
      cur_time += t
      cur_side = 1 - cur_side
      waiting = (not car_side[0].empty()) + (not car_side[1].empty())
     
    for i in range(m):
      print(res[i])
    
    if j < c - 1:
        print()
      
# Input
c = int(input())

cases = []

for _ in range(c):
  case = {}
  ntm = input().split()
  n = int(ntm[0])
  t = int(ntm[1])
  m = int(ntm[2])
  case['n'] = n
  case['t'] = t
  case['m'] = m
  cars = []
  for j in range(m):
    car_input = input().split()
    car = (int(car_input[0]), car_input[1])
    cars.append(car)
  case['cars'] = cars
  cases.append(case)

# Run and get output
ferry_loading_iii(c, cases)