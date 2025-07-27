import os
import shutil

def run(args):
    if not args:
        print("mv: Invalid arguments")
        return
    try:
        path = args[0]
        destination = args[1]
    except IndexError:
        print("mv: Invalid arguments")
        return
    if os.path.exists(path):
        if os.path.exists(destination):
            try:
                shutil.move(path, destination)
            except IOError:
                print(f"mv: File or directory {path} is being used")
        else:
            print(f"mv: No such file or directory: {destination}")
            return
    else:
        print(f"mv: No such file or directory: {path}")
