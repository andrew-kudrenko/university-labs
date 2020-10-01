from typing import List


def swap(collection: List, from_idx: int, to_idx: int):
  buffer = collection[from_idx]
  collection[from_idx] = collection[to_idx]
  collection[to_idx] = buffer


def sort_by_bubble(collection: List):
  length = len(collection)

  for i in range(length):
    for j in range(i, length):
      if collection[i] > collection[j]:
        swap(collection, i, j)
