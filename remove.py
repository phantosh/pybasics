def remove_char(word, n):
    print(f"Original word: {word}")
    w = len(word)
    if n > w:
        print(f"Number must not be longer than word: {w}")
    else:
        x = word[n::]
        print(f"New word: {x}")
remove_char("python", 2)