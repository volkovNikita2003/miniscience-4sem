with open("data_1684659547.725596.txt") as f:
    data = f.readlines()
    for i in range(25, len(data), 1):
        line_x, line_y = data[i].split('] [', 1)
        print(f"particle {i - 25}: ({line_x.split(', ')[-1]}; {line_y.split(', ')[-1][:-2]})")
