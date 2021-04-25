def insert_squares(arr, num):
    va=1
    while va<=num:
        arr.append(va**2)
        va=va+1
    return arr
