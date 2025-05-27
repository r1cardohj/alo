""" 深度优先算法
"""
from os import listdir
from os.path import isfile, join
import argparse


def print_filename(start_dir):
    for file in sorted(listdir(start_dir)):
        fullpath = join(start_dir, file)
        if isfile(fullpath):
            print(file)
        else:
            print_filename(fullpath)

parser = argparse.ArgumentParser()
parser.add_argument("start_dir", help="any dir path")
args = parser.parse_args()
print(f"{args.start_dir} printing...")
print_filename(args.start_dir)
