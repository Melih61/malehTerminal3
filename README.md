
# malehTerminal3
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![Version](https://img.shields.io/badge/version-3.0-blue)]()
[![Language](https://img.shields.io/badge/language-python-blue)]()

malehTerminal3 is a custom-built terminal inspired by the functionality and design of Bash. While it doesn't include the full range of Bash commands, it serves as a personal project where I experimented with shell-like features and attempted to replicate core behavior as closely as possible.

## Usage
Feel free to use, modify, and integrate the code into your own projects. It’s open-source and available for everyone to explore.

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

## Status
✅ Up to date. Updated on 27.07.2025


## Disclaimer
This is a learning project created for educational purposes and experimentation. Use at your own risk.

## Authors

- [@Melih61](https://github.com/Melih61)

