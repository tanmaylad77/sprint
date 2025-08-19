"""
Utility functions for the Sprint printing library.

This module provides core utility functions including:
- Automatic code indentation detection
- Text wrapping with proper formatting
- Helper functions for the main sprint printing functions

Author: Tanmay Lad
Contributors: Rolando Charles
"""

# Standard library imports
import inspect
import textwrap
import os

# Local imports
from sprint_config import COLORS, STYLES, default_l_pad_char, default_max_line_len

def detect_code_indentation():
    """Automatically detect the indentation level based on the calling code context."""
    try:
        # Get the current frame
        current_frame = inspect.currentframe()
        if not current_frame:
            return 0
        
        # Go up three levels: 
        # 1. out of _detect_code_indentation
        # 2. out of _print_with_wrapping  
        # 3. out of the sprint function (printinfo, printok, etc.)
        caller_frame = current_frame.f_back
        if not caller_frame:
            return 0
        
        # Go up one more level to get out of _print_with_wrapping
        wrapper_frame = caller_frame.f_back
        if not wrapper_frame:
            return 0
        
        # Go up one more level to get out of the sprint function
        actual_caller_frame = wrapper_frame.f_back
        if not actual_caller_frame:
            return 0
        
        # Get the filename and line number
        filename = actual_caller_frame.f_code.co_filename
        lineno = actual_caller_frame.f_lineno
        
        # Skip if it's not a real file
        if not os.path.exists(filename) or filename == '<stdin>':
            return 0
        
        # Read the source file
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if lineno <= 0 or lineno > len(lines):
            return 0
        
        # Get the calling line (1-indexed to 0-indexed)
        calling_line_idx = lineno - 1
        calling_line_content = lines[calling_line_idx]
        
        # Count leading spaces to get the actual indentation level
        leading_spaces = len(calling_line_content) - len(calling_line_content.lstrip())
        
        # Convert to indentation level (assuming 2 spaces per level)
        result = leading_spaces // 2
        
        return result
        
    except Exception as e:
        return 0

def wrap_text(text, max_length, lpad, tag_length):
    """Helper function to wrap text while preserving indentation and tag formatting."""
    # Handle None or empty text
    if text is None:
        text = ""
    
    # Calculate available space for text after tag and padding
    available_width = max_length - len(lpad) - tag_length - 1  # -1 for the space after tag
    
    if available_width <= 0:
        # If no space available, just return the original
        return [text]
    
    # Wrap the text
    wrapped_lines = textwrap.wrap(text, width=available_width, break_long_words=False, break_on_hyphens=False)
    
    if not wrapped_lines:
        return [text]
    
    return wrapped_lines

def detect_indentation(text):
    """Automatically detect indentation level from text content."""
    if not text:
        return 0
    
    # Find the first non-empty line
    lines = text.split('\n')
    for line in lines:
        if line.strip():  # Skip empty lines
            # Count leading spaces/tabs
            indent = len(line) - len(line.lstrip())
            # Convert to indentation level (assuming 2 spaces per level)
            return indent // 2
    
    return 0

def print_with_wrapping(tag, text, lvl=0, l_pad_char=default_l_pad_char, max_line_length=default_max_line_len, bold=False, auto_detect=True):
    """Helper function to print with proper wrapping and formatting."""
    # Auto-detect code indentation if level is 0 and auto_detect is True
    if lvl == 0 and auto_detect:
        lvl = detect_code_indentation()
    
    # If still 0, try text-based indentation detection
    if lvl == 0 and text and text.startswith((' ', '\t')):
        lvl = detect_indentation(text)
    
    lpad = ""
    for t in range(lvl):
        lpad += l_pad_char
    
    # Calculate tag length (including color codes)
    tag_with_colors = tag
    tag_clean = tag.replace(COLORS['BLUE'], "").replace(COLORS['GREEN'], "").replace(COLORS['RED'], "").replace(COLORS['YELLOW'], "").replace(COLORS['MAGENTA'], "").replace(STYLES['RESET'], "")
    tag_length = len(tag_clean)
    
    # Apply bold formatting if requested
    if bold:
        text = STYLES['BOLD'] + text + STYLES['RESET']
    
    # Wrap the text
    wrapped_lines = wrap_text(text, max_line_length, lpad, tag_length)
    
    # Print each wrapped line
    for i, line in enumerate(wrapped_lines):
        if i == 0:
            # First line gets the tag
            print(lpad + tag + " " + line)
        else:
            # Subsequent lines get indented to align with the text after the tag
            print(lpad + " " * (tag_length + 1) + line)
