string = str(input("Please input a word"))
print(f"Your word is {string}")

size = len(string)

for item in range(0, size - 1, 2):
    print("index[", item, "]", string[item])