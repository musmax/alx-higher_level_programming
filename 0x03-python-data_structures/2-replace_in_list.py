def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        return my_list(idx)
    elif idx > length - 1:
        return my_list(idx)
    elif my_list(idx) == my_list(element):
        return my_list(element)
