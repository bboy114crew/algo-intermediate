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

# Street Parade
def street_parade(cases):
  for case in cases:
    a = case["a"]
    n = case["n"]
    stack = []
    sorted_stack = []
    n_sorted = sorted(a)
    car_sorted_index = 0
    for i in range(n):
      if (a[i] == n_sorted[car_sorted_index]):
        if (len(stack) == 0):
          sorted_stack.append(a[i])
          car_sorted_index += 1
        else:
          sorted_stack.append(a[i])
          len_stack = len(stack)
          while (len_stack > 0):
            if (stack[len_stack - 1] == n_sorted[car_sorted_index] + 1):
              sorted_stack.append(stack.pop())
              car_sorted_index += 1
              len_stack -= 1
            else:
              break
          car_sorted_index += 1
      else:
        stack.append(a[i])

    for j in range(len(stack)):
      sorted_stack.append(stack.pop())

    can_sort = True

    for index in range(n):
      if (n_sorted[index] != sorted_stack[index]):
        can_sort = False
        break
    if (can_sort):
      print('yes')
    else:
      print('no')
# Input
cases = []
n = 1
while (True):
  n = int(input())
  if (n == 0):
    break
  else:
    case = {}
    a = list(map(int, input().split()))
    case["n"] = n
    case["a"] = a
    cases.append(case)

# Run and get output
street_parade(cases)