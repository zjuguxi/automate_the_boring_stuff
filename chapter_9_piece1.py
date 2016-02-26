#! python3
# -*- coding:utf-8 -*-

import os

# path = '/Users/apple/automate_the_boring_stuff/'

# for filename in os.listdir(path):
#     if filename.endswith('md'):
#         print(filename)


path = ('/Users/apple/')

for foldername, subfolders, filenames in os.walk(path):
    print('The current folder is ' + foldername)

    for subfolder in subfolders:
        print('Subfolder of ' + foldername +': ' + subfolder)

    for filename in filenames:
        print('File inside ' + foldername + ': ' + filename)

    print(' ')