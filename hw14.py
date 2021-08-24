# Search Engine
class Node:
  max_value = -1
  child = dict()

def add_word(root, s, value):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
    tmp = tmp.child[ch]
    tmp.max_value = max(tmp.max_value, value)

def get_max_value(root, s):
  tmp = root
  for ch in s:
    if ch not in tmp.child:
      return -1
    tmp = tmp.child[ch]
  return tmp.max_value

n, q = list(map(int, input().split()))

root = Node()

for _ in range(n):
  word, priority = list(input().split())
  add_word(root, word, int(priority))

for _ in range(q):
  word = str(input())
  print(get_max_value(root, word))