import os
import sys
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
    l_gray = '\033[90m' 

def get_time(f):
    tm = os.stat(f).st_mtime
    r_dt = datetime.fromtimestamp(tm)
    dt = str(r_dt).split('.')[0]

    return colours.blue + dt + colours.reset

def get_size(f):
    return colours.yellow + str(os.stat(f).st_size) + colours.reset

args = sys.argv
width = 0

if len(args) > 1:
    try:
        os.chdir(args[1])
    except FileNotFoundError:
        print('Folder does not exist!')
        exit(0)
    except NotADirectoryError:
        print(f"{args[1]} is not a folder")
        exit(0)

try:
    width, _ = os.get_terminal_size()
except OSError as ose:
    pass


working_dir = os.getcwd()

files = os.listdir(working_dir)

dir_files = [[f, get_time(f), get_size(f)] for f in files]

i = 0

for f in dir_files:
    
    fs = f[0].split('.')
    curr_dir_file = fs[0]
    chg_flag = 0

    if len(curr_dir_file) + 32 > width and width != 0:
        curr_dir_file = curr_dir_file[: int(width + 14 - len(str(dir_files[i])))] + "..."
        chg_flag = 1    
    
    if len(fs) == 2:
        fname = curr_dir_file
        if chg_flag:
            fname = fname + "(" + fs[1] + ")"
        else:
            fname = fname + "." + fs[1]
        if fs[1] in ['exe', 'sh']:
            dir_files[i][0] = colours.purple + fname + colours.reset
        elif fs[1] in ['py', 'c', 'cs', 'cpp', 'html', 'css', 'js', 'go', 'java', 'r']:
            dir_files[i][0] = colours.cyan + fname + colours.reset
        elif fs[1] in ['md', 'json', 'cfg', 'xml', 'tex', 'txt', 'pdf']:
            dir_files[i][0] = colours.red + fname + colours.reset
    #    elif fs[1] in ['avif', 'svg', 'png', 'tiff', 'bmp', 'gif', 'jpeg', 'raw', 'eps', 'pct', 'pcx']:
    #        dir_files[i][0] = colours.l_gray + dir_files[i][0] + colours.reset
        else:
            dir_files[i][0] = fname
    else:
        if os.path.isdir(fs[0]):
            dir_files[i][0] = colours.green + curr_dir_file + colours.reset

    i += 1

dir_files.sort()
if width < 35 and width != 0:
    print(table([f[0] for f in dir_files]))
else:
    print(table(dir_files))
