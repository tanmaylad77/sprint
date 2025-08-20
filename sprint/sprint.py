"""
Special print utility (Sprint)

A comprehensive Python printing utility that enhances console output with:
- Color-coded tags for different message types
- Automatic indentation detection
- Text wrapping with configurable line lengths
- Consistent formatting across all output

Author: Tanmay Lad
Contributors: Rolando Charles

This module provides various print functions that work like print() but add
fixed-width, color-coded tags like [ WARN ], [  OK  ], etc., with automatic
indentation detection and text wrapping capabilities.

Useful for console debugging, verbose modes, and creating professional-looking
command-line interfaces.
"""
from .config import COLORS, STYLES, default_l_pad_char, default_max_line_len

from .utils import *

## In the printing functions below:
# 's' -> string to print
# 'lvl' -> [int] indentation level (optional, default = 0, auto-detected if 0)
# 'l_pad_char' -> left pad indentation character or string (optional, default = " ")
# 'max_line_length' -> maximum line length before wrapping (optional, default = default_max_line_length)
# 'bold' -> [bool] whether to print text in bold (optional, default = False)
# 'auto_detect' -> [bool] whether to auto-detect code indentation (optional, default = True)

def printwork(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print a work-in-progress message with a blue dot icon."""
    tag = "[" + COLORS['BLUE'] + " .... " + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)

def printok(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print a success message with a green OK tag."""
    tag = "[" + COLORS['GREEN'] + "  OK  " + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)

def printfail(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print a failure message with a red FAILED tag."""
    tag = "[" + COLORS['RED'] + "FAILED" + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)

def printwarn(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print a warning message with a yellow WARN tag."""
    tag = "[" + COLORS['YELLOW'] + " WARN " + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)

def printdone(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print a completion message with a green DONE tag."""
    tag = "[" + COLORS['GREEN'] + " DONE " + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)

def printinfo(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print an informational message with a blue INFO tag."""
    tag = "[" + COLORS['BLUE'] + " INFO " + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)

def printdebug(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print a debug message with a magenta DEBUG tag."""
    tag = "[" + COLORS['MAGENTA'] + "DEBUG" + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)

def printsuccess(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print a success message with a checkmark icon."""
    tag = "[" + COLORS['GREEN'] + " ✓ " + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)

def printerror(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print an error message with an X icon."""
    tag = "[" + COLORS['RED'] + " ✗ " + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)

def printprogress(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print a progress message with a spinner icon."""
    tag = "[" + COLORS['CYAN'] + " ⟳ " + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)

def printquestion(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print a question message with a question mark icon."""
    tag = "[" + COLORS['MAGENTA'] + " ? " + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)

def printstep(step_num, total_steps, s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Print a step message with step counter."""
    step_info = f"Step {step_num}/{total_steps}"
    tag = "[" + COLORS['CYAN'] + f" {step_info} " + STYLES['RESET'] + "]"
    print_with_wrapping(tag, s, lvl, l_pad_char, max_line_length, bold, auto_detect)