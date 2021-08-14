import argparse
import os
import re
from os.path import isfile, join

parser = argparse.ArgumentParser("bulk_rename", description="Bulk File Rename")
parser.add_argument('-p', dest='path', help='Path to the folder with files to be renamed', default=".")
parser.add_argument('-r', dest='regex', help='Regular Expression', default="")
parser.add_argument('-n', dest='new', help='Replace string', default="")
parser.add_argument('-a', dest='apply', action='store_true', default=False, help='Apply changes')
args = parser.parse_args()


def main():
    for file_name in os.listdir(args.path):
        if isfile(join(args.path, file_name)):
            p = re.compile(args.regex)
            new_file_name = re.sub(p, args.new, file_name)
            if file_name != new_file_name:
                print(f"origin: {file_name}\t\tnew_file_name: {new_file_name}")
                if args.apply:
                    os.rename(file_name, new_file_name)


if __name__ == "__main__":
    main()
