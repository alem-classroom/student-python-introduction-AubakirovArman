def size_of_list(list):
    return len(list)
    # return sizt

def add_elem_to_list(list, elem):
    list.append(elem)
    return list
    # add elem to list and ret

def delete_elem_from_list(list, index = -1): 
    if index != -1 and len(list) > index:
        return list.pop(index)

    else:
        return list.pop()
  
    # delete element from list, such that its index is index


def count_elements_in_list(list, x):
    return list.count(x)
    # count elements in the list that are equal to x 

def sort_list(list):
    list = list.sort()
    return list
    # return sor

def reverse(list):
    list = list.reverse()
    # return reversed