#!/bin/bash

# Get the absolute directory path of the script
project_dir=$(dirname "$(readlink -f "$0")")

podman build -t registry.gitlab.com/feeit-freecourseware/ai "$project_dir"
