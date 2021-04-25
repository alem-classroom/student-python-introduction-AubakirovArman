def reverse_dict(dict):
    di={}
    for i in dict.items():
        di[i[1]]=i[0]
    return di
