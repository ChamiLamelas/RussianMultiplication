def multiply_literal(num1, num2): 
    lefts = list() 
    rights = list() 

    while num1 > 0: 
        lefts.append(num1)
        rights.append(num2)
        num1 //= 2 
        num2 *= 2 

    right_sum = 0 

    for i in range(len(lefts)): 
        if lefts[i] % 2 == 1: 
            right_sum += rights[i]

    return right_sum

def multiply_pythonic(num1: int, num2: int) -> int: 
    lefts = list() 
    rights = list() 

    while num1 > 0: 
        lefts.append(num1)
        rights.append(num2)
        num1 >>= 1 
        num2 <<= 1 

    return sum(r for l, r in zip(lefts, rights) if l % 2 == 1)
    

assert multiply_literal(67, 98) == 67 * 98
assert multiply_pythonic(67, 98) == 67 * 98

    


