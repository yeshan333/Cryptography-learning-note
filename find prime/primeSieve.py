# Prime Number Sieve
# http://inventwithpython.com/hacking (BSD Licensed)

import math


def isPrime(num):
    # Returns True if num is a prime number, otherwise False.

    # Note: Generally, isPrime() is slower than primeSieve().

    # all numbers less than 2 are not prime
    if num < 2:
        return False

    # 测试目标数字平方根以内的数字
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 质数筛选（primeSieve）：埃拉托色尼筛选算法
# https://zh.wikipedia.org/wiki/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AD%9B%E6%B3%95
def primeSieve(sieveSize):
    # 返回 0 到 sieveSize(如果sieveSize是素数包括sieveSize)之间的所有素数的列表
    # the Sieve of Eratosthenes algorithm.

    # 创建一个包含sieveSize + 1个元素的列表
    # 将 0 到 sieveSize 标记为素数，True
    sieve = [True] * (sieveSize+1) 
    sieve[0] = False # 0 和 1 不是素数
    sieve[1] = False

    # 把 2 到 sieveSize 的平方根内的数的倍数剔除掉(不包括自己)，标记为 False
    for i in range(2, int(math.sqrt(sieveSize+1)) + 1):
        pointer = i * 2
        while pointer < sieveSize+1:
            sieve[pointer] = False
            pointer += i

    # compile the list of primes
    primes = []
    for i in range(sieveSize+1):
        if sieve[i] == True:
            primes.append(i)

    return primes

print(primeSieve(47))