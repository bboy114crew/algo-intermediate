# https://leetcode.com/problems/candy/
def candy(ratings):
  number_of_ratings = len(ratings)
  result = [1 for i in range(number_of_ratings)]

  for idx in range(number_of_ratings - 1):
    if ratings[idx] < ratings[idx + 1]:
      result[idx + 1] = result[idx] + 1

  for idx in range(number_of_ratings - 1, 0, -1):
    if ratings[idx] < ratings[idx - 1]:
      result[idx - 1] = max(result[idx - 1], result[idx] + 1)

  return sum(result)

print(candy([1,2, 87, 87, 87, 2, 1]))