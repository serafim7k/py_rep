#!/bin/bash

read -p "Enter the remote: " remote
read -p "Enter the commin name: " commit
read -p "Enter the branch name: " branch

git init
git add .
git commit -m "$commit"
git remote remove origin
git remote add origin $remote
git push -u origin $branch