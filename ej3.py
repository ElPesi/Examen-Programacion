def IsPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def sumValues(matrix):
  total = 0
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if (i + j) % 2 == 1 and IsPrime(matrix[i][j]):
        total += matrix[i][j]
  return total


print(sumValues([[1, 2, 3], [5, 6, 7], [9,10,11,]]))
