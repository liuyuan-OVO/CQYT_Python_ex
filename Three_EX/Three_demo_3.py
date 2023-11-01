def is_prime(num):
    if num <= 100:
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
              return False
        return True
    else:
       return('out of size')
num = int(input())
print('Isprime:',is_prime(num))       