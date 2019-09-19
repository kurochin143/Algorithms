#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n == 0: return 1

  res = 0
  def rec(pv):
    nonlocal res
    for i in range(3, 0, -1):
      val = n - pv - i
      if val == 0:
        res += 1
      elif val > 0:
        rec(i + pv)

  rec(0)

  return res

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')