#!/usr/bin/env python
# -*- coding: 850 -*-
# last time edited file on linux
# @utor: Leonardo Marcos Santiago
import os, fnmatch
from datetime import datetime, date

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


datetime_str = '2020-03-01 00:00:00'
datetime_object = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
	
for filename in find_files(os.getcwd(), '*'):
	last_time = datetime.fromtimestamp(os.path.getmtime(filename)).strftime('%Y-%m-%d %H:%M:%S')
	last_time_object = datetime.strptime(last_time, '%Y-%m-%d %H:%M:%S')
	if(last_time_object > datetime_object):
		print(last_time, '->', filename)
