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

    # Replace random "#" characters with "O" without replacing spaces
    num_replacements = random.randint(1, min(len(available_indices), len(lines)))
    for _ in range(num_replacements):
        random_index = random.choice(available_indices)
        lines = lines[:random_index] + "O" + lines[random_index+1:]
        available_indices.remove(random_index)
    # print (f"Candles lit: {num_replacements}")
    # print(len(available_indices))
    # print(len(lines))
    print(lines)

def leg(amount: int):
    space = amount - 2
    if amount > 1:
        print(" " * space + "|#|")
    else:
        print(" " * space + "|")

def spruce(amount: int):
    top_spruce(amount)
    leg(amount)

if __name__ == "__main__":
    choice = int(input("How tall is the tree? "))
    spruce(choice)
