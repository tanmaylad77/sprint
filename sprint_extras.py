"""
Additional formatting functions for the Sprint printing library.

This module provides enhanced formatting capabilities including:
- Table printing with automatic column sizing
- List formatting with optional numbering
- Header separators and visual elements

Author: Tanmay Lad (2019)
Enhanced: Rolando Charles (2025)
"""

from sprint_config import COLORS, STYLES, default_l_pad_char, default_max_line_len
from sprint_utils import *

def printblank(s, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """
    Print a blank line with proper indentation and optional bold formatting.
    
    Args:
        s (str): The message string to print
        lvl (int, optional): Indentation level. Defaults to 0 (auto-detected).
        l_pad_char (str, optional): Left padding character. Defaults to "  ".
        max_line_length (int, optional): Maximum line length. Defaults to 80.
        bold (bool, optional): Whether to print in bold. Defaults to False.
        auto_detect (bool, optional): Auto-detect indentation. Defaults to True.
    """
    # Auto-detect code indentation if level is 0 and auto_detect is True
    if lvl == 0 and auto_detect:
        lvl = detect_code_indentation()
    
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    
    # For blank lines, we need to handle wrapping differently since there's no tag
    available_width = max_line_length - len(lpad)
    if available_width <= 0:
        available_width = 1
    
    # Apply bold formatting if requested
    if bold:
        s = STYLES['BOLD'] + s + STYLES['RESET']
    
    wrapped_lines = textwrap.wrap(s, width=available_width, break_long_words=False, break_on_hyphens=False)
    
    for line in wrapped_lines:
        print(lpad + "         " + line)

def printheader(lvl=0, l_pad_char=default_l_pad_char, line_length=default_max_line_len, auto_detect=True):
    """
    Print a horizontal separator line with proper indentation.
    
    Args:
        lvl (int, optional): Indentation level. Defaults to 0 (auto-detected).
        l_pad_char (str, optional): Left padding character. Defaults to "  ".
        line_length (int, optional): Length of the separator line. Defaults to 80.
        auto_detect (bool, optional): Auto-detect indentation. Defaults to True.
    """
    # Auto-detect code indentation if level is 0 and auto_detect is True
    if lvl == 0 and auto_detect:
        lvl = detect_code_indentation()
    
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    print(lpad + "=" * line_length)

def printtable(headers, rows, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, auto_detect=True):
    """
    Print a formatted table with automatic column sizing.
    
    Args:
        headers (list): List of column header strings
        rows (list): List of row data (each row is a list of values)
        lvl (int, optional): Indentation level. Defaults to 0 (auto-detected).
        l_pad_char (str, optional): Left padding character. Defaults to "  ".
        max_line_length (int, optional): Maximum line length. Defaults to 80.
        auto_detect (bool, optional): Auto-detect indentation. Defaults to True.
    """
    # Auto-detect code indentation if level is 0 and auto_detect is True
    if lvl == 0 and auto_detect:
        lvl = detect_code_indentation()
    
    if not rows:
        return
    
    # Calculate column widths
    col_widths = []
    for i, header in enumerate(headers):
        max_width = len(header)
        for row in rows:
            if i < len(row):
                max_width = max(max_width, len(str(row[i])))
        col_widths.append(max_width)
    
    # Create separator line
    separator = "+" + "+".join("-" * (width + 2) for width in col_widths) + "+"
    
    # Print header
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    
    print(lpad + separator)
    
    # Print headers
    header_row = "|" + "|".join(f" {header:<{width}} " for header, width in zip(headers, col_widths)) + "|"
    print(lpad + header_row)
    print(lpad + separator)
    
    # Print data rows
    for row in rows:
        formatted_row = "|" + "|".join(f" {str(cell):<{width}} " for cell, width in zip(row, col_widths)) + "|"
        print(lpad + formatted_row)
    
    print(lpad + separator)

def printlist(items, title=None, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, numbered=True, auto_detect=True):
    """
    Print a formatted list with optional title and numbering.
    
    Args:
        items (list): List of items to print
        title (str, optional): Optional title for the list. Defaults to None.
        lvl (int, optional): Indentation level. Defaults to 0 (auto-detected).
        l_pad_char (str, optional): Left padding character. Defaults to "  ".
        max_line_length (int, optional): Maximum line length. Defaults to 80.
        numbered (bool, optional): Whether to number the items. Defaults to True.
        auto_detect (bool, optional): Auto-detect indentation. Defaults to True.
    """
    # Auto-detect code indentation if level is 0 and auto_detect is True
    if lvl == 0 and auto_detect:
        lvl = detect_code_indentation()
    
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    
    if title:
        print(lpad + title)
        print(lpad + "-" * len(title))
    
    for i, item in enumerate(items, 1):
        if numbered:
            print(f"{lpad}{i}. {item}")
        else:
            print(f"{lpad}• {item}")
    
    if title:
        print()  # Add spacing after list