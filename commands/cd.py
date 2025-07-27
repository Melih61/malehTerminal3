import os

def run(args):
    if not args:
        path = os.path.expanduser("~")
    else:
        if os.path.exists(args[0]):
            path = args[0]
        else:
            print("cd: Der angegebene Path existiert nicht")
            return
    os.chdir(path)
