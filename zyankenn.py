# -*- coding: utf-8 -*-

import random
import time

print('\nじゃんけんしましょ')
time.sleep(1)
print('最初はグー、じゃんけん・・・')
you = int(input('1:グー\n2:チョキ\n3:パー\n'))
com = random.randint(1,3)

if you == 1:
    if com == 1:
        print("わたしは{}出したので引き分けです".format(com))
    elif com == 2:
        print("わたしは{}出したのであなたの勝ちです".format(com))
    elif com == 3:
        print("わたしは{}出したのでわたしの勝ちです".format(com))
if you == 2:
    if com == 1:
        print("わたしは{}出したのでわたしの勝ちです".format(com))
    elif com == 2:
        print("わたしは{}出したので引き分けです".format(com))
    elif com == 3:
        print("わたしは{}出したのであなたの勝ちです".format(com))
if you == 3:
    if com == 1:
        print("わたしは{}出したのであなたの勝ちです".format(com))
    elif com == 2:
        print("わたしは{}出したのでわたしの勝ちです".format(com))
    elif com == 3:
        print("わたしは{}出したので引き分けです".format(com))
