"""
https://dmoj.ca/problem/seed1
The Cosmic Era P1 - Ship

Problem Description:
The Archangel is being built! In order to build the Archangel, at least 1 of a number of
parts are required. In the following table, each part is represented by an uppercase character:

- Beam Weapons: B
- Frame (inclusive): F
- Thrusters: T
- Launch Pad: L
- Command Room: C

However, you appear to be missing some parts. Can you figure out which?

Input:
- The first line contains a string containing the identifiers of all the parts you have.
  The length of the string will be at least 1 and no longer than 10.

Output:
- The missing parts, each on a separate line and in any order.
- If there are no missing parts, output "NO MISSING PARTS".

Note: The string can contain duplicate parts (e.g., BFTLCC is valid and means no missing parts).
"""

def main():
    required = {"B", "F", "T", "L", "C"}
    parts = input().strip()
    have = set(parts)

    missing = required - have

    if not missing:
        print("NO MISSING PARTS")
    else:
        for m in missing:
            print(m)


if __name__ == "__main__":
    main()