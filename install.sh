#!/bin/bash

detect_package_manager() {
    if command -v apt >/dev/null 2>&1; then
        PKG_MANAGER="apt"
        UPDATE_CMD="sudo apt update"
        INSTALL_CMD="sudo apt install -y"
    elif command -v yum >/dev/null 2>&1; then
        PKG_MANAGER="yum"
        UPDATE_CMD="sudo yum update -y"
        INSTALL_CMD="sudo yum install -y"
    elif command -v dnf >/dev/null 2>&1; then
        PKG_MANAGER="dnf"
        UPDATE_CMD="sudo dnf update -y"
        INSTALL_CMD="sudo dnf install -y"
    elif command -v pacman >/dev/null 2>&1; then
        PKG_MANAGER="pacman"
        UPDATE_CMD="sudo pacman -Syu"
        INSTALL_CMD="sudo pacman -S --noconfirm"
    else
        echo "Unsupported package manager. Please install tmux and python3 manually."
        exit 1
    fi
}

install_if_missing() {
    local package=$1
    local check_cmd=$2
    
    if ! command -v "$check_cmd" >/dev/null 2>&1; then
        echo "Installing $package..."
        $UPDATE_CMD
        $INSTALL_CMD "$package"
    else
        echo "$package is already installed"
    fi
}

handle_file() {
    local src_file=$1
    local dest_file=$2
    
    if [ -f "$dest_file" ]; then
        echo "File $dest_file already exists"
        echo "1) Replace existing file"
        echo "2) Keep existing file and create backup"
        echo "3) Skip"
        read -p "Choose an option (1-3): " choice
        
        case $choice in
            1)
                cp "$src_file" "$dest_file"
                echo "File replaced"
                ;;
            2)
                mv "$dest_file" "${dest_file}.backup-$(date +%Y%m%d_%H%M%S)"
                cp "$src_file" "$dest_file"
                echo "Backup created and file replaced"
                ;;
            3)
                echo "Skipping file installation"
                ;;
            *)
                echo "Invalid choice, skipping"
                ;;
        esac
    else
        cp "$src_file" "$dest_file"
        echo "Installed $src_file to $dest_file"
    fi
}


echo "Starting installation..."

detect_package_manager

install_if_missing "tmux" "tmux"
install_if_missing "python3" "python3"

TMUX_DIR="$HOME/.config/tmux"
if [ ! -d "$TMUX_DIR" ]; then
    mkdir -p "$TMUX_DIR"
    echo "Created directory $TMUX_DIR"
fi

handle_file "tmux.conf" "$TMUX_DIR/tmux.conf"
handle_file "launcher.py" "$TMUX_DIR/launcher.py"

echo "Installation complete!"
