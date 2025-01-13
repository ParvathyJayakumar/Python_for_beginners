"""
Write a Python program to print a pattern of stars in the following format:
*
**
***
****
*****
"""
rows = 5  # Number of rows in the pattern
for i in range(1, rows + 1):
    print("*" * i)
