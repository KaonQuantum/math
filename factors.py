def factorize(number):
    if number % 1 == 0 and number >= 1:
        factors = [] #Creates a list of factors that will be appended
        for i in range(1, number//2+1): #Checks whether numbers from 1 to the input floor divided by 2 are factors of the input
            if number % (i) == 0:
                factors.append(i)
        factors.append(number) #Adds the input to the list of factors
        return (factors)
    elif number == 0:
        factors = [] #Creates an empty list as 0 has no factors
        return factors
    else:
        raise TypeError("Non-whole numbers cannot be factorized.")
