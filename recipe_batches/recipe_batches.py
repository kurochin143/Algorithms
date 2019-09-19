#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max = 2**64

  for key in recipe:
    r_val = recipe[key]
    if key not in ingredients:
      return 0 # no such ingredient
    i_val = ingredients[key]
    num = int(i_val / r_val)
    if num == 0:
      return 0 # not enough ingredient unit
    if num < max:
      max = num

  return max


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))