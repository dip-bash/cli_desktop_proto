# Tmux Configuration and Launcher

A custom tmux configuration with a Python-based tool launcher for enhanced terminal productivity.

## Description

This project provides a customized tmux configuration file and a Python script that acts as a quick-launch tool for common applications and commands. The setup is designed for Linux GNOME environments and includes an installation script to set everything up automatically.

## Features

### Tmux Configuration
- Custom prefix (Ctrl-a)
- Mouse support
- Top status bar with time, date, and session info
- Easy window and pane management
- VI-style copy mode
- Custom key bindings:
  - F1: Terminal popup
  - F2: Tool launcher
  - Intuitive pane navigation and resizing

### Launcher.py
- Interactive tool search
- Quick-launch for common applications:
  - Terminal tools (ls, python3, git, htop)
  - GUI applications (calculator, browser, VSCode, etc.)
- Single-key execution
- Background/foreground execution based on tool type
- Auto-detection of available commands

## Technologies Used
- Tmux (Terminal Multiplexer)
- Python 3
- Bash (installation script)
- Linux GNOME environment

## Installation

1. Clone the repository:
```bash
git clone https://github.com/dip-bash/cli_desktop_proto.git
cd cli_desktop_proto
chmod +x install.sh
./install.sh

tmux
