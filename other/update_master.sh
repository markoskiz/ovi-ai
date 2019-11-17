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
    echo "Update master with $1 files"
    git checkout origin/$1 students/$1
done
git commit -m "Master acquired the latest changes."
git push
