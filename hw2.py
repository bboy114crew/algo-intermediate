# Books
# def books(n, t, books_time):
#   i = 0
#   j = 0
#   books_time_len = len(books_time)
#   max_book = 0
#   current_sum = 0

#   for j in range(books_time_len):
#     current_sum += books_time[j]
#     while(current_sum > t):
#       current_sum -= books_time[i]
#       i += 1
#     max_book = max(max_book, j - i + 1)



#   print(max_book)

# # Input
# nt = list(map(int, input().split()))
# n = nt[0]
# t = nt[1]
# books_time = list(map(int, input().split()))

# # Run and get output
# books(n, t, books_time)

# George and Round
# def george_and_round(n, m, a, b):
#   i = 0
#   j = 0
#   while (i < n and j < m):
#     if (b[j] >= a[i]):
#       i = i + 1
#     j = j + 1
#   result = n - i
#   print(result)

# # Input
# nm = list(map(int, input().split()))
# n = nm[0]
# m = nm[1]
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# # Run and get output
# george_and_round(n, m, a, b)

# Dress'em in Vests!
# def dressem_in_vests(n, m, x, y, a, b):
#   i = 0
#   j = 0
#   results = []
#   while (i < n and j < m):
#     if (b[j] < a[i] - x):
#       j += 1
#     elif (b[j] > a[i] + y):
#       i += 1
#     else:
#       results.append([i, j])
#       i += 1
#       j += 1
#     # Wrong approach
#     # Because if b[j] < a[i] - x maybe b[j + 1] >= a[i] - x

#     # if (a[i] - x  <= b[j] and b[j] <= a[i] + y):
#     #   results.append([i, j])
#     #   i += 1
#     #   j += 1
#     # else:
#     #   i += 1

#   print(len(results))
#   for result in results:
#     print(str(result[0] + 1) + " " + str(result[1] + 1))


# # Input
# nmxy = list(map(int, input().split()))
# n = nmxy[0] # the number of soldiers
# m = nmxy[1] # the number of vests
# #  [x, y]
# x = nmxy[2]
# y = nmxy[3]
# a = list(map(int, input().split())) # the desired sizes of vests
# b = list(map(int, input().split())) # the sizes of the available vests

# # Run and get output
# dressem_in_vests(n, m, x, y, a, b)

# Array
def array(n, k, a):
  i = 0
  j = 0

# Input
nk = list(map(int, input().split()))
n = nk[0] # the number of positive number
k = nk[1] # the number of distinct number
#  [x, y]
a = list(map(int, input().split())) # the positive numbers

# Run and get output
array(n, k, a)