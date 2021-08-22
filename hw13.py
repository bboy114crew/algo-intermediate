# Distinct Count
T = int(input())

for _ in range(T):
  N, X = list(map(int, input().split()))
  numbers = list(map(int, input().split()))

  # distinct = {}
  # number_of_distinct = 0
  # for num in numbers:
  #   if distinct.get(num, None) != None:
  #     distinct[num] += 1
  #   else:
  #     distinct[num] = 1
  #     number_of_distinct += 1

  distinct = set()
  for num in numbers:
    distinct.add(num)
  number_of_distinct = len(distinct)
  
  if number_of_distinct == X:
    print('Good')
  elif number_of_distinct < X:
    print('Bad')
  else:
    print('Average')

  