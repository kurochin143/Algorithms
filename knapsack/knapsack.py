#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

# ex out {'Value': 197, 'Chosen': [1, 7, 8]}

## using ratio, doesn't always work
# def knapsack_solver(items, capacity):
#   s = sorted(items, key=lambda i: i.size / i.value)
#   cap = 0
#   chosen = []
#   value = 0
#   for item in s:
#     if item.size + cap <= capacity:
#       cap += item.size
#       chosen.append(item.index)
#       value += item.value

#   chosen = sorted(chosen)
#   return {"Value": value, "Chosen": chosen}

# using naive recursion
def knapsack_solver(items, capacity):
  bags = [] # {"Value": 0, "Chosen": [], "Size": 0}
  def rec(bag, i, is_included):
    bag_copy = {}
    bag_copy["Value"] = bag["Value"]
    bag_copy["Chosen"] = bag["Chosen"].copy()
    bag_copy["Size"] = bag["Size"]

    if is_included:
      if items[i].size + bag_copy["Size"] <= capacity:
        bag_copy["Value"] += items[i].value
        bag_copy["Chosen"].append(items[i].index)
        bag_copy["Size"] += items[i].size
    
    next_i = i + 1
    if next_i < len(items):
      rec(bag_copy, next_i, True)
      rec(bag_copy, next_i, False)
    else:
      bags.append(bag_copy)

  # recurse 0 for not included and included
  rec({"Value": 0, "Chosen":[], "Size": 0}, 0, True)
  rec({"Value": 0, "Chosen":[], "Size": 0}, 0, False)

  # find the bag with max value
  best_bag = bags[0]
  for b in bags:
    if b["Value"] > best_bag["Value"]:
      best_bag = b

  best_bag.pop("Size")
  return best_bag

items = [Item(1, 1, 1),
          Item(2, 3, 4),
          Item(3, 4, 5),
          Item(4, 5, 7),]
print(knapsack_solver(items, 7))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')