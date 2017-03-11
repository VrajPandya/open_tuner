#!/usr/bin/pyrhon3

import sys
import getopt
import ot_util.print_helper as _print
import context

print("started open tuner")

def print_help():
    _print.ot_print("usage: " + sys.argv[0] + "--input_file=<input_file> --output_file=<output_file>")
    sys.exit()


def process_cmd_args(argv):
    short_opts = "h"
    long_opts = ["kernel=", "input_file=", "out_file="]

    cur_context = OtContext

    try:
        opts, args = getopt.getopt(argv, short_opts, long_opts)
    except getopt.GetoptError:
        print_help()
    for opt, arg in opts:
        if opt == "h":
            print_help()
        elif opt in ("--input_file"):
            kernel_file = arg
        elif opt in ("--kernel_name"):
            kernel_name = arg

    return




def main(argv):
    process_cmd_args()

    return

if __name__ == '__main__':
    main(sys.argv)