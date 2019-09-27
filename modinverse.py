#欧几里得算法求最大公约数
def get_gcd(a, b):
	k = a // b
	remainder = a % b
	while remainder != 0:
		a = b 
		b = remainder
		k = a // b
		remainder = a % b
	return b
	
#改进欧几里得算法求线性方程的x与y
def get_(a, b):
	if b == 0:
		return 1, 0
	else:
		k = a // b
		remainder = a % b		
		x1, y1 = get_(b, remainder)
		x, y = y1, x1 - k * y1			
	return x, y
	
a, b = input().split()
a, b = int(a), int(b)
 
#将初始b的绝对值进行保存
if b < 0:
	m = abs(b)
else:
	m = b
flag = get_gcd(a, b)
 
#判断最大公约数是否为1，若不是则没有逆元
if flag == 1:	
	x, y = get_(a, b)	
	x0 = x % m #对于Python '%'就是求模运算，因此不需要'+m'
	print(x0) #x0就是所求的逆元
else:
	print("Do not have!")