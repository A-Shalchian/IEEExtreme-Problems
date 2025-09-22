"""
https://dmoj.ca/problem/ddrp2
Double Doors Regional P2 - Tudor Learns DDR

Problem Description:
Tudor is learning how to play Dance Dance Revolution! He is struggling with complex note patterns
and decides to focus on three-step sequences. There are four directions: up (U), down (D), left (L),
and right (R), where up/down are opposite and left/right are opposite.

Tudor is interested in:
- Crossover sequence: First and last steps are opposite, all three steps are distinct, and first step is L or R
- Candle sequence: First and last steps are opposite, all three steps are distinct, and first step is U or D
- Neither: Does not meet the criteria for crossover or candle

Given a three-step sequence, determine if it's a crossover, candle, or neither.
"""

opposite_moves = {
    "U": "D",
    "D": "U",
    "L": "R",
    "R": "L"
}

move_sequence = input().strip()
a, b, c = move_sequence[0], move_sequence[1], move_sequence[2]

first_opposite_last = (opposite_moves[a] == c)

all_distinct = len({a, b, c}) == 3

if all_distinct and first_opposite_last:
    if a in ("L", "R"):
        print("Crossover")
    elif a in ("U", "D"):
        print("Candle")
else:
    print("Neither")