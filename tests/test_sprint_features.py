#!/usr/bin/env python3
"""
Test script for the enhanced sprint.py features.
Demonstrates the completed TODOs: bold option and automatic indentation detection.
"""

from sprint import *
from sprint_extras import *

def test_bold_feature():
    """Test the new bold text feature."""
    printheader()
    printinfo("Testing Bold Text Feature", bold=True)
    printheader()
    
    printwork("This is a work message in bold", bold=True)
    printok("This is a success message in bold", bold=True)
    printfail("This is a failure message in bold", bold=True)
    printwarn("This is a warning message in bold", bold=True)
    printinfo("This is an info message in bold", bold=True)
    printdebug("This is a debug message in bold", bold=True)
    printdone("This is a done message in bold", bold=True)
    
    # Test with different indentation levels
    printinfo("Level 1 indentation", lvl=1, bold=True)
    printinfo("Level 2 indentation", lvl=2, bold=True)
    printinfo("Level 3 indentation", lvl=3, bold=True)

def test_automatic_indentation():
    """Test the automatic indentation detection feature."""
    printheader()
    printinfo("Testing Automatic Indentation Detection", bold=True)
    printheader()
    
    # Text with leading spaces (should auto-detect indentation)
    indented_text = "  This text has leading spaces and should auto-detect indentation level"
    printinfo(indented_text)  # Should auto-detect level 1
    
    more_indented_text = "    This text has more leading spaces and should auto-detect level 2"
    printinfo(more_indented_text)  # Should auto-detect level 2
    
    # Text without leading spaces (should use default level 0)
    normal_text = "This text has no leading spaces"
    printinfo(normal_text)  # Should use level 0
    
    # Mixed indentation
    mixed_text = "  Mixed indentation with\n    multiple lines\n      at different levels"
    printinfo(mixed_text)  # Should auto-detect based on first line

def test_code_indentation_detection():
    """Test the new automatic code indentation detection feature."""
    printheader()
    printinfo("Testing Automatic Code Indentation Detection", bold=True)
    printheader()
    
    # Level 0 - no indentation
    printinfo("This should be at level 0 (no indentation)")
    
    # Level 1 - inside if statement
    if True:
        printinfo("This should be at level 1 (inside if)")
        printok("Success at level 1")
    
    # Level 2 - nested inside if
    if True:
        if True:
            printinfo("This should be at level 2 (nested if)")
            printwarn("Warning at level 2")
    
    # Level 3 - deeply nested
    if True:
        if True:
            if True:
                printinfo("This should be at level 3 (deeply nested)")
                printfail("Failure at level 3")
    
    # Test with loops
    for i in range(2):
        printinfo(f"Loop iteration {i} at level 1")
        
        for j in range(2):
            printinfo(f"Nested loop {i},{j} at level 2")
            
            if i == j:
                printok(f"Match found at level 3")
    
    # Test manual override
    if True:
        printinfo("Auto-detected level 1")
        printinfo("Manual override to level 0", lvl=0)
        printinfo("Manual override to level 3", lvl=3)
        printinfo("Back to auto-detection")

def test_new_utility_functions():
    """Test the new utility functions added to sprint.py."""
    printheader()
    printinfo("Testing New Utility Functions", bold=True)
    printheader()
    
    # Test new print functions
    printsuccess("Operation completed successfully!")
    printerror("An error occurred during processing")
    printprogress("Processing data...")
    printquestion("Do you want to continue?")
    
    # Test step counter
    printstep(1, 5, "Initializing system")
    printstep(2, 5, "Loading configuration")
    printstep(3, 5, "Processing data")
    printstep(4, 5, "Generating reports")
    printstep(5, 5, "Cleanup and exit")
    
    # Test table printing
    printheader()
    printinfo("Testing Table Printing", bold=True)
    
    headers = ["Name", "Age", "City", "Status"]
    rows = [
        ["Alice", "25", "London", "Active"],
        ["Bob", "30", "Paris", "Inactive"],
        ["Charlie", "35", "Berlin", "Active"],
        ["Diana", "28", "Rome", "Pending"]
    ]
    
    printtable(headers, rows, lvl=1)
    
    # Test list printing
    printheader()
    printinfo("Testing List Printing", bold=True)
    
    items = ["First item", "Second item", "Third item", "Fourth item"]
    printlist(items, title="Sample List", lvl=1, numbered=True)
    
    printlist(items, title="Bullet List", lvl=1, numbered=False)

