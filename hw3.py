# # Devu, the Dumb Guy
# def devu_the_dumb_guy(n, x, c):
#   c.sort()
#   sum = 0
#   for num in c:
#     sum += num * x
#     if (x > 1):
#       x -= 1
#   print(sum)

# # Input
# nx = list(map(int, input().split()))
# n = nx[0]
# x = nx[1]
# c = list(map(int, input().split()))

# # Run and get output
# devu_the_dumb_guy(n, x, c)

# # Chores
# def chores(n, a, b, h):
#   h.sort()

#   l = 0
#   r = n - 1

#   while (l < b - 1):
#     l +=1

#   while (n - r < a):
#     r -= 1

#   if (l < r):
#     print(h[r] - h[l])
#   else:
#     print(0)

# # Input
# nab = list(map(int, input().split()))
# n = nab[0]
# a = nab[1]
# b = nab[2]
# h = list(map(int, input().split()))

# # Run and get output
# chores(n, a, b, h)

# Sort the Array
def sort_the_array(n, a):
  is_sorted = True

  for i in range(n - 1):
    if (a[i] > a[i + 1]):
      is_sorted = False
      break
  if (is_sorted):
    print("yes")
    print(1, 1)
    return
  else:
    l = 0
    r = n - 1
    if (n == 2):
      print("yes")
      print(l + 1, r + 1)
      return

    flag = 0

    for i in range(n - 1):
      if (a[i] > a[i + 1]):
        l = i
        break
    for i in range(n - 1, 0, -1):
      if (a[i] < a[i - 1]):
        r = i
        break
    # print(l, r)

    first = []
    first = a[0:l:1]
    # print('first:', first)

    reversed = a[l:r+1:1]
    reversed = reversed[::-1]
    # print('reversed:', reversed)

    last = []
    last = a[r + 1:n:1]
    # print('last', last)

    final = [*first, *reversed, *last]

    for i in range(n - 1):
      if (final[i] > final[i + 1]):
        flag = 1
        break
    if (flag):
      print("no")
    else:
      print("yes")
      print(l + 1, r + 1)

# Input
n = int(input())
a = list(map(int, input().split()))

# Run and get output
sort_the_array(n, a)