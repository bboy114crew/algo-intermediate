# Dynamic Array & String

# Care about delete/remove, append/insert, access 

# In python, positive index - negative index = len 

# Fashion in Berland  
# def jacket_is_fastened(number_of_buttons, list_button_state):
#   number_of_opened_buttons = 0

#   if number_of_buttons == 1:
#     if list_button_state[0] == 1:
#       print("YES")
#     else:
#       print("NO")
#   else:
#     for button_state in list_button_state:
#       if number_of_opened_buttons > 1:
#         print("NO")
#         return
#       if button_state == 0:
#         number_of_opened_buttons = number_of_opened_buttons + 1
#     if number_of_opened_buttons == 1:
#       print("YES")
#     else:
#       print("NO")
#       return
    
# # Input 
# # number_of_buttons = int(input())
# # list_button_state = list(map(int, input().split()))

# # Run and get output
# # jacket_is_fastened(number_of_buttons, list_button_state)

# # Night at the Museum
# # a -> z 97 -> 122
# def mininum_number_of_rotations(name):
#   result = 0 # minimum number of rotations of the wheel required 

#   list_char_of_name = list(name) # array of character in name
#   first_char_index = 0 # index of first character

#   ascii_of_a = 97
#   ascii_of_z = 122

#   number_of_move = 0 # number of moving 

#   def min_cost_of_move(ascii_from, ascii_to):
#     cost_counterclockwise_move = 0
#     cost_clockwise_move = 0
#     if (ascii_from < ascii_to):
#       cost_clockwise_move = abs(ascii_from - ascii_to)
#       cost_counterclockwise_move = (ascii_of_z - ascii_to) + (ascii_from - ascii_of_a) + 1
#     else:
#       cost_clockwise_move = (ascii_of_z - ascii_from) + (ascii_to - ascii_of_a) + 1
#       cost_counterclockwise_move = abs(ascii_from - ascii_to)
#     min_cost_move = min(cost_clockwise_move, cost_counterclockwise_move)
#     return min_cost_move

#   if (ord(list_char_of_name[0]) != 97):
#     ascii_of_from = ascii_of_a
#     ascii_of_to = ord(list_char_of_name[first_char_index])
#     result += min_cost_of_move(ascii_of_from, ascii_of_to)


#   for char_or_name_index in range(len(list_char_of_name) - 1):
#     ascii_of_from = ord(list_char_of_name[first_char_index])
#     ascii_of_to = ord(list_char_of_name[first_char_index + 1])
#     result += min_cost_of_move(ascii_of_from, ascii_of_to)
#     first_char_index = first_char_index + 1
  
#   print(result)

# # Input
# name = str(input())

# # Run and get output
# mininum_number_of_rotations(name)

#Bear and Game
# Bear Limak likes watching sports on TV. He is going to watch a game today. The game lasts 9090 minutes and there are no breaks.

# Each minute can be either interesting or boring. If 1515 consecutive minutes are boring then Limak immediately turns TV off.

# You know that there will be NN interesting minutes T_1, T_2, ..., T_N
# Your task is to calculate for how many minutes Limak will watch the game.

# Input Format
# The first line of the input contains one integer N (1 <= N <= 90) — the number of interesting minutes.

# The second line contains N integers T_1, T_2, ..., T_N (1 <= T_1 < T_2 < ...< T_N <= 90) given in the increasing order.

# Output Format
# Print the number of minutes Limak will watch the game.

# input
# 3
# 7 20 88

# output
# 35

# input
# 9
# 16 20 30 40 50 60 70 80 90

# output
# 15

# input
# 9
# 15 20 30 40 50 60 70 80 90

# output
# 90

# Explanation for sample test
# In the first sample, minutes 21, 22, ..., 35 are all boring and thus Limak will turn TV off immediately after the 3535-thth minute. So, he would watch the game for 35 minutes.
# In the second sample, the first 15 minutes are boring.
# In the third sample, there are no consecutive 1515 boring minutes. So, Limak will watch the whole game.