def test_combined_features():
    """Test combining multiple features together."""
    printheader()
    printinfo("Testing Combined Features", bold=True)
    printheader()
    
    # Bold text with auto-indentation
    complex_text = "  This is a complex message that combines:\n    - Bold formatting\n    - Auto-indentation\n    - Text wrapping\n    - Multiple lines"
    printinfo(complex_text, bold=True)
    
    # Bold text with manual indentation
    printinfo("Manual indentation with bold", lvl=2, bold=True)
    
    # Long text that will wrap
    long_text = "This is a very long message that will definitely exceed the default line length and demonstrate the text wrapping functionality while maintaining proper formatting and indentation."
    printwarn(long_text, bold=True, max_line_length=60)
    
    # Code indentation with bold
    if True:
        printinfo("Code indentation + bold", bold=True)
        
        if True:
            printwarn("Nested code indentation + bold", bold=True)

def test_edge_cases():
    """Test edge cases and error handling."""
    printheader()
    printinfo("Testing Edge Cases", bold=True)
    printheader()
    
    # Empty string
    printinfo("", bold=True)
    
    # Very short text
    printinfo("Hi", bold=True)
    
    # Text with special characters
    printinfo("Special chars: !@#$%^&*()", bold=True)
    
    # Text with newlines
    multiline_text = "Line 1\n  Line 2\n    Line 3"
    printinfo(multiline_text, bold=True)
    
    # Disable auto-detection
    if True:
        printinfo("Auto-detection enabled (default)")
        printinfo("Auto-detection disabled", auto_detect=False)

def test_auto_detection_control():
    """Test controlling the auto-detection feature."""
    printheader()
    printinfo("Testing Auto-Detection Control", bold=True)
    printheader()
    
    # Test enabling/disabling auto-detection
    printinfo("Auto-detection is enabled by default")
    
    if True:
        printinfo("This should auto-detect level 1")
        printinfo("This should also auto-detect level 1")
        
        # Disable auto-detection for specific calls
        printinfo("Auto-detection disabled for this call", auto_detect=False)
        printinfo("Manual level 0", lvl=0, auto_detect=False)
        printinfo("Manual level 2", lvl=2, auto_detect=False)
        
        # Re-enable auto-detection
        printinfo("Auto-detection re-enabled")
    
    # Test with utility functions
    if True:
        headers = ["Feature", "Status"]
        rows = [["Auto-detection", "Working"], ["Manual Override", "Available"]]
        printtable(headers, rows)  # Should auto-detect level 1
        
        items = ["Feature 1", "Feature 2"]
        printlist(items, title="Features", auto_detect=False)  # Should use level 0

if __name__ == "__main__":
    print("=" * 80)
    print("SPRINT.PY ENHANCED FEATURES DEMONSTRATION")
    print("=" * 80)
    print()
    
    try:
        test_bold_feature()
        print()
        
        test_automatic_indentation()
        print()
        
        test_code_indentation_detection()
        print()
        
        test_new_utility_functions()
        print()
        
        test_combined_features()
        print()
        
        test_edge_cases()
        print()
        
        test_auto_detection_control()
        print()
        
        printheader()
        printsuccess("All tests completed successfully!", bold=True)
        printheader()
        printinfo("Key Features Demonstrated:")
        printinfo("  ✓ Bold text formatting")
        printinfo("  ✓ Text-based indentation detection")
        printinfo("  ✓ Code-based indentation detection")
        printinfo("  ✓ New utility functions")
        printinfo("  ✓ Auto-detection control")
        
    except Exception as e:
        printheader()
        printfail(f"Test failed with error: {e}", bold=True)
        printheader()
        import traceback
        traceback.print_exc()
