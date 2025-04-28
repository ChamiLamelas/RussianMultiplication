def multiply_literal(left, right): 
    lefts = list() 
    rights = list() 

    while left > 0: 
        lefts.append(left)
        rights.append(right)
        left //= 2 
        right *= 2 

    right_sum = 0 

    for i in range(len(lefts)): 
        if lefts[i] % 2 == 1: 
            right_sum += rights[i]

    return right_sum

def multiply_pythonic(left: int, right: int) -> int: 
    lefts = list() 
    rights = list() 

    while left > 0: 
        lefts.append(left)
        rights.append(right)
        left >>= 1 
        right <<= 1 

    return sum(r for l, r in zip(lefts, rights) if l % 2 == 1)
    

assert multiply_literal(67, 98) == 67 * 98
assert multiply_pythonic(67, 98) == 67 * 98

    


