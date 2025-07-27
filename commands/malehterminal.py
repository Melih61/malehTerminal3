from terminal import check_update

def update():
    print("Starting update")

def run(args):
    if not args:
        print("malehTerminal")
        print("Version: 3")
        print("Release: 27.07.2025")
        print("Autor: maleh")
        print(f"Update verfügbar: {"Ja" if check_update() else "Nein"}")
    else:
        if len(args) == 1:
            if args[0].lower() == "update" or args[0].lower() == "-update" or args[0].lower() == "--update":
                update() if check_update() else print("Es ist momentan kein Update verfügbar")
            elif args[0].lower() == "help" or args[0].lower() == "-help" or args[0].lower() == "--help":
                print("malehTerminal Befehle:\n--info: Informationen über malehTerminal")
                print("--update: malehTerminal aktualisieren")
            elif args[0].lower() == "info" or args[0].lower() == "-info" or args[0].lower() == "--info":
                print("malehTerminal")
                print("Version: 3")
                print("Release: 27.07.2025")
                print("Autor: maleh")
                print(f"Update verfügbar: {"Ja" if check_update() else "Nein"}")
            else:
                print(f"malehTerminal: Befehl {args[0]} nicht gefunden")
        else:
            print("malehTerminal: Ungültige Argumente")