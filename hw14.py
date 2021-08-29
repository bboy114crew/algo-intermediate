# class Node:
#   def __init__(self):
#     self.count_word = 0
#     self.child = dict()

# def add_word(root, s):
#   tmp = root
#   for ch in s:
#     if ch not in tmp.child:
#       tmp.child[ch] = Node()
#     tmp = tmp.child[ch]
#   tmp.count_word += 1

# def find_word(root, s):
#   temp = root
#   for ch in s:
#     if ch not in temp.child:
#       return False
#     temp = temp.child[ch]
#   return temp.count_word > 0

# def is_word(node):
#   return node.count_word != 0

# def is_empty(node):
#   return len(node.child) == 0

# def remove_word(root, s, level, leng):
#   if root == None:
#     return False
  
#   if level == leng:
#     if root.count_word > 0:
#       root.count_word -= 1
#       return True
#     return False
  
#   ch = s[level]

#   if ch not in root.child:
#     return False
  
#   flag = remove_word(root.child[ch], s, level + 1, leng)

#   if flag == True and is_word(root.child[ch]) == False and is_empty(root.child[ch]) == True:
#     del root.child[ch]
  
#   return flag

# def print_word(root, s):
#   if is_word(root):
#     print(s)
#   for ch in root.child:
#     print_word(root.child[ch], s + ch)

# root = Node()
# add_word(root, 'the')
# add_word(root, 'then')
# add_word(root, 'bigo')
# print(find_word(root, 'there'))
# print(find_word(root, 'ththere'))
# print(find_word(root, 'the'))
# print_word(root, '')
# remove_word(root, 'bigo', 0, len('bigo'))
# remove_word(root, 'the', 0, len('the'))
# remove_word(root, 'then', 0, len('then'))

# # Search Engine
# class Node:
#   def __init__(self):
#     self.max_value = -1
#     self.child = dict()
# def add_word(root, s, value):
#   tmp = root
#   for ch in s:
#     if ch not in tmp.child:
#       tmp.child[ch] = Node()
#     tmp = tmp.child[ch]
#     tmp.max_value = max(tmp.max_value, value)
# def get_max_value(root, s):
#   tmp = root
#   for ch in s:
#     if ch not in tmp.child:
#       return -1
#     tmp = tmp.child[ch]
#   return tmp.max_value

# n, q = list(map(int, input().split()))

# root = Node()

# for _ in range(n):
#   word, priority = list(input().split())
#   add_word(root, word, int(priority))

# for _ in range(q):
#   word = str(input())
#   print(get_max_value(root, word))

# # DNA Prefix
# class Node:
#   def __init__(self):
#     self.th_word = 1
#     self.max_value = -1
#     self.child = dict()

# def add_word(root, s):
#   global result
#   tmp = root
#   for i in range(len(s)):
#     ch = s[i]
#     if ch not in tmp.child:
#       tmp.child[ch] = Node()
#     else:
#       tmp.child[ch].th_word += 1
#     tmp = tmp.child[ch]
    
#     tmp.max_value = i + 1
#     if tmp.th_word != 0:
#       result = max(result, tmp.max_value * tmp.th_word)

# T = int(input())

# for case in range(T):
#   N = int(input())
#   root = Node()
#   result = 0
#   for i in range(N):
#     word = input()
#     add_word(root, word)
  
#   print('Case {}: {}'.format(case +1, result))
  
# # Consistency Checker
# class Node:
#   def __init__(self):
#     self.count_word = 0
#     self.child = dict()

# def add_word(root, s):
#   tmp = root
#   for i in range(len(s)):
#     ch = s[i]
#     if ch not in tmp.child:
#       tmp.child[ch] = Node()
#     else:
#       if tmp.child[ch].count_word >= 1 and i <= len(s) - 1:
#         return False
#     tmp = tmp.child[ch]
#   tmp.count_word += 1
#   if len(tmp.child) > 0:
#     return False
#   return True

# T = int(input())

# for case in range(T):
#   N = int(input())
#   root = Node()
#   result = True

#   words = []
  
#   for i in range(N):
#     word = input()
#     words.append(word)

#   for word in words:
#     result = add_word(root, word)
#     if result == False:
#       break
  
#   final_res = 'YES' if result == True else 'NO'
#   print('Case {}: {}'.format(case +1, final_res))

# Contacts
class Node:
  def __init__(self):
    self.count_word = 0
    self.child = dict()

def add_word(root, s):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
    tmp = tmp.child[ch]
    tmp.count_word += 1

def count_word(root, s):
  temp = root
  for ch in s:
    if ch not in temp.child:
      return 0
    else:
      temp = temp.child[ch]
  return temp.count_word


n = int(input())
root = Node()
for _ in range(n):
  op, word = list( input().split())
  if op == 'add':
    add_word(root, word)
  else:
    result = count_word(root, word)
    print(result)