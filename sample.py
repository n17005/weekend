# -*- coding: utf-8 -*-
import random
count = 0
for i in range(100):
    dice = random.randint(1,20)
    print(dice)
    if dice == 7:
        count +=1
print('7が出た確率は{}%です'.format(count))


