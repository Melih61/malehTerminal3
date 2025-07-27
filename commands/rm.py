import os

def run(args):
    if not args:
        print("rm: Invalid arguments")
        return
    path = args[0]
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
            print(f"File {path} was deleted")
        else:
            print(f"rm: {path} is a folder")
            return
    else:
        print(f"rm: No such file or directory: {path}")
        return

