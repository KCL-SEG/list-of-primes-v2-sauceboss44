"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    list = [2]
    number = 3
    while len(list) < number_of_primes:
        print(number)
        if isPrime(number):
            list.append(number)
        number += 1
    return list
def isPrime(number):
    for divisor in range(2,int(number**1/2)+1):
        if number % divisor == 0:
            return False
    return True

print(primes(10))