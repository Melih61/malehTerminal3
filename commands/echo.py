
def run(args):
    if not args:
        print("")
    else:
        message = ""
        for word in args:
            message += " " + word
        print(str(message.strip()))
