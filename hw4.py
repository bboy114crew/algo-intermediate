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
#     '''
#     openings = []

#     longest_length = 0
#     paired = 0
#     i = 0
#     while i < n:
#       if case[i] == '<':
#         openings.append('<')
#       else:
#         if len(openings) == 0: # cannot find any '<' on the left to pair with this '>' -> this prefix is INVALID no matter what's behind.
#           break
#         else:
#           # pair the latest '<' with this '>'.
#           openings.pop()
#           paired += 1

#           # when all '<' is paired -> the stack is empty -> we know the current prefix is VALID -> the longest VALID prefix should at least contain this current prefix.
#           if len(openings) == 0:
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
