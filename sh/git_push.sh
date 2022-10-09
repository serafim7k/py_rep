#!/bin/bash

read -p "Enter the commin name: " commit
read -p "Enter the branch name: " branch

git init
git add .
git commit -m "$commit"
git push -u origin $branch