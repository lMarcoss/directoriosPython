#!/usr/bin/env python
# -*- coding: 850 -*-
# last time edited file on linux
# @utor: Leonardo Marcos Santiago
import os, fnmatch
from datetime import datetime

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


lista = []
for filename in find_files(os.getcwd(), '*'):
	last_time = datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%d %H:%M:%S')
	print(last_time, '->', filename)
	
	
