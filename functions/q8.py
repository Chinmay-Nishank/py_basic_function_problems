def distinct(list):
    unique = []
    for i in list:
        if i not in unique:
            unique.append(i)
    return unique
print(distinct([1,22,22,12,12,2]))        
            