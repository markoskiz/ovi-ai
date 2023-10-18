#!/bin/bash

# Check if git is installed
if [ ! command -v git &> /dev/null ]; then
    echo "Git is not installed. Installing Git..."
    # sudo dnf install git -y
else
    echo "Git is installed."
fi

# Check if podman is installed
if [ ! command -v podman &> /dev/null ]; then
    echo "Podman is not installed. Installing Podman..."
    # sudo dnf install podman -y
else
    echo "Podman is installed."
fi

# Set variables up
software_dir="$HOME/Software"
project_dir="$software_dir/ai"

# Create the project directory if it doesn't exist
if [ ! -d "$project_dir" ]; then
    echo "project dir is not installed."
    cd $software_dir
    git clone https://gitlab.com/feeit-freecourseware/ai.git "$project_dir"
else
    echo "project dir is installed."
    cd $project_dir
    git fetch
    git reset --hard origin/master
fi

# Pull the latest image
# podman pull registry.gitlab.com/feeit-freecourseware/ai

# Spin a container
podman run -it --rm -p 8888:8888 -v $project_dir:/app:Z registry.gitlab.com/feeit-freecourseware/ai

