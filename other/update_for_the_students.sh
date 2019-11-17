#!/bin/bash

# execute update_master first
$(dirname $(readlink -f $0))/update_master.sh

remote_branches=false
git remote show origin | while read line; do
    if [ "$line" == "Remote branches:" ]; then
        remote_branches=true
        continue
    fi
    if [ "$remote_branches" == false ]; then
        continue
    fi
    if [ "$line" == "Local branch configured for 'git pull':" ]; then
        break
    fi
    set -- $line
    if [ "$1" == "master" ]; then
        continue
    fi
    echo "Update $1 from master"
    git checkout origin/$1
    git merge -X theirs -m "Branch merged with master to get the latest changes." origin/master
    git push origin HEAD:$1
    git checkout master
done

