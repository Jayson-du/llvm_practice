import os
import platform
import subprocess
import argparse
import string

def parseargs()->string:
    parser = argparse.ArgumentParser()
    parser.add_argument("option", type=str,
                        help="build llvm_practice or clean non git control files or directorys")
    args = parser.parse_args()

    return args.option

def build_item(system, abspath):

    # create build and remove CMakeCache.txt
    build_dir = abspath + "/build"
    cmakecache = build_dir + "/CMakeCache.txt"

    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    if os.path.exists(cmakecache):
        os.remove(cmakecache)

    #  judge platform && execute build script
    if system == "Linux":
        command = "sh " + "./script/linux/build.sh " + abspath
        os.system(command)

    elif system == "Windows":
        command = abspath + "\\script\\windows\\build.cmd " + abspath
        os.system(command)
    else:
        print("except windows && linux, other OS are not support")

def clean_item(system, abspath):

    #  judge platform && execute build script
    if system == "Linux":
        command = "sh " + "./script/linux/clean.sh " + abspath
        os.system(command)
    elif system == "Windows":
        command = abspath + "\\script\\windows\\clean.cmd " + abspath
        os.system(command)
    else:
        print("except windows && linux, other OS are not support")

def main():
    system = platform.system()
    abspath = os.path.abspath(os.path.dirname(__file__))

    # 1. analysis input args
    option = parseargs()

    if option == "build":
        print("cmake build llvm_practice x64")
        build_item(system, abspath)
    elif option == "clean":
        print("clean non git control files or directorys")
        clean_item(system, abspath)
    else:
        print("unknow command, please input '/build'/ or '/clean/'/")


if __name__=="__main__":
    main()