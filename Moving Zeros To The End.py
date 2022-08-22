def move_zeros(lst):
    """
    Write an algorithm that takes an array and moves all of the zeros to the end,
    preserving the order of the other elements.
    """
    counter = 0
    moved_list = []
    for x in range(len(lst)):
        if lst[x] == 0:
            counter += 1
        else:
            moved_list.append(lst[x])
    for x in range(counter):
        moved_list.append(0)
    return moved_list


list = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
print(move_zeros(list))