def size_of_list(list):
    return len(list)

def add_elem_to_list(list, elem):
    list.append(elem)
    return list

def delete_elem_from_list(list, index = -1):
    if len(list)>index:
        list.pop(index)
        return list
    else:
        return []

def count_elements_in_list(list, x):
    return list.count(x)
    # count elements in the list that are equal to x and return the count

def sort_list(list):
    list.sort()
    return list

def reverse(list):
    return list.reverse()
