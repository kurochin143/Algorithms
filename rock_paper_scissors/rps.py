#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0: return [[]]

  rps = ["rock", "paper", "scissors"]
  res = []
  def rec(arr, cn):
    nonlocal res
    for i in range(len(rps)):
      arr.append(rps[i])
      if cn == n:
        res.append(arr.copy())
      else:
        rec(arr, cn + 1)
      arr.pop()
    
  rec([], 1)

  return res

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')