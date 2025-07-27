import os

def run(args):
    if not args:
        print("mkdir: Ungültige Argumente")
        return
    for directory in args:
        try:
            os.mkdir(directory)
            print(f"{directory} wurde erfolgreich erstellt")
        except FileExistsError:
            print(f"mkdir: Der Ordner {directory} existiert bereits")
        except Exception as e:
            print(f"mkdir: Fehler: {e}")
