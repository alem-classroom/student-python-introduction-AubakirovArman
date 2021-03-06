def size_of_list(list):
    return len(list)
    # return size of list

def add_elem_to_list(list, elem):
    list.append(elem)
    return list
    # add elem to list and return the list

def delete_elem_from_list(list, index = -1):
    if len(list) <= index:
        return []
    return list.pop(index)

    # delete element from list, such that its index is index
    # if index is invalid, return empty list

def count_elements_in_list(list, x):
    return list.count(x)
    # count elements in the list that are equal to x and return the count

def sort_list(list):
    return(list.sort())
    # return sorted list

def reverse(list):
    return(list.reverse())
