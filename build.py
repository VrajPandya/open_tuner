import os
import subprocess
import shutil
import sys
from ot_util.print_helper import ot_print


def install_package(pkg):
    #implement this at the very end
    ot_print("installing " + pkg)
    #install package
    ot_print("complete installing package")
    return


def check_available_packages():
    #list the commands that we need to check
    commands = ["cmake", "make", "gcc", "g++"]
    #windows_commands = []
    #unix_commands = []

    for c in commands:
        available = False if (shutil.which(c) is None) else True
        if available:
            continue
        else:
            ot_print(c + " is not available please install it and run the build again")
            sys.exit(1)

    return

def create_benchmark_build_files():
    return


def build_benchmarks():
    # add suport for multiple OS
    return


def create_build_files():
    ot_print("generating build files")
    try:
        subprocess.call(["cmake", ".", "-G", "Unix Makefiles", "-Bbuild/", "-H."])
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print(os.errno.ENOENT)
        else:
            print(Exception)
            raise
    #os.system()

    ot_print("completed generating build file")
    return


def build():
    ot_print("Building project")
    OT_PWD = OT_ROOT + "/build"
    os.chdir(OT_PWD)

    try:
        subprocess.call(["make", "all"])
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print(os.errno.ENOENT)
        else:
            print(Exception)
            raise
    ot_print("complete Building project")

    return

def create_test_build_file():
    return

def build_tests():

def main():
    check_available_packages()

    create_benchmark_build_files()
    build_benchmarks()

    create_build_files()
    build()

    create_test_build_file()
    build_tests()

    return

if __name__ == '__main__':
    main()
