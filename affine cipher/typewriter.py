# 装 bi 打字效果，一个字一个字的慢慢打

import sys, random, time


def print(message, end='\n'):
    for c in message:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.randint(40, 100)/ 1000)
    sys.stdout.write(end)
