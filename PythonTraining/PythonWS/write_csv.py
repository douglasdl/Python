# -*- coding: utf-8 -*-

import os

dir_path = '/home/pi/Desktop'

filename = 'test'

if not os.path.exists(dir_path):
    os.makedirs(dir_path)
f = open(dir_path + '/' + filename + '.csv', 'a')
f.write("'" + str(1) + ", abc, def\n")
f.close()