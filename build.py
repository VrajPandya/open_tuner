import os
import subprocess
import shutil


def install_package():

    return


def check_available_packages():
    commands = ["cmake", "make", "gcc", "g++"]

    for c in commands:
        available = False if (shutil.which(c) is None) else True
        if available:
            continue
        else:
            print(c + " is not available please install it and run the build again")
            exit(1)

    return


def create_benchmark_build_files():
    return


def build_benchmarks():
    return


def create_build_files():
    try:
        subprocess.call(["cmake", ".", "-G", "Unix Makefiles", "-Bbuild/", "-H."])

        print("Build Files Generated")
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print(os.errno.ENOENT)
        else:
            print(Exception)
            raise
    #os.system()

    return


def build():
    shutil.which("make")
    print("Building project")

    return


def main():
    check_available_packages()

    create_benchmark_build_files()
    build_benchmarks()

    create_build_files()
    build()

    return

if __name__ == '__main__':
    main()
