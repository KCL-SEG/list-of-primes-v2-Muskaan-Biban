
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    try:
        if number_of_primes <= 0:
            raise ValueError("ValueError")
        else:
             return createPrimes(number_of_primes)
    except ValueError as e:
        print(f'We caught a {e.__class__}')
        
        
def createPrimes(number_of_primes):
    list = []
    count = 0
    while len(list) < number_of_primes:
        if count == 0 or count == 1:
            count += 1
            continue
        else:
            for j in range(2, int(count/2) + 1):
                if count % j == 0:
                    count += 1
                    break
            else:
                list.append(count)
                count += 1
    return list

primes(-1)