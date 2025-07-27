import os

def run(args):
    if not args:
        print("cat: Invalid arguments")
        return
    if os.path.exists(args[0]):
        if os.path.isfile(args[0]):
            try:
                with open(args[0], "r") as f:
                    content = f.read()
                    f.close()
                print(content)
            except PermissionError:
                print(f"cat: Cannot read file {args[0]}: No permission")
                return
            except Exception as e:
                print(f"cat: Error: {e}")
                return
        else:
            print(f"cat: {args[0]} is not a file")
            return
    else:
        print(f"cat: No such file or directory {args[0]}")
        return
