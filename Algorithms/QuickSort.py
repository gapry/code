import random

def quickSort(n):
    if len(n) <= 1:
        return n 
    
    print('IN:', n)
    ref = random.randint(0, len(n) - 1)
    val = n.pop(ref)
    print('REF:', val)
    
    n1 = []
    n2 = []
    while len(n) > 0:
        if n[0] < val:
            n1.append(n.pop(0))
        else:
            n2.append(n.pop(0))
    print('n1:', n1, ', n2:', n2)
    
    n1 = quickSort(n1)
    n2 = quickSort(n2)
    print('RETURN:', n1 + [val] + n2)
    
    return n1 + [val] + n2

    
if __name__ == '__main__':
    print(quickSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
