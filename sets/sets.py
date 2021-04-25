def size_of_set(set):
    return len(set) 
def is_elem_in_set(set, elem):
    return elem in set

def are_sets_equal(first_set, second_set):
    return first_set==second_set

def add_elem_to_set(set, elem):
    set.add(elem)
    return set
def remove_elem_if_exists(set, elem):
    if elem in set:
        set.remove(elem)
        return set
    else:
        return set

def delete_first_element(set):
    set.pop()
    return set
    