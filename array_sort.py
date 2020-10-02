from typing import List


def sort_by_bubble(collection: List):
  length = len(collection)

  for i in range(length):
    for j in range(i, length):
      if collection[i] > collection[j]:
        collection[i], collection[j] = collection[j], collection[i]


a = [9, 4, 2, 102, 32, 11, 9, 2, 0, 9]

i = 0

while i < len(a):
  k = i
  while k < len(a):
    if a[i] > a[k]:
      a[i], a[k] = a[k], a[i]
    k += 1

  i += 1


#sort_by_bubble(a)

print(a)
