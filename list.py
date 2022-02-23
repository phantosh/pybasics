def numbers(n):
    print(f"Original list:{n}")

    first = n[0]
    last = n[-1]
    if first == last:
        print(f"True: {first}, {last}")
    else:
        print(f"False: {first}, {last}")
numbers([10, 20, 30, 40, 10])