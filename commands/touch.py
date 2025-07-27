import os

def run(args):
    if not args:
        print("touch: Ungültige Argumente")
        return
    path = args[0]
    if os.path.exists(path) and os.path.isfile(path):
        print(f"touch: Die Datei {path} existiert bereits")
    else:
        with open(path, "w"):
            pass
        print(f"Die Datei {path} wurde erfolgreich erstellt")
