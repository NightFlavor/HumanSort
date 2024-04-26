import random
def ask_user_for_items():
    all_items = []
    while True:
        user_input = input("Give Input: ")
        if user_input == "":
            return all_items
        else:
            all_items.append(user_input)

def better(item1, item2):
    try:
        user_choice = int(input(f"Choose item 1 or 2\n 1: {item1}\n 2: {item2}: \n"))
    except ValueError:
        print("Please enter a correct value.")
        better(item1,item2)
    return user_choice == 2

while True:
    user_choice = input("1. File mode 2. Manual mode")
    if int(user_choice) == 1:
        file_name = input("Provide name of text file: ")
        file = open(f"{file_name}.txt", "r")
        all_items = file.readlines()
        file.close()
        break
    elif int(user_choice) == 2:
        all_items = ask_user_for_items()   
        break

random.shuffle(all_items)
all_items = [item.strip() for item in all_items]
used_combinations = []

while True:
    has_swaped=False
    for i in range(0, len(all_items)):
        if i != len(all_items)-1:
            item1 = all_items[i]
            item2 = all_items[i+1]
            if [item1,item2] not in used_combinations and [item2,item1] not in used_combinations:
                if better(item1, item2):
                    all_items[i],all_items[i+1] = item2,item1
                    has_swaped=True
                used_combinations.append([item1,item2])
    if not has_swaped:
        break

for i, item in enumerate(all_items, start=1):
    print(f"{i}: {item}")