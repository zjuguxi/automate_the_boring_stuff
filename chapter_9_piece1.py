#! python3
# -*- coding:utf-8 -*-

import os

path = '/Users/apple/automate_the_boring_stuff/'

for filename in os.listdir(path):
    if filename.endswith('md'):
        print(filename)

