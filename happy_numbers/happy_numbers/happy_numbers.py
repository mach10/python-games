"""
Objective: print the happy numbers from 1 up to 1,000.

A happy number is a number defined by the following process: Starting with any positive integer, replace the number
with the sum of the squares of its digits, and repeat the process until the number either equals 1 (where it will stay),
or it loops endlessly in a cycle that does not include 1. Those numbers for which this process ends in 1 are happy
numbers, while those that do not end in 1 are unhappy numbers (or sad numbers).

For example, 19 is happy, as the associated sequence is:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

On the other hand, 4 is unhappy, as the associated sequence is:
4^2 = 16
1^2 + 6^2 = 37
3^2 + 7^2 = 58
5^2 + 8^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4

The first five happy numbers are 1, 7, 10, 13, 19.

Print the happy numbers up to 1,000. Hint: There are 143.

"""

def is_happy(number):
    """
    this could be used to test certain numbers, instead of printing them all out.
    :param number:
    :return: Boolean
    """
    return True

def get_happy_numbers_between(start, finish):
    """
    Return all the happy numbers between start and finish inclusive
    :param start:
    :param finish:
    :return: Array of all happy numbers
    """
    return []