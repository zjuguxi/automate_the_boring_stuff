#! python3
# -*- coding:utf-8 -*-

# 密码强度测试器
# 要求：
# 1. 至少8位
# 2. 有大小写
# 3. 至少1个数字

import re

text = input('enter your password >>> ')

longDetect = re.compile(r'.{8}')                        # 8位开头
lowercaseDetect = re.compile(r'[a-z]+')              # 有小写
uppercaseDetect = re.compile(r'[A-Z]+')             # 有大写
numberDetect = re.compile(r'[0-9]+')                       # 有数字

if len(text) > 8:
    lowercaseDetect.findall(text)
    if lowercaseDetect.findall(text) == True:
        uppercaseDetect.findall(text)
        if uppercaseDetect.findall(text) == True:
            numberDetect.findall(text)
            if numberDetect.findall(text) == True:
                print('OK!')

            else:
                print('Numbers are needed.')
        else:
            print('Uppercase character is needed.')

    else:
        print('Lowercase character is needed.')
else:
    print('Not enough characters!')