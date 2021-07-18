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

# chores
def chores(n, a, b, h):
  h.sort()

  l = 0
  r = n - 1

  while (l < b - 1):
    l +=1

  while (n - r < a):
    r -= 1

  if (l < r):
    print(h[r] - h[l])
  else:
    print(0)

# Input
nab = list(map(int, input().split()))
n = nab[0]
a = nab[1]
b = nab[2]
h = list(map(int, input().split()))

# Run and get output
chores(n, a, b, h)