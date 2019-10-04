# Cryptomath Module
# http://inventwithpython.com/hacking (BSD Licensed)

# 欧几里得算法（辗转相除求最大公约数）
# https://baike.baidu.com/item/%E6%AC%A7%E5%87%A0%E9%87%8C%E5%BE%B7%E7%AE%97%E6%B3%95/9002848?fr=aladdin
# Greatest Common Divisor (最大公约数)
def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b

# https://wenku.baidu.com/view/34dbaef343323968011c92ea.html
# # 扩展欧几里得求模逆元：https://zh.wikipedia.org/wiki/模反元素#用扩展欧几里得算法
# ????have to learn
# 思路：https://blog.csdn.net/baidu_38271024/article/details/78881031?tdsourcetag=s_pctim_aiomsg
def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    # https://baike.baidu.com/item/%E6%89%A9%E5%B1%95%E6%AC%A7%E5%87%A0%E9%87%8C%E5%BE%97%E7%AE%97%E6%B3%95
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m