list1 = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len1 = len(list1)
i = 0
while i <= len1:
    if list1[i] > 0:
        print(list1[i])
        i = i+1
    if list1[i] < 0: break