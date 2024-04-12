def intersect(list1, list2):
  result = []
  for element in list1:
    if element in list2:
      result.append(element)
  return result


print(intersect([1, 2, 3, 4,5], [2, 3, 5,5,6]))
