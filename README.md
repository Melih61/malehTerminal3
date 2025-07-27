
# malehTerminal3
[![Version](https://img.shields.io/badge/version-3.0-blue)]()
[![Language](https://img.shields.io/badge/language-python-blue)]()

malehTerminal3 is my custom-built terminal, inspired by the classic Bash shell. I've recreated a range of standard commands, allowing users to interact with the system in a familiar way while showcasing the inner workings of a shell environment. Whether you're navigating directories, managing files, or running basic scripts, malehTerminal3 provides a streamlined and educational experience for command-line enthusiasts.


## Installation

Install malehTerminal using git and python

```bash
git clone https://github.com/Melih61/malehTerminal3.git
cd malehTerminal3
pip install -r requirements.txt
python terminal.py
```
    
## Configuration

After the first start of the terminal a file namend .malehterminalrc will be created in your home directory which you can edit to customize the terminal

```bash
nvim ~/.malehterminalrc
```

After opening the file with your favorite text editor you will see this and can change or add whatever your want

```python
PROMPT_STYLE="$USER@$OS $DIR$ "
USER_COLOR="red"
OS_COLOR="red"
DIR_COLOR="cyan"
SHOW_UPDATE_NOTIFICATION="true"
```
## Authors

- [@Melih61](https://github.com/Melih61)