# def time_limak_watch_game(num_interesting_minutes, list_of_minutes):
#   result = 0
#   min_time_watch = 15
#   max_time_watch = 90
#   length_of_list = len(list_of_minutes)
#   for index in range(length_of_list):
#     current_minute = list_of_minutes[index]
#     if (index == 0):
#       if (current_minute - min_time_watch > 0):
#         result += min_time_watch
#         print(result)
#         return
#       else:
#         result += current_minute
#         if (length_of_list == 1):
#           if (max_time_watch - current_minute > min_time_watch):
#             result += min_time_watch
#     if (index > 0):
#       previous_minute = list_of_minutes[index - 1]
#       if (current_minute - previous_minute <= min_time_watch):
#         result = 0
#         result += current_minute
#         if (index == length_of_list - 1):
#           if (max_time_watch - current_minute >  min_time_watch):
#             result += min_time_watch
#           else:
#             result = result + max_time_watch - current_minute
#       else:
#         result += min_time_watch
#         print(result)
#         return

#   print(result)


# # Input
# num_interesting_minutes = int(input())
# list_of_minutes = list(map(int, input().split()))

# # Run and get output
# time_limak_watch_game(num_interesting_minutes, list_of_minutes)

# Vitaly and Strings

def vitaly_and_string(s1, s2):
  chars_s1 = list(s1)
  chars_s2 = list(s2)
  for i in range(len(chars_s1) - 1, -1, -1):
    if s1[i] == 'z':
        s1[i] = 'a'
    else:
        s1[i] = chr(ord(s1[i]) + 1)
        break
 
  print(s1 if s1 != s2 else "No such string")   

# Input
s1 = str(input())
s2 = str(input())

# Run and get output
vitaly_and_string(s1, s2)

# def arrays(s1_len, s2_len, sub_s1, sub_s2, s1, s2):
#   if (s1[sub_s1 - 1] < s2[s2_len - sub_s2]):
#     print("YES")
#   else:
#     print("NO")

# # Input
# ss_len = list(map(int, input().split()))
# s1_len = ss_len[0]
# s2_len = ss_len[1]
# subs_len = list(map(int, input().split()))
# sub_s1 = subs_len[0]
# sub_s2 = subs_len[1]
# s1 = list(map(int, input().split()))
# s2 = list(map(int, input().split()))

# # Run and get output
# arrays(s1_len, s2_len, sub_s1, sub_s2, s1, s2)

# def big_segment(list_segment):
#   if (len(list_segment) <= 1):
#     print(1)
#     return
#   min = list_segment[0][0]
#   max = list_segment[0][1]
#   for segment in list_segment:
#     if (segment[0] < min):
#       min = segment[0]
#     if (segment[1] > max):
#       max = segment[1]
#   for index in range(len(list_segment)):
#     if ((list_segment[index][0] == min) and (list_segment[index][1] == max)):
#       print(index + 1)
#       return
#   print(-1)

# # Input
# list_segment = []
# num_segment = int(input())
# for index in range(num_segment):
#   segment = list(map(int, input().split()))
#   list_segment.append(segment)

# # Run and get output
# big_segment(list_segment)

# def big_segment(list_segment):
#   if (len(list_segment) <= 1):
#     print(1)
#     return
#   min = list_segment[0][0]
#   max = list_segment[0][1]
#   for segment in list_segment:
#     if (segment[0] < min):
#       min = segment[0]
#     if (segment[1] > max):
#       max = segment[1]
#   for index in range(len(list_segment)):
#     if ((list_segment[index][0] == min) and (list_segment[index][1] == max)):
#       print(index + 1)
#       return
#   print(-1)

# # Input
# list_segment = []
# num_segment = int(input())
# for index in range(num_segment):
#   segment = list(map(int, input().split()))
#   list_segment.append(segment)

# # Run and get output
# big_segment(list_segment)

