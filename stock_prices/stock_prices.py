#!/usr/bin/python

import argparse

def find_max_profit(prices):
  if len(prices) == 1: return 0

  max = -2**64
  for i1 in range(len(prices)):
    for i2 in range(i1 + 1, len(prices)):
      profit = prices[i2] - prices[i1]
      if profit > max:
        max = profit

  return max


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))