def fibonacci (count):
    if count < 1 or count % 1 != 0:
        raise Exception("Number of numbers cannot be less than one or a floating point number")

    elif count == 1:
        return [0]
    
    elif count == 2:
        return [0, 1]
    
    else:
        a, b = 0, 1
        seq = [a, b]
        for i in range(2, int(count)):
            a, b = b, a + b
            seq.append(b)
        return seq

while "Ur mom is gay":
    ct = float(input("How many numbers would you like?"))
    print(str(fibonacci(ct))[1:-1])
