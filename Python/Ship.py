"""
https://dmoj.ca/problem/seed1
The Cosmic Era P1 - Ship

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