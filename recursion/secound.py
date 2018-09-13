def first(value):
    if value//10:
        return first(value//10)
    else:
        return value

def remove_from_list(lst, value):
    if value not in lst:
        return lst
    else:
        lst.remove(value)
        return remove_from_list(lst, value)

def perfect_number(value, div = 1, sm = 0):
    if value==sm: 
        return True
    else:
        if value//div != 1:
            sm += div
            return perfect_number(value,div+1, sm)
        else:
            return False
        


print(first(51911198))
print(remove_from_list([1,2,3,8,9,8,8,8,8,7,9,6,], 8))
print(perfect_number(28))