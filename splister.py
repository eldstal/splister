#/bin/env python3

import os
import sys
import argparse

# Returns filename,count
def file_params(conf, index):

    prefix = conf.output
    if not prefix:
        prefix = os.path.basename(conf.input)

    if prefix == "-":
        prefix = "splister"

    if prefix.endswith(os.path.sep):
        prefix += "splister"

    count = conf.start * conf.base**index
    filename = f"{prefix}-{index:>03}-{count}.txt"

    return (filename, count)

def main():

    parser = argparse.ArgumentParser("Split a wordlist into exclusive chunks")

    parser.add_argument("-n", "--start", type=int, default=100, help="Size (in lines) of the first file.")
    parser.add_argument("-b", "--base", type=int, default=10, help="Size factor (in lines) of each additional file. Base 1 for equal size files. Base 2: n, n*2, n*4, n*8, ...")
    parser.add_argument("-o", "--output", type=str, default=None, help="Output filename prefix, including path. Default: autogenerate. result/abc will yield files result/abc-00-100.txt, result/abc-01-1000.txt, ...")
    parser.add_argument("input", type=str, nargs="?", default="-", help="Input file to split, - for stdin")

    conf = parser.parse_args()

    assert(conf.start > 0)
    assert(conf.base > 0)



    infile = None
    if conf.input == "-":
        infile = sys.stdin
    else:
        infile = open(conf.input, "r")


    current_index = -1
    current_threshold = 0
    current_line = 0

    for l in infile.readlines():

        current_line += 1
        if current_line > current_threshold:
            current_index += 1
            out_filename, current_threshold = file_params(conf, current_index)
            print(out_filename)

            outdir = os.path.dirname(out_filename)
            os.makedirs(outdir, exist_ok=True)
            outfile = open(out_filename, "w+")

        
        outfile.write(l)

if __name__ == "__main__":
    sys.exit(main())
