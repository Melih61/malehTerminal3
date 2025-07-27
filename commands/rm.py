import os

def run(args):
    if not args:
        print("rm: Ungültige Argumente")
        return
    path = args[0]
    if os.path.exists(path):
        if os.path.isfile(path):
            os.remove(path)
            print(f"Die Datei {path} wurde gelöscht")
        else:
            print(f"{path} ist ein Ordner")
            return
    else:
        print(f"Die Datei {path} existiert nicht")
        return

