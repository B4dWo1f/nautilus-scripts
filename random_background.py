#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os

f = ['/home/n03l/Pictures/2019_01_29_ciervos/IMG_20190129_104245.jpg',
     '/home/n03l/Pictures/2019_01_29_ciervos/IMG_20190129_104125.jpg']

com = 'gsettings set org.gnome.desktop.background picture-uri file://%s'%(f)
os.system(com)
