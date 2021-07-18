# Devu, the Dumb Guy
def devu_the_dumb_guy(n, x, c):
  c.sort()
  sum = 0
  for num in c:
    sum += num * x
    if (x > 1):
      x -= 1
  print(sum)

# Input
nx = list(map(int, input().split()))
n = nx[0]
x = nx[1]
c = list(map(int, input().split()))

# Run and get output
devu_the_dumb_guy(n, x, c)