#!/bin/bash
git pull --all
git checkout -f jinja2
lastcommit=$(git rev-parse HEAD | cut -c0-10)
python generate.py
git checkout -f master
cp -r generated/* /
if git diff-index --quiet HEAD --; then
	echo "No changes made."
else
	git commit -a -m "Automatic update from commit $lastcommit."
fi
git checkout -f jinja2
