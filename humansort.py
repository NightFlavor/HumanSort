import random
def ask_user_for_items():
    all_items = []
    while True:
        user_input = input("Give Input: ")
        if user_input == "":
            return all_items
        else:
            all_items.append(user_input)

def better(a, b):
    print(a)
    print(b)
    try:
        user_choice = int(input("Choose item 1 or 2: "))
    except:
        print("Please enter correct value")
    if user_choice == a or user_choice == 1:
        return False
    elif user_choice == b or user_choice == 2: 
        return True

while True:
    user_choice = input("1. File mode 2. Manual mode")
    if int(user_choice) == 1:
        file_name = input("Provide name of text file: ")
        file = open(f"{file_name}.txt", "r")
        all_items = file.readlines()
        random.shuffle(all_items)
        file.close()
        break
    elif int(user_choice) == 2:
        all_items = ask_user_for_items()   
        random.shuffle(all_items)
        break
used_combinations = []
while True:
    hasswaped=False
    for i in range(0, len(all_items), 1):
        item1 = all_items[i]
        if i != len(all_items)-1:
            item2 = all_items[i+1]
            if [item1,item2] not in used_combinations and [item2,item1] not in used_combinations:
                used_combinations.append([item1,item2])
                print(used_combinations)
                if better(item1, item2):
                    all_items[i] = item2
                    all_items[i+1] = item1
                    hasswaped=True
    
    if not hasswaped:
        break


file = open("mijn.txt", "r")
file.readlines()
file.close()

for i in range(0, len(all_items), 1):
    print(i+1,": ",all_items[i])

