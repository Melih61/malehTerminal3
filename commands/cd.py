import os

def run(args):
    if not args:
        path = os.path.expanduser("~")
    else:
        if os.path.exists(args[0]):
            path = args[0]
        else:
            print(f"cd: No such file or directory: {args[0]}")
            return
    os.chdir(path)
