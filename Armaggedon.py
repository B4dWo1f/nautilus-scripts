#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
HOME = os.environ['HOME']
USER = os.environ['USER']
HOSTNAME = os.uname()[1]

FILE_PATH = os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS'].strip()
SELECTD_URI = os.environ['NAUTILUS_SCRIPT_SELECTED_URIS'].strip()
CURRENT_URI = os.environ['NAUTILUS_SCRIPT_CURRENT_URI'].strip()
WINDOW_GEO = os.environ['NAUTILUS_SCRIPT_WINDOW_GEOMETRY'].strip()


with open(f'{HOME}/nautilus.log','w') as f:
   f.write(HOSTNAME+', '+USER+', '+HOME+'\n')
   f.write(f'*{FILE_PATH}*\n')
   f.write(f'*{SELECTD_URI}*\n')
   f.write(f'*{CURRENT_URI}*\n')
   f.write(f'*{WINDOW_GEO}*\n\n')
f.close()
