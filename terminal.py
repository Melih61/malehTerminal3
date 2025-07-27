from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion, WordCompleter, PathCompleter
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.formatted_text import FormattedText
from prompt_toolkit.document import Document
import importlib
import os
import getpass
import distro
import platform
from colorama import Fore
import shlex
from settings import get_settings, load_settings, create_settings
import re

create_settings()

history = InMemoryHistory()
path_completer = PathCompleter()

def get_dir():
    return os.getcwd()


settings = get_settings()

def get_prompt():
    prompt_style = settings["PROMPT_STYLE"]

    values = {
        "$USER": getpass.getuser(),
        "$OS": distro.id().capitalize() if platform.system().lower() == "linux" else platform.system(),
        "$DIR": get_dir(),
    }

    colors = {
        "$USER": settings["USER_COLOR"],
        "$OS": settings["OS_COLOR"],
        "$DIR": settings["DIR_COLOR"],
    }

    pattern = re.compile(r"\$USER|\$OS|\$DIR")

    result = []
    last_end = 0

    for match in pattern.finditer(prompt_style):
        start, end = match.span()
        var = match.group()

        if start > last_end:
            result.append(("", prompt_style[last_end:start]))

        result.append((f"fg:{colors[var]}", values[var]))

        last_end = end

    if last_end < len(prompt_style):
        result.append(("", prompt_style[last_end:]))

    return FormattedText(result)

def check_update():
    if settings["SHOW_UPDATE_NOTIFICATION"]:
        return True
    else:
        return False

class LastTokenPathCompleter(Completer):
    def __init__(self, **kwargs):
        self.path_completer = PathCompleter(**kwargs)
    
    def get_completions(self, document: Document, complete_event):
        text = document.text_before_cursor
        if not text or text[-1].isspace():
            last_token = ''
            new_document = Document(text=last_token, cursor_position=len(last_token))
        else:
            words = text.split(' ')
            last_token = words[-1]
            new_document = Document(text=last_token, cursor_position=len(last_token))

        for completion in self.path_completer.get_completions(new_document, complete_event):
            yield completion

completer = LastTokenPathCompleter(expanduser=True, min_input_len=0)

def main():
    session = PromptSession(completer=completer, history=history, complete_while_typing=True)

    print(Fore.RED + """
░█▄█░█▀█░█░░░█▀▀░█░█░▀█▀░█▀▀░█▀▄░█▄█░▀█▀░█▀█░█▀█░█░░░▀▀█
░█░█░█▀█░█░░░█▀▀░█▀█░░█░░█▀▀░█▀▄░█░█░░█░░█░█░█▀█░█░░░░▀▄
░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀░
      """ + Fore.RESET)
    if check_update():
        print(Fore.RED + "Update available!\nDownload update using\n" + Fore.WHITE + "> " + Fore.RED + "malehterminal update\n" + Fore.RESET)
    while True:
        try:
            inp = session.prompt(get_prompt())
        except KeyboardInterrupt:
            continue
        except EOFError:
            break

        if not inp.strip():
            continue

        parts = shlex.split(inp.strip())
        cmd, *args = parts

        if cmd == "exit":
            break

        try:
            module = importlib.import_module(f"commands.{cmd}")
            module.run(args)
        except ModuleNotFoundError:
            os.system(inp)
        except Exception as e:
            print(f"An error occured while executing '{cmd}': {e}")

if __name__ == "__main__":
    main()

