#!/usr/bin/pyrhon3

import sys
import parser
import argparse
from ot_util.print_helper import ot_print as _print
from context import ot_context


def process_cmd_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("kernel_name", type=str, help="Name of the kernel to be optimized")
    parser.add_argument("kernel_file", type=str, help="Name of the file in which the kernel is present")
    parser.add_argument("-o", "--output_file", type=str, default="p.out", help="Name of the optimized file")

    args = parser.parse_args()

    return ot_context.OtContext(args.kernel_file, args.kernel_name, args.output_file)


def main():
    cur_context = process_cmd_args()
    str(cur_context)
    return

if __name__ == '__main__':
    main()
    sys.exit()

