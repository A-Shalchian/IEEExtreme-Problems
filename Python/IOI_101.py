"""
https://dmoj.ca/problem/dmopc17c5p1
DMOPC '17 Contest 5 P1 - IOI 101

Problem Description:
The number 1 looks quite similar to the letter l and the letter I. Similarly, the number 0
looks quite similar to the letter o. Sometimes, these simple replacements are used in passwords.

Roger is reviewing his passwords one day, and realizes that he no longer remembers what letters
he replaced with numbers! Alarmed, he pulls up the following table:

Replacement Table:
- 0 → O
- 1 → l
- 3 → E
- 4 → A
- 5 → S
- 6 → G
- 8 → B
- 9 → g

Given a string of alphanumeric characters, can you write a program to perform these replacements?

Input:
- The first and only line of input will contain a single string of alphanumeric characters.
- The given string will contain no more than 1000 characters.

Output:
- The output should have a single string: the result of performing all the replacements
  on the string given in the input.

Example: y0105w49 → yOlOSwAg
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