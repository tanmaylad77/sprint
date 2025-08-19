# Sprint Configuration and Common Imports
# Centralized configuration for all sprint modules

# Third-party imports
from colorama import Fore, Style, init

# Initialize colorama for cross-platform color support
init()

# Configuration variables
default_l_pad_char = "  "  # Default left-pad character is two spaces
default_max_line_len = 80   # Default maximum line length

# Color constants for consistent usage across modules
COLORS = {
    'BLUE': Fore.BLUE,
    'GREEN': Fore.GREEN,
    'RED': Fore.RED,
    'YELLOW': Fore.YELLOW,
    'MAGENTA': Fore.MAGENTA,
    'CYAN': Fore.CYAN,
    'RESET': Style.RESET_ALL,
    'BRIGHT': Style.BRIGHT
}

# Style constants for consistent usage across modules
STYLES = {
    'BOLD': Style.BRIGHT,
    'RESET': Style.RESET_ALL
}
