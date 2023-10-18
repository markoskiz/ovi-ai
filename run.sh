#!/bin/bash

# Get the absolute directory path of the script
project_dir=$(dirname "$(readlink -f "$0")")

# Pull the latest image
podman pull registry.gitlab.com/feeit-freecourseware/ai

# Spin a container
podman run -it --rm -p 8888:8888 -v $project_dir:/app:Z registry.gitlab.com/feeit-freecourseware/ai

