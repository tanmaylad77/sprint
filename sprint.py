# Special print utility (Sprint)
# Tanmay Lad 2019
# Works like print but adds a fixed-width tag like [ WARN ]
# with the short message colour-coded

# Useful for console debugging/verbose modes (console only)
from colorama import Fore, Style, init

init()

# Default left-pad character is a space
default_l_pad_char = "  "

## In the printing functions below:
# 's' -> string to print
# 'lvl' -> [int] indentation level (optional, default = 0)
# 'l_pad_char' -> left pad indentation character or string (optional, default = " ")

def printwork(s, lvl=0, l_pad_char=default_l_pad_char):
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    print(lpad + "[" + Fore.BLUE + " .... " + Style.RESET_ALL + "] " + s)


def printok(s, lvl=0, l_pad_char=default_l_pad_char):
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    print(lpad + "[" + Fore.GREEN + "  OK  " + Style.RESET_ALL + "] " + s)


def printfail(s, lvl=0, l_pad_char=default_l_pad_char):
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    print(lpad + "[" + Fore.RED + "FAILED" + Style.RESET_ALL + "] " + s)


def printwarn(s, lvl=0, l_pad_char=default_l_pad_char):
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    print(lpad + "[" + Fore.YELLOW + " WARN " + Style.RESET_ALL + "] " + s)


def printblank(s, lvl=0, l_pad_char=default_l_pad_char):
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    print(lpad + "         " + s)


def printdone(s, lvl=0, l_pad_char=default_l_pad_char):
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    print(lpad + "[" + Fore.GREEN + " DONE " + Style.RESET_ALL + "] " + s)


def printinfo(s, lvl=0, l_pad_char=default_l_pad_char):
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    print(lpad + "[" + Fore.BLUE + " INFO " + Style.RESET_ALL + "] " + s)
