"""
https://dmoj.ca/problem/ddrp1
Tudor Gets a Goat
"""

car = int(input())
pick = int(input())
opened = int(input())

if pick == car:
    print("Switch")
else:
    print("Stay")