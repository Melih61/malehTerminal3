import os

def run(args):
    if not args:
        print("rmdir: Invalid arguments")
        return
    for directory in args:
        try:
            os.rmdir(directory)
            print(f"{directory} was deleted")
        except FileNotFoundError:
            print(f"rmdir: No such file or directory: {directory}")
        except Exception as e:
            print(f"rmdir: Error: {e}")
