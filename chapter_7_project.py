#! python3
# -*- coding:utf-8 -*-

# 密码强度测试器
# 要求：
# 1. 至少8位
# 2. 有大小写
# 3. 至少1个数字

import re

text = input('enter your password >>> ')

longDetect = re.compile(r'^.{8}')                        # 8位开头
lowercaseDetect = re.compile(r'[a-z]')              # 有小写
uppercaseDetect = re.compile(r'[A-Z]')             # 有大写
numberDetect = re.compile(r'[0-9]')                       # 有数字

if longDetect(text) == True:
    lowercaseDetect(text)
    if lowercaseDetect(text) == True:
        uppercaseDetect(text)
        if uppercaseDetect(text) == True:
            numberDetect(text)
            if numberDetect(text) == True:
                print('OK!')

            else:
                print('numbers are needed.')
        else:
            print('Uppercase should be included.')

    else:
        print('Lowercase should be included.')
else:
    print('Not enough characters!')