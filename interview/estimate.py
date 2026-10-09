import random
def rounder(number: float) -> int:
   """
   round accepts a float and returns a rounded integer.defw
   the number is rounded up iff the decimal is >= .5
   """


   # TODO implement round function


   if number % 1 >= 0.5:
       return int(number) + 1
   return int(number)
# The rogram uses modulo operator to check the decimal portion of the number.

