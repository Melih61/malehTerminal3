import os
from colorama import Fore, Style
import shutil
import re

def strip_ansi(text):
    ansi_escape = re.compile(r'\x1b\[([0-9]+)(;[0-9]+)*m')
    return ansi_escape.sub('', text)

def run(args):
    if not args:
        path = os.getcwd()
    else:
        if os.path.exists(args[0]):
            path = args[0]
        else:
            print(f"ls: No such file or directory: {args[0]}")
            return

    term_width = shutil.get_terminal_size((80, 20)).columns

    entries = []
    for file in sorted(os.listdir(path)):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):
            color_file = Fore.GREEN + file + Style.RESET_ALL
        elif os.path.isdir(full_path):
            color_file = Fore.CYAN + file + Style.RESET_ALL
        else:
            color_file = file
        entries.append(color_file)

    visible_lengths = [len(strip_ansi(e)) for e in entries]
    max_len = max(visible_lengths, default=0) + 2
    cols = max(1, term_width // max_len)

    for i in range(0, len(entries), cols):
        row = entries[i:i+cols]
        for item in row:
            vis_len = len(strip_ansi(item))
            print(item + ' ' * (max_len - vis_len), end='')
        print()
