"""
https://dmoj.ca/problem/dmopc17c5p1
DMOPC '17 Contest 5 P1 - IOI 101
"""

def main():

    mapping_dict = {
        "0": "O",
        "1": "l",
        "3": "E",
        "4": "A",
        "5": "S",
        "6": "G",
        "8": "B",
        "9": "g"
    }
    result = ""
    string_input = input().strip()

    for char in string_input:
        if char in mapping_dict:
            result += mapping_dict[char]
        else:
            result += char

    print(result)

if __name__ == "__main__":
    main()