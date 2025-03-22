import os
import sys
import shutil

# Updated dictionary of tools for Linux GNOME
# Added 'foreground' flag to indicate if the tool should run in the foreground
tools_dict = {
    "list": {"command": "ls -la", "foreground": True},
    "calculator": {"command": "gnome-calculator", "foreground": False},
    "paint": {"command": "pinta", "foreground": False},
    "terminal": {"command": "gnome-terminal", "foreground": False},
    "python": {"command": "python3", "foreground": True},
    "git": {"command": "git --version", "foreground": True},
    "vscode": {"command": "code", "foreground": False},
    "chrome": {"command": "google-chrome", "foreground": False},
    "firefox": {"command": "firefox", "foreground": False},
    "filemanager": {"command": "nautilus", "foreground": False},
    "htop": {"command": "htop", "foreground": True}  # Added htop
}

def get_top_matches(search_term, limit=9):
    """Get top matching tools based on search term using basic string matching"""
    matches = []
    search_term = search_term.lower()
    
    for tool in tools_dict.keys():
        tool_lower = tool.lower()
        if not search_term or search_term in tool_lower:
            score = 100 if search_term == tool_lower else (50 if search_term in tool_lower else 0)
            matches.append((tool, score))
    
    matches.sort(key=lambda x: (-x[1], x[0]))
    return matches[:limit]

def clear_screen():
    """Clear the console screen"""
    os.system('clear')

def main():
    search_term = ""
    
    while True:
        clear_screen()
        print("Tool Search (Press Ctrl+C to exit)")
        print(f"Current search: {search_term}")
        print("\nMatching tools:")
        
        matches = get_top_matches(search_term)
        if matches:
            for i, (tool, _) in enumerate(matches, 1):
                print(f"{i}. {tool} - {tools_dict[tool]['command']}")
        else:
            print("No matches found")
        
        print("\nEnter number to execute, continue typing tool name, or use Backspace to delete")
        
        # Get single character input without requiring Enter (Linux version only)
        try:
            import termios
            import tty
            
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                char = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
                
            # Handle input
            if char.isdigit() and 1 <= int(char) <= len(matches):
                selected_tool = matches[int(char) - 1][0]
                tool_info = tools_dict[selected_tool]
                command = tool_info["command"]
                foreground = tool_info["foreground"]
                clear_screen()
                
                # Check if the command exists in PATH
                command_base = command.split()[0]
                if shutil.which(command_base):
                    if foreground:
                        # Run in foreground for terminal-based tools
                        os.system(command)
                        return  # Exit after the command finishes
                    else:
                        # Run in background for GUI tools
                        os.system(f"{command} &")
                        return  # Exit after launching
                else:
                    return  # Silently exit if command not found
            elif char == '\x03':  # Ctrl+C
                break
            elif char == '\x08' or char == '\x7f':  # Backspace
                if search_term:
                    search_term = search_term[:-1]
            else:
                search_term += char
                
        except KeyboardInterrupt:
            break
        except Exception:
            break

    clear_screen()
    print("Goodbye!")

if __name__ == "__main__":
    main()