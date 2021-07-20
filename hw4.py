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