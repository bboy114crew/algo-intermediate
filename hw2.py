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
  if k == 1:
    print("1 1")
    return
  l = 0
  r = 0

  count_appear = {}
  for number in a:
    if number in count_appear:
      count_appear[number] += 1
    else:
      count_appear[number] = 1

  distinct_numbers = set()
  array_l_to_r = []

  # Nếu có 5 số 1 liên tiếp ví dụ 1111151 thì l sẽ là 4
  while (l < count_appear[a[0]] and n > 1):
    if (a[0] == a[l + 1]):
      l += 1
    else:
      break
  
  while (l < n and r < n):
    distinct_numbers.add(a[r])

    # Dãy số trong đoạn [l, r]
    if (r >= l):
      array_l_to_r.append(a[r])

    r += 1

    # Cho đến khi có đủ k số riêng biệt trong đoạn [l, r]
    if (len(distinct_numbers) == k):
      while (l < r):
        copy_array = [*array_l_to_r]
        copy_array.remove(a[l])
        # Nếu sau khi remove a[l] khỏi array trong đoạn [l, r] mà vẫn còn phần tử có giá trị = a[l] trong array thì remove a[l] và tăng l lên 1
        if (a[l] in copy_array):
          array_l_to_r.remove(a[l])
          if (len(set(array_l_to_r)) == k):
            l += 1
          else:
            print(str(l + 1) + " " + str(r))
            return
        # Ngược lại thì return luôn về kết quả
        else:
          print(str(l + 1) + " " + str(r))
          return
            
  print("-1 -1")   

   
# Input
nk = list(map(int, input().split()))
n = nk[0] # the number of positive number
k = nk[1] # the number of distinct number
#  [x, y]
a = list(map(int, input().split())) # the positive numbers

# Run and get output
array(n, k, a)