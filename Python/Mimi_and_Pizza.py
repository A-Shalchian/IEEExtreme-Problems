"""
https://dmoj.ca/problem/dmopc17c5p0
DMOPC '17 Contest 5 P0 - Mimi and Pizza

Problem Description:
Mimi is ordering pizza! She looks at the menu with these options:
- Pizza A: $5, Not vegetarian (her favourite)
- Pizza B: $5, Vegetarian (2nd favourite)
- Pizza C: $2, Not vegetarian (3rd favourite)
- Pizza D: $2, Vegetarian (least favourite)

She can only order 1 type of pizza. Given her budget (B), number of pizzas she wants (P),
and whether vegetarian friends are coming, determine the most preferred pizza she can buy,
or "NO PIZZA" if she cannot afford P pizzas of any type.
"""

pizzas = {
    "A": (5, False),
    "B": (5, True),
    "C": (2, False),
    "D": (2, True)
}

preference = ["A", "B", "C", "D"]

budget = int(input())
pizza_amount = int(input())
veg_coming = input().strip()

for p in preference:
    price, is_veg = pizzas[p]

    # Skip non-veg if vegetarian friends are coming
    if veg_coming == "Y" and not is_veg:
        continue

    if price * pizza_amount <= budget:
        print(p)
        break
else:
    print("NO PIZZA")
