def size_of_list(list):
    return len(list)

def add_elem_to_list(list, elem):
    list.append(elem)
    return list

def delete_elem_from_list(list, index = -1):
    if index in list:
        for i in range(len(list)):
            if list[i]==index:
                list.pop(i)
                break
        return list
    else:
        return []
def count_elements_in_list(list, x):
    return list.count(x)


def sort_list(list):
    list.sort()
    return list

def reverse(list):
    return list.reverse()
