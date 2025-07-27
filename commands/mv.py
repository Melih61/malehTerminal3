import os
import shutil

def run(args):
    if not args:
        print("mv: Ungültige Argumente")
        return
    try:
        path = args[0]
        destination = args[1]
    except IndexError:
        print("mv: Nicht genug Argumente")
        return
    if os.path.exists(path):
        if os.path.exists(destination):
            try:
                shutil.move(path, destination)
            except IOError:
                print(f"Die Datei {path} wird grade benutzt")
        else:
            print(f"Der Path {destination} existiert nicht")
            return
    else:
        print(f"Der Path {path} existiert nicht")
