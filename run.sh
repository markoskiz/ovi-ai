#!/bin/bash

# Set variables up
software_dir="$HOME/Software"
project_dir="$software_dir/ai"

# Detect the operating system
if [ -f /etc/os-release ]; then
    source /etc/os-release
    os_name=$ID
else
    os_name=$(uname -s)
fi

# Check if git is installed
if [ ! command -v git &> /dev/null ]; then
    echo "Git is not installed. Installing Git..."
    if [ "$os_name" = "ubuntu" ]; then
        sudo apt update
        sudo apt install git -y
    elif [ "$os_name" = "fedora" ]; then
        sudo dnf install git -y
    else
        # Add commands for other distributions here
        echo "Unsupported distribution. Please install Git manually."
        exit 1
    fi
else
    echo "Git is installed."
fi

# Check if podman is installed
if ! command -v podman &> /dev/null; then
    echo "Podman is not installed. Installing Podman..."
    if [ "$os_name" = "ubuntu" ]; then
        sudo apt update
        sudo apt install podman -y
    elif [ "$os_name" = "fedora" ]; then
        sudo dnf install podman -y
    else
        # Add commands for other distributions here
        echo "Unsupported distribution. Please install Podman manually."
        exit 1
    fi
else
    echo "Podman is installed."
fi

# Create the project directory if it doesn't exist
if [ ! -d "$project_dir" ]; then
    echo "Project directory is not installed."
    mkdir -p $software_dir
    cd $software_dir
    git clone https://gitlab.com/feeit-freecourseware/ai.git "$project_dir"
else
    echo "Project directory is installed."
    cd $project_dir
    git fetch
    git reset --hard origin/master
fi

# Pull the latest image
podman pull registry.gitlab.com/feeit-freecourseware/ai

# Spin a container
podman run -it --rm -p 8888:8888 -v $project_dir:/app:Z registry.gitlab.com/feeit-freecourseware/ai
