# RSA 算法基本步骤

## 一、公钥密钥的生成

- Step 1：创建两个随机大质数p、q，n = p * q
- Step 2：创建一个与 (p-1)*(q-1) 互质的随机数整数e，即$ gcd(\phi(n),e) = 1 $
- Step 3：计算 e 的模逆 d，可使用扩展欧几里得算法求解，即$ ex+\phi(n)y=gcd(e,\phi(n))=1 $
- Final ：公钥(n, e)、私钥(n, d)

### 关键算法

- 欧几里得算法：求两个数的最大公约数


- 扩展欧几里得算法（根据贝祖等式）：求解模逆


- 拉宾米勒素性检验判断一个大数是否为素数


## 二、文本加密

>区块数学

### 纯文本的加密、解密

#### 公钥(n，e)加密

- Step 1：将加密字符串进行分块，每128个字符为一块，注意区块大小小于或等于密钥大小
- Step 2: 按块将块内的每一个字符转换为ASCII整数，通过的$ {(ASCII num)} \times 256^{index} $的方式将每个字符对应的ASCII整数转换成一个较大的整数，再将所有的较大整数求和即可得区间大整数（index为某个字符所在区块内对应的索引）。
- Step 3：对每个区块所对应得大整数进行加密。加密算法如下：

$$ cipherBlockInt = BlockInt^{e}\ \ \ mod\ \ \ n $$

- Step 4：将每个区块加密后的整数转换成字符串格式，使用`,`连接成一个长字符串写入文件中，写入文件时以如下格式写入：

明文字符串长度_每个区块大小(Bytes)_密文字符整数(以,分隔的String)

![示例](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190929160434.png)

#### 私钥(n,d)解密

- Step 1：从文件读取被加密信息（字符串大小、区块大小、密文），将字符串块转回整数块
- Step 2：分别对每个区块进行解密，解密算法如下：

$$ BlockInt = cipherBlockInt^{d}\ \ \  mod\ \ \  n  $$

- Step 3：将区块整数分解成`blocksize`个整数（每个整数是一个字符的ASCII值），这里采用倒序分解法（先求最后一个字符）

#### 加解密实践

- **1、Hamlet.txt的加密，17万个字符，180,768 Bytes**

**加密效率，23秒左右**

![加密效率](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190929213722.png)

**加密后结果，175176个字符**

![](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190929213753.png)

**解密效率，47秒左右**

![](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190929213818.png)

- **2、15M文件的加密，一千五百多万个字符，16,081,069 Bytes**

**加密效率，2064秒左右**

![](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190930104022.png)

**加密后结果，15583559个字符**

![](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190930103931.png)

**解密效率，4129秒左右**

![](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190930104044.png)

### 图像、视频文件加密的思考

>Base64是一种基于64个可打印字符来表示二进制数据的表示方法。由于$2^{6}=64$，所以每6个比特为一个单元，对应某个可打印字符。3个字节有24个比特，对应于4个Base64单元，即3个字节可由4个可打印字符来表示。它可用来作为电子邮件的传输编码。在Base64中的可打印字符包括字母A-Z、a-z、数字0-9，这样共有62个字符，此外两个可打印符号在不同的系统中而不同。
>[https://zh.wikipedia.org/wiki/Base64](https://zh.wikipedia.org/wiki/Base64)

前端到后台的图片的传输一般都是经过Base64编码后传输的，目的是为了减少Http请求

不同硬件设备某些二进制值代表的意义不一样，Base64使用的64个字符，经ASCII/UTF-8编码后在大多数机器，软件上的行为是一样的。

>Base64编码是从二进制值到某些特定字符的编码，这些特定字符一共64个，所以称作Base64。


![Base64编码示例](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190930175058.png)

更多：

- [玩转图片Base64编码](https://www.cnblogs.com/coco1s/p/4375774.html)
- [Base64编码原理与应用](http://blog.xiayf.cn/2016/01/24/base64-encoding/)

#### 图像文件Base64编码后加密解密实践

**大小为1.18MB的jpg格式的图片经Base64编码后转为大小为1.58MB的文本**

![](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190930175511.png)

**对文本（1657784个字符）进行加密，结果如下**

![](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190930175702.png)

**加密效率，219秒左右**

![](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190930175804.png)

**解密效率，681秒左右**

![](https://cdn.jsdelivr.net/gh/ssmath/mypic/img/20190930175845.png)

## 三、私钥加密、公钥解密

加密算法

$$ ciphertext = plaintext^{e}\ \ \ mod\ \ \ n $$

解密算法

$$ plaintext = ciphertext^{d}\ \ \  mod\ \ \  n $$




