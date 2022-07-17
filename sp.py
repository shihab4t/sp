#!/usr/bin/env python3

from os import system, rename
import re
from sys import argv


def help() -> str:
    return """sp

Automation script for Sport Programmer aka. Competitive Programmer

commands:
-------------
<file name>  ----------------------------------------  Create file with $HOME/.sp/template.cpp
<file name> with ------------------------------------  Create file with row customization
update <template name>  -----------------------------  update template in $HOME/.sp/template.cpp
run <file name>  ------------------------------------  Run C/C++ code with runtime info
compile <file name>  --------------------------------  Compile C/C++ with log details
cfst  <numeric series> <alphabetical series>  -------  Problem submission status
cfre <file name> <problem numeric series>  ----------  Rename codeforces with specific formatting
atre <file name> <problem series>  ------------------  Rename atcoder with specific formatting
help, --help  ---------------------------------------  For help
    """


if __name__ == "__main__":
    argc = len(argv)

    if argc == 1 or argv[1] == "help" or argv[1] == "--help":
        print(help())

    elif argv[1] == "update":
        template_name = argv[2]
        system(f"cp -v {template_name} $HOME/.sp/template.cpp")

    elif argv[1] == "run":
        file_name = argv[2]
        system(f"g++ {file_name} && ./a.out")

    elif argv[1] == "compile":
        file_name = argv[2]
        system(f"g++ -v {file_name}")

    elif argv[1] == "cfst":
        numeric_series = argv[2]
        alphabetical_series = argv[3]
        command = f'google-chrome "https://codeforces.com/problemset/status/{numeric_series}' + \
                  f'/problem/{alphabetical_series}?friends=on" &'
        system(command)

    elif argv[1] == "cfre":
        old_file_name = argv[2]
        numeric_series = argv[3]
        file_name = re.sub("_", ".", old_file_name, 1)
        file_name = str(numeric_series) + file_name
        print(old_file_name, file_name)
        rename(old_file_name, file_name)

    elif argv[1] == 'atre':
        old_file_name = argv[2]
        numeric_series = argv[3]
        file_name = old_file_name[4:]
        # print(old_file_name, file_name)
        file_name = str(numeric_series) + "." + file_name
        print(old_file_name, file_name)
        rename(old_file_name, file_name)

    elif argc >= 3 and argv[2] == "with":
        file_name = argv[1]
        file_name = re.sub("\s", "_", file_name)
        file_name = re.sub("._", ".", file_name, 1)

        open_flag = True
        if argc >= 3:
            if argv[2] == "no":
                open_flag = False
            else:
                file_name += "." + argv[2]

        print(f"Creating the {file_name} file...")
        system(f"cp ~/.sp/template.cpp {file_name}")
        system(f"date '+%A, %B %d, %Y | %r (%Z)' >> {file_name}")
        print("Done! let's play")

        if open_flag:
            open_flag = not(argc >= 4 and argv[3] == "no")

        if open_flag:
            system(f"code {file_name}")
    else:
        file_name = argv[1]
        print(f"Creating the {file_name} file...")
        system(f"cp ~/.sp/template.cpp {file_name}")
        system(f"date '+%A, %B %d, %Y | %r (%Z)' >> {file_name}")
        print("Done! let's play")

        open_flag = True
        if open_flag:
            open_flag = not(argc >= 4 and argv[3] == "no")
        if open_flag:
            system(f"code {file_name}")
