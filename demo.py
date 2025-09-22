#!/usr/bin/env python3
# -*- coding: utf-8 -*-

\"\"\"
GitHub Tools Demo Script
This script demonstrates basic Python functionality.
\"\"\"

def greet(name):
    \"\"\"
    Greet a person by name.
    
    Args:
        name (str): The name of the person to greet.
        
    Returns:
        str: A greeting message.
    \"\"\"
    return f\"Hello, {name}! Welcome to the GitHub Tools Demo.\"

def add_numbers(a, b):
    \"\"\"
    Add two numbers together.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
        
    Returns:
        int or float: The sum of a and b.
    \"\"\"
    return a + b

if __name__ == \"__main__\":
    # Demo the functions
    print(greet(\"User\"))
    print(f\"5 + 3 = {add_numbers(5, 3)}\")