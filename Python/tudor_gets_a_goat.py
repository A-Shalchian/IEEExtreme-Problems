"""
https://dmoj.ca/problem/ddrp1
Double Doors Regional P1 - Tudor Gets a Goat

Problem Description:
Tudor likes goats! One day, Tudor finds himself inside a mall, the Honty Mall.
He is participating in a game show where he has the chance to either win a goat or a car.
In the rewards segment of the game show, Tudor gets to select one of three rooms, each of
which is blocked from view by a set of double doors. Behind one set of double doors is a car,
which Tudor doesn't want. Behind each of the other two sets of double doors is a goat,
which Tudor will take home and nurture. Tudor will be happy with either goat.

Because Tudor often has trouble distinguishing among sets of double doors, the rooms are
conveniently numbered 1, 2, and 3. Tudor merely has to say the number of the room he wants
to inspect, after which he gets to open the double doors and claim his prize.

Jason, the host of the game, really wants Tudor to get a goat. To help him in his quest,
Jason chooses to open the double doors of a room that Tudor didn't select which contains a goat.
However, Tudor can't actually take that goat. That would be unethical.

With this information, Tudor suddenly starts to panic. Should he switch his room selection
to the other room to get the goat?

Input:
- Line 1: N (the car is behind room number N)
- Line 2: M (Tudor has selected room number M)
- Line 3: P (Jason has opened room number P)

Output:
- If Tudor should switch rooms, output "Switch". Otherwise, output "Stay".

This is like the Monty Hall problem.
"""

car = int(input())
pick = int(input())
opened = int(input())

if pick == car:
    print("Switch")
else:
    print("Stay")