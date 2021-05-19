import os
from tabulate import tabulate as table
from datetime import datetime

class colours:
    cyan   = '\033[96m'
    purple = '\033[95m'
    blue   = '\033[94m'
    green  = '\033[92m'
    yellow = '\033[93m'
    red    = '\033[91m' 
    reset  = '\033[0m'

def get_time(f):
    tm = os.stat(f).st_mtime
    r_dt = datetime.fromtimestamp(tm)
    dt = str(r_dt).split('.')[0]
    
    return colours.blue + dt + colours.reset

def get_size(f):
    return colours.yellow + str(os.stat(f).st_size) + colours.reset


working_dir = os.getcwd()

files = os.listdir(working_dir)

dir_files = [[f, get_time(f), get_size(f)] for f in files]

i = 0

for f in dir_files:
    if len(fs := f[0].split('.')) == 2:
        if fs[1] in ['exe', 'sh']:
            dir_files[i][0] = colours.purple + dir_files[i][0] + colours.reset
        elif fs[1] in ['py', 'c', 'cs', 'cpp', 'html', 'css', 'js', 'go', 'java', 'r']:
            dir_files[i][0] = colours.cyan + dir_files[i][0] + colours.reset
        elif fs[1] in ['md', 'json', 'cfg', 'xml', 'tex', 'txt']:
            dir_files[i][0] = colours.red + dir_files[i][0] + colours.reset
    else:
        if os.path.isdir(fs[0]):
            dir_files[i][0] = colours.green + dir_files[i][0] + colours.reset

    i += 1        

print(table(dir_files))

