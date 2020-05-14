#!/usr/bin/python3

import os, sys
import gzip
import shutil

tmp_file = 'tmp.txt'

def gunzip_shutil(source_filepath, dest_filepath, block_size=65536):
    with gzip.open(source_filepath, 'rb') as s_file, \
            open(dest_filepath, 'wb') as d_file:
        shutil.copyfileobj(s_file, d_file, block_size)
        
def read_n_search(file, key_word):
    line_num = 0
    with open(file, 'r') as f:
        for line in f.readlines():
            line_num = line_num + 1
            if key_word in line:
                print ('%d %s' %(line_num, line))

def loop_dir(path, key_word):
    files = os.listdir(path)
    for file in files:
        if not file.endswith('.gz'):
            continue
        print ('=== Searching %s ===' %file)
        gunzip_shutil(file, tmp_file)
        read_n_search(tmp_file, key_word)
        os.remove(tmp_file)
        print ('=== Searched %s ===' %file)

def main(argv):
    loop_dir(argv[1], argv[2])
    print ('All search finished')

if __name__ == '__main__':
    main(sys.argv)