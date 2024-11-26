list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len = len(list)
i = 0
while i <= len:
    if list[i] > 0:
        print(list[i])
        i = i+1
    if list[i] < 0: break