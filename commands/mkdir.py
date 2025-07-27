import os

def run(args):
    if not args:
        print("mkdir: Invalid arguments")
        return
    for directory in args:
        try:
            os.mkdir(directory)
            print(f"{directory} was created")
        except FileExistsError:
            print(f"mkdir: Cannot create directory {directory}: File exists")
        except Exception as e:
            print(f"mkdir: Error: {e}")
