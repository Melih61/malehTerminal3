import os

def run(args):
    if not args:
        print("touch: Invalid arguments")
        return
    path = args[0]
    if os.path.exists(path) and os.path.isfile(path):
        print(f"touch: Cannot create file {path}: File exists")
    else:
        with open(path, "w"):
            pass
        print(f"File {path} was created")
