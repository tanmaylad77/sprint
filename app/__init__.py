"""
Sprint - Special print utility with color-coded tags and formatting.

A comprehensive Python printing utility that enhances console output with:
- Color-coded tags for different message types
- Automatic indentation detection
- Text wrapping with configurable line lengths
- Consistent formatting across all output

Author: Tanmay Lad
Contributors: Rolando Charles
"""

from .sprint import (
    printwork, printok, printfail, printwarn, 
    printdone, printinfo, printdebug
)

from .extras import (
    printblank, printheader, printtable, printlist
)

__version__ = "0.1.0"
__all__ = [
    "printwork", "printok", "printfail", "printwarn", 
    "printdone", "printinfo", "printdebug",
    "printblank", "printheader", "printtable", "printlist",
    "detect_code_indentation", "wrap_text", 
    "detect_indentation", "print_with_wrapping"
]
