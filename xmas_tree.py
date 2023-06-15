import random

def top_spruce(amount: int):
    space = amount - 1
    amount_mid = 1
    digit_list = "0123456789"
    i = 1
    lines = ""
    while i <= amount:
        line = " " * space + "#" * amount_mid + " " * space
        lines += line + "\n"
        i += 1
        amount_mid += 2
        space -= 1
    
    lines = lines[:-1]
    
    # Find indices of available positions for replacements
    available_indices = []
    for i in range(len(lines)):
        if lines[i] == "#":
            available_indices.append(i)
