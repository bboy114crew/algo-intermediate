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
# def array(n, k, a):
#   if k == 1:
#     print(1, 1)
#     return
#   l = 0
#   r = 0

#   count_appear = {}
#   for number in a:
#     if number in count_appear:
#       count_appear[number] += 1
#     else:
#       count_appear[number] = 1

#   distinct_numbers = set()
  
#   array_l_to_r = []

#   # N???u c?? 5 s??? 1 li??n ti???p v?? d??? 1111151 th?? l s??? l?? 4
#   while (l < count_appear[a[0]] and n > 1):
#     if (a[0] == a[l + 1]):
#       l += 1
#     else:
#       break
  
#   while (l < n and r < n):
#     distinct_numbers.add(a[r])

#     # D??y s??? trong ??o???n [l, r]
#     if (r >= l):
#       array_l_to_r.append(a[r])

#     r += 1

#     # Cho ?????n khi c?? ????? k s??? ri??ng bi???t trong ??o???n [l, r]
#     if (len(distinct_numbers) == k):
#       while (l < r):
#         copy_array = [*array_l_to_r]
#         copy_array.remove(a[l])
#         # N???u sau khi remove a[l] kh???i array trong ??o???n [l, r] m?? v???n c??n ph???n t??? c?? gi?? tr??? = a[l] trong array th?? remove a[l] v?? t??ng l l??n 1
#         if (a[l] in copy_array):
#           array_l_to_r.remove(a[l])
#           if (len(set(array_l_to_r)) == k):
#             l += 1
#           else:
#             print(l + 1, r)
#             return
#         # Ng?????c l???i th?? return lu??n v??? k???t qu???
#         else:
#           print(l + 1, r)
#           return
            
#   print(-1, -1)    

   
# # Input
# nk = list(map(int, input().split()))
# n = nk[0] # the number of positive numbers
# k = nk[1] # the number of distinct numbers
# #  [x, y]
# a = list(map(int, input().split())) # the positive numbers

# # Run and get output
# array(n, k, a)

# # Sereja and Dima
# def sereja_and_Dima(n, a):
#   r = len(a) - 1
#   l = 0

#   sereja_score = 0
#   dima_score = 0

#   for i in range(len(a)):
#     if (i % 2 == 0):
#       if (a[l] > a[r]):
#         sereja_score += a[l]
#         l += 1
#       else:
#         sereja_score += a[r]
#         r -= 1
#     else:
#       if (a[l] > a[r]):
#         dima_score += a[l]
#         l += 1
#       else:
#         dima_score += a[r]
#         r -= 1

#   print(sereja_score, dima_score)

# # Input
# n = int(input())
# a = list(map(int, input().split()))

# # Run and get output
# sereja_and_Dima(n, a)

# Approximating a Constant Range
# def approximating_a_constant_range(n, a):
#   l = 0
#   r = 0

#   max_range = r - l + 1
#   distinct_number = set()
#   distinct_number.add(a[l])

#   while (l < n and r < n - 1):
#     r += 1
#     distinct_number.add(a[r])
#     if (len(distinct_number) <= 2):
#       max_range = max(max_range, r - l + 1)
#     else:
#       k = r - 2
#       while (k < r and k >= l):
#         if (a[k] != a[r - 1]):
#           l = k + 1
#           distinct_number.remove(a[k])
#           break
#         else:
#           k = k - 1

#   print(max_range)

# # Input
# n = int(input())
# a = list(map(int, input().split()))

# # Run and get output
# approximating_a_constant_range(n, a)

# Wrath
def wrath(n, a):
  j = n - 1
  people_was_killed = 0

  for i in range(n - 1, -1, -1):
    j = min(j, i)
    pivot = max(0, i - a[i])

    if j > pivot:
        people_was_killed += (j - pivot)
        j = pivot

  print(n - people_was_killed)

# Input
n = int(input())
a = list(map(int, input().split()))

# Run and get output
wrath(n, a)

# Alice Bob and Chocolate
# def alice_bob_and_chocolate(n, a):
#   l = -1
#   r = len(a)
  
#   alice_total = 0
#   bob_total = 0

#   if (n == 2):
#     print(1, 1)
#     return

#   while (l != r):
#     if (r - l == 2):
#       if (alice_total < bob_total):
#         l += 1
#         alice_total += a[l]
#       elif (alice_total > bob_total):
#         r -= 1
#         bob_total += a[r]
#       else:
#         l += 1
#         alice_total += a[l]
#       break
#     else:
#       if (alice_total < bob_total):
#         l += 1
#         alice_total += a[l]
#       elif (alice_total > bob_total):
#         r -= 1
#         bob_total += a[r]
#       else:
#         l += 1
#         alice_total += a[l]
#         r -= 1
#         bob_total += a[r]
    
#   print(l + 1, n - 1 - r + 1)

# # Input
# n = int(input())
# a = list(map(int, input().split()))

# # Run and get output
# alice_bob_and_chocolate(n, a)