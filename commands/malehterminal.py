from terminal import check_update

def update():
    print("Starting update")

def get_info():
    print("malehTerminal")
    print("Version: 3")
    print("Release: 27.07.2025")
    print("Autor: maleh")
    print(f"Update verfügbar: {"Ja" if check_update() else "Nein"}")

def run(args):
    if not args:
        get_info()
    else:
        if len(args) == 1:
            if args[0].lower() == "update" or args[0].lower() == "-update" or args[0].lower() == "--update":
                update() if check_update() else print("Es ist momentan kein Update verfügbar")
            elif args[0].lower() == "help" or args[0].lower() == "-help" or args[0].lower() == "--help":
                print("malehTerminal commands:\n--info: informations about malehTerminal")
                print("--update: update malehTerminal")
            elif args[0].lower() == "info" or args[0].lower() == "-info" or args[0].lower() == "--info":
                get_info()
            else:
                print(f"malehTerminal: Unexpected argument {args[0]}")
        else:
            get_info()