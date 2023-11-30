
"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num /2)+1):
        if num % i == 0:
            return False
        
    return True 
def primes(number_of_primes):
    arr = []
    num = 2
    if number_of_primes > 0:
        while (len(arr) < number_of_primes):
            if check_prime(num):
                arr.append(num)
            num = num + 1
    else:
        raise ValueError
    return arr
