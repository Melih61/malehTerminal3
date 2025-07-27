import os

def run(args):
    if not args:
        print("rmdir: Ungültige Argumente")
        return
    for directory in args:
        try:
            os.rmdir(directory)
            print(f"{directory} wurde erfolgreich gelöscht")
        except FileNotFoundError:
            print(f"rmdir: Der Ordner {directory} existiert nicht")
        except Exception as e:
            print(f"rmdir: Fehler: {e}")
