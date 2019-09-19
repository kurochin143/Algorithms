#!/usr/bin/python

import sys

def is_in_combs(denominations, combs):
  for c in combs:
    c_copy = c.copy()
    for d in denominations:

      for cc_i in range(len(c_copy)):
        if c_copy[cc_i] == d:
          c_copy.pop(cc_i)
          break

    if len(c_copy) == 0:
      return True
  
  return False

# naive recursive solution, can only test up to 30 because it's slow
def making_change(amount, denominations):
  if amount == 0: return 1

  res = 0
  lengths = []
  combs = [] # unique combinations
  def rec(a, c_denominations): # current denominations
    nonlocal res
    for i in range(len(denominations)):
      new_a = a - denominations[i] # new amount
      c_denominations.append(denominations[i])
      if new_a == 0:
        if not is_in_combs(c_denominations, combs):
          combs.append(c_denominations.copy())
          res += 1
          lengths.append(len(c_denominations))

      elif new_a > 0:
        rec(new_a, c_denominations)

      c_denominations.pop()

  rec(amount, [])
  return res

# # dynamic solution
# def making_change(amount, denominations):
#   res = [0] * (amount + 1)
#   res[0] = 1
#   for d in denominations:
#     for i in range(amount + 1):
#       if d <= i:
#         res[i] += res[i - d]

#   return res[amount]

print(making_change(100, [1, 5, 10, 25, 50]))

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")