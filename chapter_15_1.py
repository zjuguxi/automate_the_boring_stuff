#！ python3
# -*- coding:utf-8 -*-

import time
def calcProd():
    product = 1
    for i in range(1, 100000):
        product = product *i
    return product


startTime = time.time()
prod = calcProd()
endTime = time.time()

print(('The result is {0} digits long.').format(len(str(prod))))
print(('Took {0} seconds to calculate.').format(endTime - startTime))
