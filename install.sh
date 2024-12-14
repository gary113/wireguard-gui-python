#!/bin/bash

set -e

INSTALL_DIR="/opt/wireguard-gui-python"
REPOSITORY="https://github.com/gary113/wireguard-gui-python.git"
SYSTEM_REQUIREMENTS_UBUNTU="$INSTALL_DIR/system-requirements-ubuntu.txt"
SYSTEM_REQUIREMENTS_FEDORA="$INSTALL_DIR/system-requirements-fedora.txt"
SYSTEM_REQUIREMENTS_ARCH="$INSTALL_DIR/system-requirements-arch.txt"
USER=$(whoami)

if [ -d "$INSTALL_DIR" ]; then
    sudo rm -rf "$INSTALL_DIR"
fi

sudo mkdir "$INSTALL_DIR"
sudo chown -R "$USER":"$USER" "$INSTALL_DIR"

git clone "$REPOSITORY" "$INSTALL_DIR"

if command -v apt-get; then
    sudo apt-get update
    sudo apt-get install -y $(cat "$SYSTEM_REQUIREMENTS_UBUNTU")
elif command -v dnf; then
    sudo dnf install -y $(cat "$SYSTEM_REQUIREMENTS_FEDORA")
elif command -v pacman; then
    sudo pacman -Sy --noconfirm $(cat "$SYSTEM_REQUIREMENTS_ARCH")
else
    echo "No compatible package manager found (apt-get, pacman, dnf)."
    sudo rm -rf "$INSTALL_DIR"
    exit 1
fi

python3 -m venv "$INSTALL_DIR/venv"
source "$INSTALL_DIR/venv/bin/activate"
pip3 install -r "$INSTALL_DIR/requirements.txt"
deactivate

chmod +x "$INSTALL_DIR/run.sh"
chmod +x "$INSTALL_DIR/resources/wgp.desktop"

sudo cp "$INSTALL_DIR/resources/wgp.desktop" /usr/share/applications

echo "Installation completed successfully."
